from django.contrib.admin.sites import site
from django.test import TestCase
from reviews.models import Game, Review


class AdminSiteTest(TestCase):
    """Test case for Django Admin Site"""

    def test_game_registered(self):
        """Test if Game model is registered in Admin"""
        self.assertTrue(site.is_registered(Game))

    def test_reviewed_registered(self):
        """Test if Review model is registered in Admin"""
        self.assertTrue(site.is_registered(Review))
