from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    """
    Middleware to restrict all views to authenticated users,
    except login, registration and password reset pages.
    """

    EXEMPT_URLS = [
        "/",                 # 👈 Add the landing page (root URL)
        "/login/",
        "/register/",
        "/password_reset",
        "/password_reset_done/",
        "/reset/",
        "/reset_done/"
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow authenticated users to access all pages
        if request.user.is_authenticated:
            return self.get_response(request)

        # Allow public access to exempt URLS (login, registration, password reset)
        current_path = request.path_info
        if any(current_path.startswith(url) for url in self.EXEMPT_URLS):
            return self.get_response(request)

        # Redirect unauthenticated users to login
        return redirect(f"{settings.LOGIN_URL}?next={current_path}")
