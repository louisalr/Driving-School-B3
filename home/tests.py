from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import School, Customer

class SchoolModelTest(TestCase):

    def setUp(self):
        # Configuration initiale pour chaque test
        self.school = School.objects.create(
            name="Test School",
            address="123 Test St",
            phone="1234567890",
            description="This is a test school.",
            picture_url="http://example.com/picture.jpg"
        )

    def test_school_creation(self):
        # Vérifie que l'école a été créée correctement
        school = School.objects.get(id=self.school.id)
        self.assertEqual(school.name, "Test School")
        self.assertEqual(school.address, "123 Test St")
        self.assertEqual(school.phone, "1234567890")
        self.assertEqual(school.description, "This is a test school.")
        self.assertEqual(school.picture_url, "http://example.com/picture.jpg")

    def test_str_method(self):
        # Vérifie que la méthode __str__ renvoie le bon nom
        school = School.objects.get(id=self.school.id)
        self.assertEqual(str(school), "Test School")


class CustomerModelTest(TestCase):

    def setUp(self):
        self.school = School.objects.create(
            name="Test School",
            address="123 Test St",
            phone="1234567890",
            description="This is a test school.",
            picture_url="http://example.com/picture.jpg"
        )
        self.customer = get_user_model().objects.create_user(
            username="TestUser",
            first_name="Jane",
            last_name="Smith",
            password="password123",
            isManager=True
        )
        self.customer.school.add(self.school)

    def test_customer_creation(self):
        customer = Customer.objects.get(id=self.customer.id)
        self.assertEqual(customer.first_name, "Jane")
        self.assertEqual(customer.last_name, "Smith")
        self.assertEqual(customer.username, "JaneSmith")
        self.assertTrue(customer.isManager)
        self.assertIn(self.school, customer.school.all())

    def test_superuser_username(self):
        superuser = get_user_model().objects.create_superuser(
            username="TestAdmin",
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            password="adminpassword"
        )
        superuser.save()
        self.assertTrue(superuser.username, "TestAdmin")

    def test_str_method(self):
        customer = Customer.objects.get(id=self.customer.id)
        self.assertEqual(str(customer.username), "JaneSmith")