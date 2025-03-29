from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ✅ Two-Factor Auth URLs (uses 'two_factor' namespace internally)
    path("account/", include("two_factor.urls", namespace="two_factor")),

    # ✅ Django Admin Panel
    path("admin/", admin.site.urls),

    # ✅ Your Reviews App URLs
    path("", include("reviews.urls")),
]

# ✅ Custom 404 Error Handler
handler404 = "reviews.views.custom_404_view"
