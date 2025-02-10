from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Game, Review
from .forms import GameForm, ReviewForm, RegisterForm

# ✅ Secure Authentication Views
class SecureLoginView(LoginView):
    template_name = 'reviews/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('landing_page')

    def get_success_url(self):
        return self.request.GET.get('next', self.next_page)

class SecureLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# ✅ User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            return redirect('login')  # Redirect to login page
    else:
        form = RegisterForm()
    
    return render(request, 'reviews/form_page.html', {'form': form, 'title': "Register"})

# ✅ Landing Page
def landing_page(request):
    games = Game.objects.select_related('genre').all()
    return render(request, 'reviews/landing_page.html', {'games': games})

# ✅ Review Page
def review_page(request, game_id):
    game = get_object_or_404(Game.objects.prefetch_related('reviews'), id=game_id)
    form = ReviewForm()
    return render(request, 'reviews/review_page.html', {'game': game, 'form': form})

# ✅ Create & Edit Game (Unified View)
def game_form(request, game_id=None):
    game = get_object_or_404(Game, id=game_id) if game_id else None
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = GameForm(instance=game)

    return render(request, 'reviews/form_page.html', {'form': form, 'title': "Edit Game" if game else "Add Game"})

# ✅ Delete Game
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        game.delete()
        return redirect('landing_page')
    return render(request, 'reviews/confirm_delete.html', {'object': game, 'type': 'game'})

# ✅ Create & Edit Review (Unified View)
def review_form(request, game_id, review_id=None):
    game = get_object_or_404(Game, id=game_id)
    review = get_object_or_404(Review, id=review_id) if review_id else None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.game = game
            new_review.save()
            return redirect('review_page', game_id=game.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/form_page.html', {
        'form': form, 
        'title': "Edit Review" if review else "Add Review",
        'game': game
    })

# ✅ Delete Review
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        game_id = review.game.id
        review.delete()
        return redirect('review_page', game_id=game_id)
    return render(request, 'reviews/confirm_delete.html', {'object': review, 'type': 'review'})

# ✅ List All Reviews
def all_reviews(request):
    reviews = Review.objects.select_related('game').all()
    return render(request, 'reviews/review_page.html', {'reviews': reviews, 'title': "All Reviews"})
