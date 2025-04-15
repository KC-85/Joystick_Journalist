from django.test import TestCase
from django.contrib.auth import get_user_model
from reviews.models import Game, Review, Genre

User = get_user_model()

class ReviewModelTest(TestCase):
    """Test case for the Review model"""

    def setUp(self):
        """Create test data for Genre, Game, User, and Review"""
        self.genre = Genre.objects.create(name="Racing")
        self.game = Game.objects.create(
            title="Super Metroid",
            release_year=1994,
            genre=self.genre
        )

        # ✅ Create a user instance
        self.user = User.objects.create_user(username="johnsmith", password="testpass123")

        # ✅ Assign user to reviewer_name
        self.review = Review.objects.create(
            game=self.game,
            reviewer_name=self.user,
            rating=5,
            comment="Amazing game!"
        )

    def test_review_creation(self):
        """Test review creation and ForeignKey relationship"""
        self.assertEqual(str(self.review), "johnsmith - Super Metroid")
        self.assertEqual(self.review.game, self.game)
