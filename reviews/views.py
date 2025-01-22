from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Review
from .forms import GameForm, ReviewForm


"""View for the landing page"""
def landing_page(request):
    """Fetch all games from the database and render landing page."""
    games = Game.objects.all()
    return render(
        request, 'reviews/landing_page.html', {'games': games}
    )


"""View for the review page of a specific game"""
def review_page(request, game_id):
    """Fetch game and its reviews, then render review page."""
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.all()
    return render(
        request, 'reviews/review_page.html',
        {'game': game, 'reviews': reviews}
    )


"""View to add a new game"""
def add_game(request):
    """Handle form submission for adding a new game."""
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = GameForm()
    
    return render(
        request, 'reviews/add_game.html', {'form': form}
    )


"""View to add a new review for a specific game"""
def add_review(request, game_id):
    """Handle form submission for adding a review to a game."""
    game = get_object_or_404(Game, id=game_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.save()
            return redirect('review_page', game_id=game.id)
    else:
        form = ReviewForm()

    return render(
        request, 'reviews/add_review.html',
        {'form': form, 'game': game}
    )
