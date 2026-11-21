
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import BASE_URL, USERNAME, PASSWORD


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self):

        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        ).send_keys(USERNAME)

        self.driver.find_element(
            *self.PASSWORD_FIELD
        ).send_keys(PASSWORD)

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    def is_dashboard_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADER)
        ).is_displayed()
