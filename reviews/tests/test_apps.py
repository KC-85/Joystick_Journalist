from django.apps import apps
from django.test import TestCase
from reviews.apps import ReviewsConfig


class ReviewsConfigTest(TestCase):
    """Test case for app configuration"""

    def test_app_name(self):
        """Check if app is configured correctly"""
        self.assertEqual(ReviewsConfig.name, 'reviews')
        self.assertEqual(apps.get_app_config('reviews').name, 'reviews')