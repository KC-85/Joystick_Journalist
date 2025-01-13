from django.shortcuts import render, get_object_or_404
from .models import Game

# View for the landing page
def landing_page(request):
    games = Game.objects.all()  # Fetch all games from the database
    return render(request, 'reviews/landing_page.html', {'games': games})  # Render the landing page template

# View for the review page of a specific game
def review_page(request, game_id):
    game = get_object_or_404(Game, id=game_id)  # Fetch the game or return a 404 if not found
    return render(request, 'reviews/review_page.html', {'game': game})  # Render the review page template
