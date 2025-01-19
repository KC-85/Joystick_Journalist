from django.urls import path
from . import views

# URL patterns for the reviews app
urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Home page URL
    path('game/add/', views.add_game, name='add_game'),
    path('review/<int:game_id>/', views.review_page, name='review_page'),  # URL for a game's review page
]
