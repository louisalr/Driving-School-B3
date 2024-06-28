from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from .models import Customer
import time

class AddSchoolIntegrationSeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        cls.driver.implicitly_wait(10)  # Temps d'attente pour trouver les éléments

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        # Créer un utilisateur de test
        self.user = Customer.objects.create(
        username='manager',  # Nom d'utilisateur
        password = 'Rootroot8!',
        first_name='John',   # Prénom
        last_name='Doe',     # Nom de famille
        email='manager@example.com',  # Email
        isManager=True  # Définir isManager à True
    )

    def test_login(self):
        self.driver.get(f'{self.live_server_url}/login/')

        # Vérification des éléments dans le header
        navbar = self.driver.find_element(By.CLASS_NAME, 'navbar')
        self.assertIsNotNone(navbar)
        navbar_brand = self.driver.find_element(By.CLASS_NAME, 'navbar-brand')
        self.assertIsNotNone(navbar_brand)
        login_button = self.driver.find_element(By.LINK_TEXT, 'Login')
        self.assertIsNotNone(login_button)

        username_input = self.driver.find_element(By.ID, 'id_username')
        username_input.send_keys('manager')

        password_input = self.driver.find_element(By.ID, 'id_password')
        password_input.send_keys('RootRoot8!')

        # Simuler un clic sur le bouton "Login"
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()