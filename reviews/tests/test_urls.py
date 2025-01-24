from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reviews.views import landing_page, review_page, add_game, add_review


class URLTests(SimpleTestCase):
    """Test case for URL resolutions"""

    def test_landing_page_url(self):
        """Test landing page URL"""
        url = reverse('landing_page')
        self.assertEqual(resolve(url).func, landing_page)

    def test_review_page_url(self):
        """Test review page URL with a valid game ID"""
        url = reverse('review_page', args=[1])
        self.assertEqual(resolve(url).func, review_page)

    def test_add_game_url(self):
        """Test add game URL"""
        url = reverse('add_game')
        self.assertEqual(resolve(url).func, add_game)

    def test_add_review_url(self):
        """Test add review URL"""
        url = reverse('add_review', args=[1])
        self.assertEqual(resolve(url).func, add_review)
