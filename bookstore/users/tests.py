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
# Create your tests here.
