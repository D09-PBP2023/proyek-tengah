from django.forms import ImageField
from django.test import Client, TestCase
from django.urls import reverse

from main.models import Book

class BookTestCase(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_assign_book(self):
        Book.objects.create(
            name = 'Harry Potter',
            author = 'Arvin',
            original_language = 'Indonesia',
            year_published = 1999,
            sales = 2,
            genre = 'Horror, Mystery',
            cover_image = None,
        )

        # Validate created book
        book = Book.objects.get(name = 'Harry Potter')
        self.assertEqual(book.author, 'Arvin')
        self.assertEqual(book.original_language, 'Indonesia')
        self.assertEqual(book.year_published, 1999)
        self.assertEqual(book.sales, 2)
        self.assertEqual(book.genre, 'Horror, Mystery')
        self.assertFalse(bool(book.cover_image))

    def test_preassigned_book(self):
        book = Book.objects.get(pk=1)
        self.assertEqual(book.name, 'A Tale of Two Cities')
        self.assertEqual(book.author, 'Charles Dickens')
        self.assertEqual(book.original_language, 'English')
        self.assertEqual(book.year_published, 1859)
        self.assertEqual(book.sales, 200)
        self.assertEqual(book.genre, 'Historical fiction')
        self.assertTrue(bool(book.cover_image))

        book = Book.objects.get(pk=100)
        self.assertEqual(book.name, 'Where the Wild Things Are')
        self.assertEqual(book.author, 'Maurice Sendak')
        self.assertEqual(book.original_language, 'English')
        self.assertEqual(book.year_published, 1963)
        self.assertEqual(book.sales, 20)
        self.assertEqual(book.genre, "Children's picture book")
        self.assertTrue(bool(book.cover_image))

    def test_get_books(self):
        response = self.client.get(
            "/get_books/",
        )
        self.assertEqual(response.status_code, 200)

    def test_mislead_get_books(self):
        response = self.client.get(
            "/get_books/2",
        )
        self.assertEqual(response.status_code, 404)

    def test_get_books_by_name(self):
        response = self.client.get(
            "/get_books_by_name/a",
        )
        self.assertEqual(response.status_code, 200)

        response = Client().get(reverse('main:get_books_by_name', kwargs={'name': 'a'}))
        self.assertTrue(len(response.json()) > 0)

        response = Client().get(reverse('main:get_books_by_name', kwargs={'name': 'abcdefgh$^#^#$)#$@)($!@)'}))
        self.assertTrue(len(response.json()) == 0)

    def test_mislead_get_books_by_name(self):
        response = self.client.get(
            "/get_books_by_name/",
        )
        self.assertEqual(response.status_code, 404)

        response = self.client.get(
            "/get_books_by_name/a/bc",
        )
        self.assertEqual(response.status_code, 404)