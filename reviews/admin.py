from django.contrib import admin
from .models import Game, Review, Genre

# Register Models
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Genre)