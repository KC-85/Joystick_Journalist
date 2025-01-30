from django.urls import path
from . import views, SecureLoginView, SecureLogoutView, register


urlpatterns = [
    path('login/', SecureLoginView.as_view(), name='login'),
    path('logout/', SecureLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', views.landing_page, name='landing_page'),
    path('game/add/', views.add_game, name='add_game'),
    path('game/edit/<int:game_id>/', views.edit_game, name='edit_game'),
    path('game/delete/<int:game_id>/', views.delete_game, name='delete_game'),
    path('review/<int:game_id>/', views.review_page, name='review_page'),
    path('review/<int:game_id>/add/', views.add_review, name='add_review'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('reviews/', views.all_reviews, name='all_reviews'),
]
