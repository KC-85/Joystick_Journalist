from django.contrib import admin
from .models import Game, Review, Genre

# Import Axes models for security monitoring
from axes.models import AccessAttempt, AccessLog

# Register Models
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Genre)

# ✅ Prevent Double Registration of Axes Models
if not admin.site.is_registered(AccessAttempt):
    admin.site.register(AccessAttempt, AccessAttemptAdmin)

if not admin.site.is_registered(AccessLog):
    admin.site.register(AccessLog, AccessLogAdmin)
