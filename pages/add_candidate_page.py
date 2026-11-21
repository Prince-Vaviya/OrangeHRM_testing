
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCandidatePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    ADD_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Add']"
    )

    FIRST_NAME = (
        By.NAME,
        "firstName"
    )

    MIDDLE_NAME = (
        By.NAME,
        "middleName"
    )

    LAST_NAME = (
        By.NAME,
        "lastName"
    )

    EMAIL = (
        By.XPATH,
        "//label[text()='Email']/../following-sibling::div//input"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Save']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Successfully Saved')]"
    )

    def open_add_candidate(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        ).click()

    def enter_candidate_details(self, first, middle, last):

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first)

        self.driver.find_element(
            *self.MIDDLE_NAME
        ).send_keys(middle)

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last)

    def enter_email(self, email):

        self.driver.find_element(
            *self.EMAIL
        ).send_keys(email)

    def save_candidate(self):

        self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        ).click()

    def is_success_message_displayed(self):

        toast_message = (
            By.CSS_SELECTOR,
            ".oxd-toast--success .oxd-text--toast-message"
        )

        message = self.wait.until(
            EC.visibility_of_element_located(toast_message)
        )

        print("Success notification:", message.text)

        return message.text.strip() == "Successfully Saved"

    
    def get_validation_errors(self):
        locator = (
            By.CSS_SELECTOR,
            ".oxd-input-field-error-message"
        )

        self.wait.until(
            lambda driver: len(driver.find_elements(*locator)) > 0
        )

        errors = self.driver.find_elements(*locator)
        return [error.text for error in errors]
