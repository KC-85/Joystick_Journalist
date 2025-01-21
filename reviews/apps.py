from django.apps import AppConfig

# Configuration class for the reviews app


class ReviewsConfig(AppConfig):
    # Default type for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'  # Name of the app
