
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CandidateListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    CANDIDATES_TAB = (
        By.XPATH,
        "//a[normalize-space()='Candidates']"
    )

    CANDIDATE_ROWS = (
        By.CSS_SELECTOR,
        ".oxd-table-body .oxd-table-row"
    )

    def open_candidate_list(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CANDIDATES_TAB)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.CANDIDATE_ROWS)
        )

    def get_candidate_records(self):
        rows = self.driver.find_elements(*self.CANDIDATE_ROWS)

        records = []

        for row in rows:
            records.append(row.text)

        return records

    def candidate_exists(self, candidate_name):
        records = self.get_candidate_records()

        return any(
            candidate_name in record
            for record in records
        )

    def get_record_count(self):
        return len(
            self.driver.find_elements(*self.CANDIDATE_ROWS)
        )

    
    def is_candidate_present(self, first_name, last_name):
        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".oxd-table-body .oxd-table-row"
        )

        for row in rows:
            if first_name in row.text and last_name in row.text:
                return True

        return False
