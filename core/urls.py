from django.contrib import admin
from django.urls import path, include
import two_factor.urls
from reviews.views import CustomSetupView 

urlpatterns = [
    path('account/two_factor/setup/', CustomSetupView.as_view(), name='setup'),

    # Two-Factor Auth URLs with proper URL path
    path('', include(two_factor.urls.urlpatterns)),

    # Admin Panel
    path('admin/', admin.site.urls),

    # Main App URLs
    path('', include('reviews.urls')),
]

# Custom 404 Page
handler404 = "reviews.views.custom_404_view"
