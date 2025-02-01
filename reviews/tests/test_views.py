from django.urls import reverse
from django.test import TestCase
from reviews.models import Game, Genre


class LandingPageViewTest(TestCase):
    """Test case for the Landing Page View"""

    def setUp(self):
        """Create a Genre and Game instance"""
        self.genre = Genre.objects.create(name="Action")
        Game.objects.create(
            title="Super Metroid",
            release_year=1994,
            genre=self.genre
        )

    def test_landing_page_status_code(self):
        """Check if the landing page loads correctly"""
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/landing_page.html')


class ReviewPageViewTest(TestCase):
    """Test case for the Review Page View"""

    def setUp(self):
        """Create a Genre and Game instance for the review page"""
        self.genre = Genre.objects.create(name="Fighting")
        self.game = Game.objects.create(
            title="Killer Instinct",
            release_year=1994,
            genre=self.genre
        )

    def test_review_page_status_code(self):
        """Check if the review page loads correctly"""
        response = self.client.get(reverse('review_page', args=[self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_page.html')
