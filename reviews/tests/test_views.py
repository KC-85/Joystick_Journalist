from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from reviews.models import Game, Genre

User = get_user_model()


class LandingPageViewTest(TestCase):
    """Test case for the Landing Page View"""

    def setUp(self):
        """Create a test user and a game instance"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.genre = Genre.objects.create(name="Action/Adventure")
        Game.objects.create(
            title="Super Metroid",
            release_year=1994,
            genre=self.genre
        )

    def test_landing_page_status_code(self):
        """Check if the landing page loads correctly"""

        # Skip Axes backend
        self.client.force_login(self.user)
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/landing_page.html')


class ReviewPageViewTest(TestCase):
    """Test case for the Review Page View"""

    def setUp(self):
        """Create a test user and a game instance"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.genre = Genre.objects.create(name="Action/Adventure")
        self.game = Game.objects.create(
            title="Super Metroid",
            release_year=1994,
            genre=self.genre
        )

    def test_review_page_status_code(self):
        """Check if the review page loads correctly"""

        # Authenticated user
        response = self.client.force_login(self.user)
        response = self.client.get(reverse('add_review', args=[self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/form_page.html')
