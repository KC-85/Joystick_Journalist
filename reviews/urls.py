from django.urls import path
from .views import game_form, review_form
from django.contrib.auth import views as auth_views
from .views import SecureLoginView, SecureLogoutView, register
import reviews.views as views

urlpatterns = [
    path('account/login/', SecureLoginView.as_view(), name='login'),
    path('account/logout/', SecureLogoutView.as_view(), name='logout'),
    path('account/register/', register, name='register'),

    # ✅ Game URLs
    path('', views.landing_page, name='landing_page'),
    path('game/add/', views.game_form, name='game_form'),
    path('game/edit/<int:game_id>/', views.game_form, name='edit_game'),
    path('game/delete/<int:game_id>/', views.delete_game, name='delete_game'),

    # ✅ Review URLs
    path('review/<int:game_id>/add/', views.review_form, name='add_review'),
    path('review/edit/<int:review_id>/', 
        views.edit_review, 
        name='edit_review'),
    path('review/delete/<int:review_id>/', 
        views.delete_review, 
        name='delete_review'),
    path('reviews/', views.all_reviews, name='all_reviews')
]
