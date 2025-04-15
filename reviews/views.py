from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Avg
from django.contrib.auth import login, get_backends
from django.contrib.auth.decorators import login_required
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
    ).order_by('title')

    return render(request, 'reviews/landing_page.html', {
        'games': games,
        'user_authenticated': request.user.is_authenticated
    })


# ✅ Review Page
@login_required
def review_form(request, game_id):
    """
    Form to add a new review
    """
    game = get_object_or_404(Game, id=game_id)
    form = ReviewForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.reviewer_name = request.user
            new_review.game = game
            new_review.save()
            messages.success(request, "Review added successfully.")
            return redirect('all_reviews')
        messages.error(request, "Review not posted, please try again.")

    return render(request, 'reviews/form_page.html', {
        'form': form,
        'title': "Add Review",
        'game': game
    })


# ✅ Edit Review
@login_required
def edit_review(request, review_id):
    """
    Form to edit an existing review (user-specific)
    """
    review = get_object_or_404(Review, id=review_id)
    game = review.game
    print("DEBUG - review:", review)

    if review:
        print("🧠 DEBUG — Logged in user:", request.user.username)
        print("🧠 DEBUG — Review owner:", review.reviewer_name)

    # 🔐 Block users from editing others' reviews
    if review and review.reviewer_name != request.user:
        messages.error(request, "🚫 You are not allowed to edit this review.")
        return redirect('all_reviews')

    form = ReviewForm(request.POST or None, instance=review)

    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.reviewer_name = request.user  # ✅ SET reviewer_name properly
            review.save()
            messages.success(request, "Review updated successfully.")
            return redirect('all_reviews')
        messages.error(request, "Error, please try again")

    return render(request, 'reviews/form_page.html', {
        'form': form,
        'title': "Edit Review",
        'game': game,
        'review': review,
    })


# ✅ Create Game
@login_required
def game_form(request, game_id=None):
    """
    Form to add a new game (only for superuser)
    """
    if not request.user.is_superuser:
        messages.error(request, "🚫 You are not allowed to manage games.")
        return redirect('landing_page')

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
@login_required
def delete_game(request, game_id):
    """
    Form to delete a game (only for superuser)
    """
    if not request.user.is_superuser:
        messages.error(request, "🚫 You are not allowed to delete this game.")
        return redirect('landing_page')

    game = get_object_or_404(Game, id=game_id)
    game.delete()
    messages.success(request, "Game deleted successfully")
    return redirect('landing_page')


# ✅ Delete Review
@login_required
def delete_review(request, review_id):
    """
    Form to delete an existing review (user-specific)
    """
    review = get_object_or_404(Review, id=review_id)
    game_id = review.game.id

    # 🔐 Block users from deleting others' reviews
    if review and review.reviewer_name != request.user:
        messages.error(request, "🚫 You are not allowed to delete this review.")
        return redirect('all_reviews')

    review.delete()
    messages.success(request, "Review deleted successfully")
    return redirect('all_reviews')


# ✅ All Reviews Grouped by Game
@login_required
def all_reviews(request):
    """
    Page to retrieve all reviews
    """
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
    """
    Error 404 page
    """
    return render(request, "errors/404.html", status=404)
