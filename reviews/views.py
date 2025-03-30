from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Avg
from collections import defaultdict

from django.contrib.auth import login, get_backends
from django.contrib.auth.views import LogoutView
from two_factor.views import LoginView as TwoFactorLoginView
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp import devices_for_user, user_has_device

from .models import Game, Review
from .forms import GameForm, ReviewForm, RegisterForm

# ✅ Secure Login with Two-Factor Check
class SecureLoginView(TwoFactorLoginView):
    template_name = 'reviews/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('landing_page')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        # ✅ Check if user has a confirmed 2FA device
        has_verified_device = any(
            device.verify_is_allowed() for device in devices_for_user(user)
            if isinstance(device, TOTPDevice) and device.confirmed
        )

        if user_has_device(user) and not has_verified_device:
            messages.error(self.request, "🔐 2FA device required. Please complete authentication.")
            return redirect("two_factor:login")

        messages.success(self.request, "✅ Logged in successfully with 2FA!")
        return redirect(self.get_success_url())

# ✅ Secure Logout
class SecureLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "🎮 You have been logged out successfully!")
        return super().dispatch(request, *args, **kwargs)

# ✅ 2FA Setup Override for QR code visibility
from two_factor.views.core import SetupView

class CustomSetupView(SetupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = self.get_device() if hasattr(self, 'get_device') else None
        if device and hasattr(device, 'config_url'):
            context['qr_code_url'] = device.config_url
        return context

# ✅ User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            backend = get_backends()[0]
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

            login(request, user)
            messages.success(request, "🎉 Account created successfully! Welcome to Joystick Journalist 🎮")
            return redirect('two_factor:setup')
        else:
            print("\n❌ DEBUG: Registration failed due to the following errors:")
            print(form.errors.as_json())
            messages.error(request, "⚠️ Registration failed. Please fix the errors below.")
    else:
        form = RegisterForm()

    return render(request, "reviews/register.html", {"form": form})

# ✅ Landing Page
def landing_page(request):
    games = Game.objects.select_related('genre').annotate(
        average_rating=Avg('reviews__rating')
    ).order_by('-release_year')

    return render(request, 'reviews/landing_page.html', {
        'games': games,
        'user_authenticated': request.user.is_authenticated
    })

# ✅ Review Page
def review_page(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.all()
    form = ReviewForm()

    return render(request, 'reviews/review_page.html', {
        'game': game,
        'reviews': reviews,
        'form': form
    })

# ✅ Create & Edit Game
def game_form(request, game_id=None):
    game = get_object_or_404(Game, id=game_id) if game_id else None
    form = GameForm(request.POST or None, instance=game)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('landing_page')

    return render(request, 'reviews/form_page.html', {
        'form': form,
        'title': "Edit Game" if game else "Add Game"
    })

# ✅ Delete Game
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        game.delete()
        return redirect('landing_page')

    return render(request, 'reviews/confirm_delete.html', {
        'object': game,
        'type': 'game'
    })

# ✅ Create & Edit Review
def review_form(request, game_id, review_id=None):
    game = get_object_or_404(Game, id=game_id)
    review = get_object_or_404(Review, id=review_id) if review_id else None
    form = ReviewForm(request.POST or None, instance=review)

    if request.method == "POST" and form.is_valid():
        new_review = form.save(commit=False)
        new_review.game = game
        new_review.save()
        return redirect('review_page', game_id=game.id)

    return render(request, 'reviews/form_page.html', {
        'form': form,
        'title': "Edit Review" if review else "Add Review",
        'game': game
    })

# ✅ Delete Review
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    game_id = review.game.id

    if request.method == "POST":
        review.delete()
        return redirect('review_page', game_id=game_id)

    return render(request, 'reviews/confirm_delete.html', {
        'object': review,
        'type': 'review'
    })

# ✅ All Reviews Grouped by Game
def all_reviews(request):
    reviews = Review.objects.select_related('game').all().order_by('-id')
    grouped_reviews = defaultdict(list)

    for review in reviews:
        grouped_reviews[review.game.title].append(review)

    return render(request, 'reviews/all_reviews.html', {
        'grouped_reviews': dict(grouped_reviews),
        'title': "All Reviews"
    })

# ✅ Custom 404 Handler
def custom_404_view(request, exception):
    return render(request, "errors/404.html", status=404)
