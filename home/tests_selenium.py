# school/tests_selenium.py
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class UserLoginSeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Utilise ChromeDriver pour contrôler le navigateur
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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

        # Trouver le champ de nom d'utilisateur en utilisant le sélecteur CSS input[type="text"]
        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        username_input.send_keys('UserTest')

        # Trouver le champ de mot de passe et entrer le mot de passe
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys('RootRoot8!')
        password_input.send_keys(Keys.RETURN)  # Appuyer sur Entrée pour soumettre le formulaire

        # Vérifier la présence de "Account" dans la navbar après la connexion
        #navbar_account_link = self.driver.find_element(By.LINK_TEXT, 'Account')
        #self.assertIsNotNone(navbar_account_link)
