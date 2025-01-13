from django.apps import AppConfig

# Configuration class for the reviews app
class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Default type for primary keys
    name = 'reviews'  # Name of the app
