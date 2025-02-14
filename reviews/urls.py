from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SecureLoginView, SecureLogoutView, register
import reviews.views as views

urlpatterns = [
    path('login/', SecureLoginView.as_view(), name='login'),
    path('logout/', SecureLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # ✅ Game URLs
    path('', views.landing_page, name='landing_page'),
    path('game/add/', views.game_form, name='add_game'),
    path('game/edit/<int:game_id>/', views.game_form, name='edit_game'),
    path('game/delete/<int:game_id>/', views.delete_game, name='delete_game'),

    # ✅ Review URLs
    path('review/<int:game_id>/', views.review_page, name='review_page'),
    path('review/<int:game_id>/add/', views.review_form, name='add_review'),
    path('review/edit/<int:review_id>/', views.review_form, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('reviews/', views.all_reviews, name='all_reviews')
]
