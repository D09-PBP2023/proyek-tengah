from django.test import Client, TestCase
from django.contrib import auth
from django.contrib.auth import get_user_model

from users.forms import UserRegistrationForm

class AuthTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.client = Client()
    
    def test_login_url_is_exist(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_using_correct_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')
    
    def test_register_url_is_exist(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_using_correct_template(self):
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'register.html')

    def test_logout_url_is_exist_when_not_signed_in(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_redirect_login_page(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/login/')
        self.assertRedirects(response, '/')

    def test_redirect_register_page(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/register/')
        self.assertRedirects(response, '/')

    def test_redirect_logout_page(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/login/')

    def test_success_login_via_endpoint(self):
        self.client.post('/login/', {'username': 'temporary', 'password': 'temporary'})
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_fail_login_via_endpoint(self):
        self.client.post('/login/', {'username': 'temporary', 'password': 'temporary123'})
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
    
    def test_success_register_via_endpoint(self):
        self.client.post('/register/', {'username': 'temporary2', 'password1': 'kelompokpbp123', 'password2': 'kelompokpbp123'})
        user = get_user_model().objects.filter(username__iexact='temporary2')
        self.assertTrue(user.exists())

    def test_fail_register_via_endpoint(self):
        self.client.post('/register/', {'username': 'temporary2', 'password1': 'kelompokpbp12', 'password2': 'kelompokmppi'})
        user = get_user_model().objects.filter(username='temporary2')
        self.assertFalse(user.exists())

    def test_logout(self):
        self.client.login(username='temporary', password='temporary')
        self.client.get('/logout/')
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)