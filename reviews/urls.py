from django.urls import path
from . import views

# URL patterns for the reviews app
urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Home page
    path('game/add/', views.add_game, name='add_game'),  # Add a new game
    path(
        'review/<int:game_id>/',
        views.review_page,
        name='review_page'
    ),  # View reviews for a game
    path(
        'review/<int:game_id>/add/',
        views.add_review,
        name='add_review'
    ),  # Add a review for a game
    path('reviews/', views.all_reviews, name='all_reviews'),
]
