from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username='nixa',
            email='nixa@gmail.com',
            password='sanix1234'
        )
        self.assertEqual(user.username, 'nixa')
        self.assertEqual(user.email, 'nixa@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username='sanix',
            email='sanix@gmail.com',
            password='sanix2324'
        )
        self.assertEqual(admin_user.username,'sanix')
        self.assertEqual(admin_user.email, 'sanix@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    class SignupPageTests(TestCase): # new
        def setUp(self):
            url = reverse('signup')
            self.response = self.client.get(url)

        def test_signup_template(self):
            self.assertEqual(self.response.status_code, 200)
            self.assertTemplateUsed(self.response, 'signup.html')
            self.assertContains(self.response, 'Sign Up')
            self.assertNotContains(
                self.response, 'Hi there! I should not be on the page.')

        def test_signup_form(self): # new
            form = self.response.context.get('form')
            self.assertIsInstance(form, CustomUserCreationForm)
            self.assertContains(self.response, 'csrfmiddlewaretoken')

        def test_signup_view(self): # new
            view = resolve('/accounts/signup/')
            self.assertEqual(
                view.func.__name__,
                SignupPageView.as_view().__name__
            )

class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)            

# Create your tests here.
