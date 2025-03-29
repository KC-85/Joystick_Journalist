from django.contrib import admin
from django.urls import path, include
import two_factor.urls # ✅ Import two_factor urls directly

urlpatterns = [
    # Two-Factor Auth URLs with proper namespace and app_name
    path('account/', include(two_factor.urls.urlpatterns)),

    # Admin Panel
    path('admin/', admin.site.urls),

    # Main App URLs
    path('', include('reviews.urls')),
]

# Custom 404 Page
handler404 = "reviews.views.custom_404_view"

