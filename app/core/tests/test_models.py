from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the normalization of a user's email"""
        email = 'teSt@ExAmPlE.CoM'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )

        self.assertEqual(
            user.email,
            '@'.join([
                s if ind == 0 else s.lower()
                for ind, s in enumerate(email.split('@'))
            ])
        )
        self.assertNotEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
