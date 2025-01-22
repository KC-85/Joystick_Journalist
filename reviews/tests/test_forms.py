from django.test import TestCase
from reviews.forms import GameForm, ReviewForm
from reviews.models import Game


class GameFormTest(TestCase):
    """Test case for the GameForm"""

    def test_game_form_valid_data(self):
        """Test if GameForm is valid with correct data"""
        form = GameForm(data={'title': 'Super Metroid', 'release_year': 1994, 'genre': 'Action'})
        self.assertTrue(form.is_valid())

    def test_game_form_missing_fields(self):
        """Test if GameForm is invalid when fields are missing"""
        form = GameForm(data={'title': ''})  # Missing release_year & genre
        self.assertFalse(form.is_valid())
        self.assertIn('release_year', form.errors)
        self.assertIn('genre', form.errors)


class ReviewFormTest(TestCase):
    """Test case for the ReviewForm"""

    def setUp(self):
        """Create a game instance for reviews"""
        self.game = Game.objects.create(title="Super Metroid", release_year=1994, genre="Action")

    def test_review_form_valid_data(self):
        """Test if ReviewForm is valid with correct data"""
        form = ReviewForm(data={
            'game': self.game.id,
            'reviewer_name': 'John Doe',
            'rating': 5,
            'comment': 'Amazing game!'
        })
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_rating(self):
        """Test if ReviewForm is invalid with an out-of-range rating"""
        form = ReviewForm(data={
            'game': self.game.id,
            'reviewer_name': 'John Doe',
            'rating': 6,  # Invalid rating (should be 1-5)
            'comment': 'Amazing game!'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

    def test_review_form_missing_fields(self):
        """Test if ReviewForm is invalid when fields are missing"""
        form = ReviewForm(data={'game': self.game.id, 'reviewer_name': ''})  # Missing rating & comment
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)
        self.assertIn('comment', form.errors)
