from django.test import TestCase, Client
from django.urls import reverse
from home.forms import RegistrationForm, LoginForm, SchoolForm, EventForm
from home.models import School, Customer, Event


class LoginRequestTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home:login')
        self.user = Customer.objects.create_user(username='testuser', password='password')

    def test_login_request_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_request_post_valid(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:index'))

    def test_login_request_post_invalid(self):
        response = self.client.post(self.url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        messages_list = list(response.context['messages'])
        self.assertEqual(str(messages_list[0]), "Invalid username or password.")
