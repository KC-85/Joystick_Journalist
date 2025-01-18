from django.shortcuts import render, get_object_or_404
from .models import Game
from .models import GameForm, ReviewForm

# Create a new game
def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')

    else:
        form = GameForm()
    return render(request, 'reviews/add_game.html', {'form': form})

# Create a new review
def add_review(request, game_id):
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
    return render(request, 'reviews/add_review.html', {'form': form, 'game': game})

# View for the landing page
def landing_page(request):
    games = Game.objects.all()  # Fetch all games from the database
    return render(request, 'reviews/landing_page.html', {'games': games})  # Render the landing page template

# View for the review page of a specific game
def review_page(request, game_id):
    game = get_object_or_404(Game, id=game_id)  # Fetch the game or return a 404 if not found
    return render(request, 'reviews/review_page.html', {'game': game})  # Render the review page template
