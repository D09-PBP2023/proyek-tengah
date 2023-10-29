from django.test import Client, TestCase
from django.contrib import auth
from django.contrib.auth import get_user_model

from user_profile.models import UserProfile

# Create your tests here.
class BookDetailTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.client = Client()
    
    def test_book_details_url_is_exist(self):
        response = self.client.get('/book_details/1/')
        self.assertEqual(response.status_code, 200)

    def test_book_details_using_correct_template(self):
        response = self.client.get('/book_details/2/')
        self.assertTemplateUsed(response, 'book_details.html')

    def test_bookmarked_url_when_not_signed_in(self):
        response = self.client.get('/bookmarked/')
        self.assertEqual(response.status_code, 302)

    def test_bookmarked_url_when_signed_in(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/bookmarked/')
        self.assertNotEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'bookmarked_list.html')

    def test_bookmark_when_not_signed_in(self):
        response = self.client.get('/bookmark_book/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/bookmark_book/1/')

    def test_bookmark_when_signed_in(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/bookmark_book/1/')
        self.assertNotEqual(response.status_code, 404)
        self.assertRedirects(response, '/book_details/1/')

    def test_nonexisting_bookmark_when_signed_in(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/bookmark_book/-15/')
        self.assertEqual(response.status_code, 404)
    
    def test_unbookmark_when_signed_in(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/bookmark_book/1/')
        self.assertNotEqual(response.status_code, 404)
        self.assertRedirects(response, '/book_details/1/')
        user_profile = UserProfile.objects.get(user=auth.get_user(self.client))
        self.assertEqual(user_profile.bookmarkedbooks.count(), 1)

        response = self.client.get('/bookmark_book/1/')
        self.assertNotEqual(response.status_code, 404)
        self.assertRedirects(response, '/book_details/1/')
        user_profile = UserProfile.objects.get(user=auth.get_user(self.client))
        self.assertEqual(user_profile.bookmarkedbooks.count(), 0)

    def test_get_bookmarked_list_when_not_signed_in(self):
        response = self.client.get('/get_marked_books/')
        self.assertEqual(response.status_code, 302)

    def test_get_bookmarked_list_when_signed_in(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/get_marked_books/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), [])

    def test_get_filled_bookmarked_list_when_signed_in(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.post('/bookmark_book/1/')
        response = self.client.get('/get_marked_books/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONNotEqual(str(response.content, encoding='utf8'), [])