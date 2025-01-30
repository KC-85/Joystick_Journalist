from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Review
from .forms import GameForm, ReviewForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class SecureLoginView(LoginView):
    template_name = 'reviews/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('landing_page')

    def get_success_url(self):
        return self.request.GET.get('next', self.next_page)

class SecureLogoutView(LogoutView):
    next_page = reverse_lazy('login')

def landing_page(request):
    games = Game.objects.all()
    return render(request, 'reviews/landing_page.html', {'games': games})

def review_page(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.all()
    return render(request, 'reviews/review_page.html', {'game': game, 'reviews': reviews})

def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = GameForm()
    return render(request, 'reviews/add_game.html', {'form': form})

def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = GameForm(instance=game)
    return render(request, 'reviews/edit_game.html', {'form': form, 'game': game})

def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        game.delete()
        return redirect('landing_page')
    return render(request, 'reviews/delete_game.html', {'game': game})

def add_review(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        print("🛠️ Received POST request:", request.POST)  # Debugging print
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.save()
            print("✅ Review saved successfully!")  # Debugging print
            return redirect('review_page', game_id=game.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_page.html', {'form': form, 'game': game})

def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_page', game_id=review.game.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        game_id = review.game.id
        review.delete()
        return redirect('review_page', game_id=game_id)
    return render(request, 'reviews/delete_review.html', {'review': review})

def all_reviews(request):
    """Fetch all reviews from the database and render the page."""
    reviews = Review.objects.all()
    return render(
        request, 'reviews/all_reviews.html',
        {'reviews': reviews}
    )