from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfum"""
        email = 'test@franckalain.com'
        password= 'manager$2021'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for the new user is normalized"""
        email = 'test@FRANCKALAIN.COM'
        user = get_user_model().objects.create_user(email, 'manager$2021')
        
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'manager$2021')
    
    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@franckalain.com',
            'manager$2021'
        )
        """superuser is part of PermissionsMixin"""
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
