from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Main App URLs
    path('', include('reviews.urls')),
]

# Custom 404 Page
handler404 = "reviews.views.custom_404_view"
