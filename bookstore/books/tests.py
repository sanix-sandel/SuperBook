from django.test import Client, TestCase
from django.urls import reverse

from .models import Books

class BookTests(TestCase):
    def setup(self):
        self.book=Book.objects.create(
            title='Harry potter',
            author='Jk Rowling',
            price='23.1',

        )

    def test_book_listing(self):
        self.assertEqual(f'self.book.title', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_detail.html')
# Create your tests here.
