from django.shortcuts import redirect
from django.conf import settings


class LoginRequiredMiddleware:
    """
    Middleware to restrict all views to authenticated users,
    except login, registration and password reset pages.
    """

    EXEMPT_URLS = [
        "/",
        "/account/login/",
        "/account/register/",
        "/password_reset/",
        "/password_reset_done/",
        "/reset/",
        "/reset_done/"
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ✅ Authenticated users are always allowed
        if request.user.is_authenticated:
            return self.get_response(request)

        current_path = request.path_info
        if any(current_path.startswith(url) for url in self.EXEMPT_URLS):
            return self.get_response(request)

        # 🚫 All other paths redirect to login
        return redirect(f"{settings.LOGIN_URL}?next={current_path}")
