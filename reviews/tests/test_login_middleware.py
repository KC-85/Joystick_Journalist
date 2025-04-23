from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.conf import settings

from reviews.login_middleware import LoginRequiredMiddleware


class LoginRequiredMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        # Setup a working dummy response function
        def dummy_get_response(request):
            return HttpResponse("OK")

        self.middleware = LoginRequiredMiddleware(dummy_get_response)

    def test_authenticated_user_has_access(self):
        user = User.objects.create_user(username="tester", password="test123")
        request = self.factory.get("/some-private-page/")
        request.user = user
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_user_exempt_urls(self):
        exempt_urls = [
            "/",  # Even if the view has login_required, this tests middleware only
            "/account/login/",
            "/register/",
            "/password_reset",
            "/password_reset_done/",
            "/reset/",
            "/reset_done/"
        ]
        for url in exempt_urls:
            request = self.factory.get(url)
            request.user = AnonymousUser()
            response = self.middleware(request)
            self.assertEqual(response.status_code, 200, f"Expected OK on exempt URL: {url}")

    def test_anonymous_user_blocked_urls(self):
        protected_urls = [
        ]
        for url in protected_urls:
            request = self.factory.get(url)
            request.user = AnonymousUser()
            response = self.middleware(request)
            self.assertEqual(response.status_code, 302, f"Expected redirect for protected URL: {url}")
            self.assertIn(settings.LOGIN_URL, response.url)
