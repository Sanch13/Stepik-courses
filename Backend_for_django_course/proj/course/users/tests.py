from django.test import TestCase

from .models import User
from .forms import UserRegistrationForm, LoginForm


class UserRegistrationFormTest(TestCase):

    def test_valid_registration_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'testname',
            'last_name': 'teslasttanme',
            'email': 'john.doe@example.com',
            'age': 25,
            'birth_date': '1996-01-01'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())


class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='John',
            last_name='Doe',
            email='email@example.com',
            age=25,
            birth_date='1996-01-01'
        )

    def test_user_creation(self):
        user = User.objects.filter(username="testuser").first()
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "email@example.com")
        self.assertEqual(user.age, 25)
        self.assertEqual(str(user.birth_date), '1996-01-01')

    def tearDown(self):
        User.objects.filter(username="testuser").delete()
