from django.db import models

# Model representing a 90s game
class Game(models.Model):
    title = models.CharField(max_length=100)  # Game title (e.g., Super Metroid)
    release_year = models.IntegerField()  # Year the game was released
    genre = models.CharField(max_length=50)  # Genre of the game (e.g., Action)

    def __str__(self):
        return self.title  # Display the game title as the string representation

# Model representing a review for a game
class Review(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="reviews"
    )  # Link to the Game model; delete reviews if the game is deleted
    reviewer_name = models.CharField(max_length=100)  # Name of the reviewer
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )  # Rating from 1 to 5
    comment = models.TextField()  # Text of the review
    review_date = models.DateTimeField(auto_now_add=True)  # Auto-populate with the date the review was created

    def __str__(self):
        return f"{self.reviewer_name} - {self.game.title}"  # Display reviewer name and game title
