from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls 

urlpatterns = [
    path('', include(tf_urls)),
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),  # Include URLs from the reviews app
]

handler404 = "reviews.views.custom_404_view"
