from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(LiveServerTestCase):

    def setUp(self):
        # Setup the Chrome WebDriver with the correct path using webdriver-manager
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.implicitly_wait(3)

        # Setup a test user
        self.username = 'testuser'
        self.password = 'testpassword'
        User.objects.create_user(username=self.username, password=self.password)

    def tearDown(self):
        # Close the browser after each test
        self.browser.quit()

    def test_can_login_with_valid_credentials(self):
        # Navigate to the login page
        self.browser.get(self.live_server_url + '/login/')

        # Find the username and password input elements and fill them
        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)

        # Check that the user is redirected to the home page or their profile page
        self.assertIn('Home', self.browser.title)  # Or change this to match your actual home page title
        # Alternatively, check for a specific element that is present only on the home page:
        # self.assertTrue(self.browser.find_element(By.ID, 'home_welcome_message'))

    def test_cannot_login_with_invalid_credentials(self):
        # Navigate to the login page
        self.browser.get(self.live_server_url + '/login/')

        # Fill in the username and a wrong password
        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')
        username_input.send_keys(self.username)
        password_input.send_keys('wrongpassword')
        password_input.send_keys(Keys.ENTER)

        # Check that an error message is displayed
        error_message = self.browser.find_element(By.CLASS_NAME, 'errorlist')  # Adjust to match your actual class name
        self.assertIn('Please enter a correct username and password.', error_message.text)
