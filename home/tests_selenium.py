from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class UserLoginSeleniumTests(StaticLiveServerTestCase):

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
        self.user = get_user_model().objects.create_user(
            username='UserTest',
            password='RootRoot8!',
            email='usertest@example.com'
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

        # Vérification des éléments dans le formulaire de login
        username_input = self.driver.find_element(By.ID, 'id_username')
        self.assertIsNotNone(username_input)
        password_input = self.driver.find_element(By.ID, 'id_password')
        self.assertIsNotNone(password_input)
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        self.assertIsNotNone(submit_button)

        # Vérification des éléments dans le footer
        footer = self.driver.find_element(By.TAG_NAME, 'footer')
        self.assertIsNotNone(footer)
        footer_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'© 2023 Driving School')]")
        self.assertIsNotNone(footer_text)
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, 'footer .nav-link')
        self.assertGreaterEqual(len(nav_links), 4)
