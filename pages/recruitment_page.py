from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecruitmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    RECRUITMENT_MENU = (
        By.XPATH,
        "//span[text()='Recruitment']"
    )

    CANDIDATES_HEADER = (
        By.XPATH,
        "//h5[text()='Candidates']"
    )

    def open_recruitment(self):

        self.wait.until(
            EC.element_to_be_clickable(self.RECRUITMENT_MENU)
        ).click()

    def is_candidates_page_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.CANDIDATES_HEADER)
        ).is_displayed()