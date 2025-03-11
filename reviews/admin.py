from django.contrib import admin
from .models import Game, Review, Genre
from axes.models import AccessAttempt, AccessLog  # Import Axes models for security monitoring

# Register Models
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Genre)

# ✅ Monitor failed login attempts (Django Axes)
@admin.register(AccessAttempt)
class AccessAttemptAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'attempt_time', 'failures_since_start')
    search_fields = ('username', 'ip_address')
    list_filter = ('attempt_time',)

# ✅ Monitor successful & failed logins (Django Axes)
@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'attempt_time', 'trusted')
    search_fields = ('username', 'ip_address')
    list_filter = ('trusted',)