from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Game, Review, Genre
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Form for registering a new user
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
    
        if password1 and password2:
            if password1 != password2:
                raise ValidationError("Passwords do not match. Please try again.")
            if len(password1) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
    
        return password2   

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
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Write your review'}
            ),
        }
