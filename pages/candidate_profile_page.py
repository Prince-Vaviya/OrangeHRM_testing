
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CandidateProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")

    EMAIL = (
        By.XPATH,
        "//label[normalize-space()='Email']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    def get_candidate_name(self):

        first = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).get_attribute("value")

        middle = self.driver.find_element(
            *self.MIDDLE_NAME
        ).get_attribute("value")

        last = self.driver.find_element(
            *self.LAST_NAME
        ).get_attribute("value")

        return f"{first} {middle} {last}".strip()

    def get_candidate_email(self):

        return self.driver.find_element(
            *self.EMAIL
        ).get_attribute("value")
