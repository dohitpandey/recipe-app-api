"""
Test for models
"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


class ModelTests(TestCase):
    """Test for models"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        sample_emails = [['Test1@Example.com', 'Test1@example.com'],
                         ['TEST2@EXAMPLE.COM', 'TEST2@example.com'],
                         ['test3@EXAMPLE.com', 'test3@example.com'],
                         ['test4@example.COM', 'test4@example.com']
                         ]

        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'test123')

            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email(self):
        """Test creating user without email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful"""
        user = get_user_model().objects.create_user(
            'test1@example.com',
            'test123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='sample recipe name',
            time_minutes=5,
            price=Decimal('10.50'),
            description='sample recipe description'
        )

        self.assertEqual(str(recipe), recipe.title)
