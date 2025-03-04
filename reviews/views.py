from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Avg
from .models import Game, Review
from .forms import GameForm, ReviewForm, RegisterForm
from collections import defaultdict

# ✅ Secure Authentication Views
class SecureLoginView(LoginView):
    template_name = 'reviews/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('landing_page')

    def get_success_url(self):
        return self.request.GET.get('next', self.next_page)

class SecureLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully! 🎮")
        return super().dispatch(request, *args, **kwargs)

# ✅ Fixed User Registration
def register(request):
    print("✅ DEBUG: register view called!")  # Debugging print statement

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # ✅ No need for set_password()
            login(request, user)  # ✅ Auto-login after registration
            print("✅ DEBUG: User registered successfully!")

            request.session['registered_before'] = True
            messages.success(request, "🎉 Account created successfully! Welcome to Joystick Journalist 🎮")

            return redirect('landing_page')  # ✅ Redirect to homepage after signup
        else:
            messages.error(request, "⚠️ Registration failed. Please fix the errors below.")

    else:
        form = RegisterForm()

    return render(request, "reviews/register.html", {"form": form})
    
    print("✅ DEBUG: Rendering register.html")  # Print before rendering template
    return render(request, 'reviews/register.html', {'form': form, 'title': "Register"})

# ✅ Landing Page
def landing_page(request):
    games = Game.objects.select_related('genre').annotate(
        average_rating=Avg('reviews__rating')
    ).order_by('-release_year')  # Sort by newest release first

    context = {
        'games': games,
        'user_authenticated': request.user.is_authenticated  # ✅ Pass authentication status
    }

    return render(request, 'reviews/landing_page.html', {'games': games})

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

# ✅ Create & Edit Game (Unified View)
def game_form(request, game_id=None):
    game = get_object_or_404(Game, id=game_id) if game_id else None
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = GameForm(instance=game)

    return render(request, 'reviews/form_page.html', {'form': form, 'title': "Edit Game" if game else "Add Game"})

# ✅ Delete Game
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        game.delete()
        return redirect('landing_page')
    return render(request, 'reviews/confirm_delete.html', {'object': game, 'type': 'game'})

# ✅ Create & Edit Review (Unified View)
def review_form(request, game_id, review_id=None):
    game = get_object_or_404(Game, id=game_id)
    review = get_object_or_404(Review, id=review_id) if review_id else None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.game = game
            new_review.save()
            return redirect('review_page', game_id=game.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/form_page.html', {
        'form': form, 
        'title': "Edit Review" if review else "Add Review",
        'game': game
    })

# ✅ Delete Review
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    game_id = review.game.id  # ✅ Store game ID before deleting review

    if request.method == "POST":
        review.delete()
        return redirect('review_page', game_id=game_id)  # ✅ Redirect back to game review page

    return render(request, 'reviews/confirm_delete.html', {'object': review, 'type': 'review'})

# ✅ List All Reviews Grouped by Game
def all_reviews(request):
    reviews = Review.objects.select_related('game').all().order_by('-id')

    grouped_reviews = defaultdict(list)
    for review in reviews:
        grouped_reviews[review.game.title].append(review)  # Store under game title

    # Convert defaultdict to a normal dictionary
    grouped_reviews = dict(grouped_reviews)

    print("\nDEBUG: Grouped Reviews Data\n")  # Print debug output
    for game, reviews in grouped_reviews.items():
        print(f"Game: {game}, Reviews: {len(reviews)}")
        for r in reviews:
            print(f" - {r.reviewer_name}: {r.rating}/5 - {r.comment}")

    return render(request, 'reviews/all_reviews.html', {
        'grouped_reviews': grouped_reviews,
        'title': "All Reviews"
    })
