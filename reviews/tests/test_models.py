from django.test import TestCase
from reviews.models import Game, Review, Genre


class GameModelTest(TestCase):
    """Test case for the Game model"""

    def setUp(self):
        """Create a Genre and Game instance for testing"""
        self.genre = Genre.objects.create(name="Action")
        self.game = Game.objects.create(
            title="Super Metroid",
            release_year=1994,
            genre=self.genre
        )

    def test_game_creation(self):
        """Test that the game is created correctly"""
        self.assertEqual(str(self.game), "Super Metroid")


class ReviewModelTest(TestCase):
    """Test case for the Review model"""

    def setUp(self):
        """Create a Genre, Game, and Review instance"""
        self.genre = Genre.objects.create(name="Racing")
        self.game = Game.objects.create(
            title="Super Mario Kart",
            release_year=1992,
            genre=self.genre
        )

        self.review = Review.objects.create(
            game=self.game,
            reviewer_name="John Smith",
            rating=5,
            comment="Amazing game!"
        )

    def test_review_creation(self):
        """Test review creation and ForeignKey relationship"""
        self.assertEqual(str(self.review), "John Smith - Super Mario Kart")
        self.assertEqual(self.review.game, self.game)
