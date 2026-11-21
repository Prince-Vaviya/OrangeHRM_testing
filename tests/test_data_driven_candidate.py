
import pytest

from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.add_candidate_page import AddCandidatePage


@pytest.mark.parametrize(
    "first_name, last_name",
    [
        ("", "Smith"),
        ("John", ""),
        ("", ""),
    ],
)
def test_candidate_required_fields(driver, first_name, last_name):

    login = LoginPage(driver)
    recruitment = RecruitmentPage(driver)
    candidate = AddCandidatePage(driver)

    login.open()
    login.login()

    recruitment.open_recruitment()
    candidate.open_add_candidate()

    candidate.enter_candidate_details(
        first_name, "Michael", last_name
    )

    candidate.enter_email("test@example.com")
    candidate.save_candidate()

    errors = candidate.get_validation_errors()

    print("Validation errors:", errors)

    assert len(errors) >= 1
    assert "Required" in errors
