from django.urls import path
from . import views

# URL patterns for the reviews app
urlpatterns = [
    path(
        '', 
        views.landing_page, 
        name='landing_page'
    ),  # Home page
    path(
        'game/add/', 
        views.add_game, 
        name='add_game'
    ),  # Add a new game
    path(
        'review/<int:game_id>/',
        views.review_page,
        name='review_page'
    ),  # View reviews for a game
    path(
        'reviews/', 
        views.all_reviews, 
        name='all_reviews'
    ),
    path(
        'game/add/', 
        views.game_form, 
        name='add_game'
    ),
    path(
        'game/<int:game_id>/edit/', 
        views.game_form, 
        name='edit_game'
    ),
    path(
        'review/<int:game_id>/add/', 
        views.review_form, 
        name='add_review'
    ),
    path(
        'review/<int:game_id>/<int:review_id>/edit/', 
        views.review_form, 
        name='edit_review'
    ),
]
