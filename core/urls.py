from django.contrib import admin
from django.urls import path, include
import two_factor.urls

urlpatterns = [
    path('account/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),  # ✅ Correct format
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),  # Your app URLs
]

# Custom 404 handler
handler404 = "reviews.views.custom_404_view"
