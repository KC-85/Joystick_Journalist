from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),  # Include URLs from the reviews app
]

handler404 = "reviews.views.custom_404_view"
