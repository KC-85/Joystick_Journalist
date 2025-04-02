from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Avg
from django.contrib.auth import login, get_backends
from django.contrib.auth.views import LoginView, LogoutView
from collections import defaultdict

from .models import Game, Review
from .forms import GameForm, ReviewForm, RegisterForm

# ✅ Secure Login (without 2FA)
class SecureLoginView(LoginView):
    template_name = 'reviews/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('landing_page')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, "✅ Logged in successfully!")
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.request.GET.get('next', self.next_page)

# ✅ Secure Logout
class SecureLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "🎮 You have been logged out successfully!")
        return super().dispatch(request, *args, **kwargs)

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
            return redirect('landing_page')
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
def review_form(request, game_id, review_id=None):
    game = get_object_or_404(Game, id=game_id)
    review = get_object_or_404(Review, id=review_id) if review_id else None

    # 🔐 Block users from editing others' reviews
    if review and review.reviewer_name != request.user.username:
        messages.error(request, "🚫 You are not allowed to edit this review.")
        return redirect('review_page', game_id=game.id)

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

# ✅ Edit Review
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    game = review.game
    print("DEBUG - review:", review)

    if review:
        print("🧠 DEBUG — Logged in user:", request.user.username)
        print("🧠 DEBUG — Review owner:", review.reviewer_name)

    # if review.reviewer_name != request.user.username:
    #     return redirect('review_page', game_id=game.id)

    form = ReviewForm(request.POST or None, instance=review)

    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.game = game
        review.reviewer_name = request.user.username  # ✅ SET reviewer_name properly
        review.save()
        return redirect('all_reviews')

    return render(request, 'reviews/form_page.html', {
        'form': form,
        'title': "Edit Review",
        'game': game
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
