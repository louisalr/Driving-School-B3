from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import RegistrationForm

User = get_user_model()

class RegistrationFormTest(TestCase):

    def test_form_fields_widgets(self):
        """Test que les widgets des champs ont les bons attributs"""
        form = RegistrationForm()
        self.assertEqual(form.fields['email'].widget.attrs['class'], 'form-control mb-1')
        self.assertEqual(form.fields['first_name'].widget.attrs['class'], 'form-control mb-1')
        self.assertEqual(form.fields['last_name'].widget.attrs['class'], 'form-control mb-1')
        self.assertEqual(form.fields['password1'].widget.attrs['class'], 'form-control mb-1')
        self.assertEqual(form.fields['password2'].widget.attrs['class'], 'form-control mb-1')
        self.assertEqual(form.fields['isManager'].widget.attrs['class'], 'form-check-input')

    def test_form_invalid_email(self):
        """Test que le formulaire est invalide avec un email incorrect"""
        form = RegistrationForm(data={
            'email': 'invalid-email',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'password12345',
            'password2': 'password12345',
            'isManager': True
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_password_mismatch(self):
        """Test que le formulaire est invalide si les mots de passe ne correspondent pas"""
        form = RegistrationForm(data={
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'password12345',
            'password2': 'differentpassword',
            'isManager': True
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
