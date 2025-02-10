from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SecureLoginView, SecureLogoutView, register


urlpatterns = [
    path('login/', SecureLoginView.as_view(), name='login'),
    path('logout/', SecureLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # ✅ Update these lines to use `game_form`
    path('', views.landing_page, name='landing_page'),
    path('game/add/', views.game_form, name='add_game'),  # 🛠️ Uses game_form for adding
    path('game/edit/<int:game_id>/', views.game_form, name='edit_game'),  # 🛠️ Uses same view for editing
    path('game/delete/<int:game_id>/', views.delete_game, name='delete_game'),

    path('review/<int:game_id>/', views.review_page, name='review_page'),
    path('review/<int:game_id>/add/', views.add_review, name='add_review'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('reviews/', views.all_reviews, name='all_reviews')
]
