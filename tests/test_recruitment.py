from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage


def test_navigate_to_recruitment(driver):

    login = LoginPage(driver)
    recruitment = RecruitmentPage(driver)

    login.open()
    login.login()

    recruitment.open_recruitment()

    assert recruitment.is_candidates_page_displayed()