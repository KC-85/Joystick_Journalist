from django import forms
from .models import Game, Review, Genre
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Form for registering a new user
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        min_length=12
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        min_length=12
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

"""Form for creating or updating a Game"""
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'release_year', 'genre']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter game title'}
            ),
            'release_year': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Release year'}
            ),
            'genre': forms.Select(  # Now using a Select widget for ForeignKey
                attrs={'class': 'form-control'}
            ),
        }

"""Form for creating or updating a Review"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'comment']
        widgets = {
            'reviewer_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your name'}
            ),
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Write your review'}
            ),
        }
