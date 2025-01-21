from django import forms
from .models import Game, Review


"""Form for creating or updating a Game"""


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'release_year', 'genre']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter game title'
                }
            ),
            'release_year': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Release year'
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Genre'
                }
            ),
        }


"""Form for creating or updating a Review"""


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'reviewer_name', 'rating', 'comment']
        widgets = {
            'game': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'reviewer_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name'
                }
            ),
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your review'
                }
            ),
        }
