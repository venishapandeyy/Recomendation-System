from django.test import TestCase
from django.urls import reverse, resolve
from .views import home,loginuser, logoutuser,register,rating
from .models import Moviess
# Create your tests here.
class UnitTesting(TestCase) :
    def test_views_home(self):
         url = reverse("home")
         self.assertEquals(resolve(url).func, home)
    def test_views_register(self):
         url = reverse("register")
         self.assertEquals(resolve(url).func, register)

    def test_views_login(self):
         url = reverse("login")
         self.assertEquals(resolve(url).func, loginuser)

    def test_views_logout(self):
         url = reverse("logout")
         self.assertEquals(resolve(url).func, logoutuser)

    def test_views_rating(self):
         url = reverse("rating", args=[1])
         self.assertEquals(resolve(url).func, rating)
