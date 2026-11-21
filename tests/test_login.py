from pages.login_page import LoginPage


def test_orangehrm_login(driver):

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login()

    assert login_page.is_dashboard_displayed()