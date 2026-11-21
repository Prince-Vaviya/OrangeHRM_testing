from pages.candidate_profile_page import CandidateProfilePage
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.add_candidate_page import AddCandidatePage


def test_add_candidate(driver):

    login = LoginPage(driver)
    recruitment = RecruitmentPage(driver)
    candidate = AddCandidatePage(driver)

    # Login
    login.open()
    login.login()

    # Navigate to Recruitment
    recruitment.open_recruitment()

    # Open Add Candidate form
    candidate.open_add_candidate()

    # Enter candidate information
    candidate.enter_candidate_details(
        "John",
        "Michael",
        "Smith"
    )

    candidate.enter_email(
        "john.smith.test@example.com"
    )

    # Save
    candidate.save_candidate()

    # Verify
    assert candidate.is_success_message_displayed()

    profile = CandidateProfilePage(driver)

    assert profile.get_candidate_name() == "John Michael Smith"
    assert profile.get_candidate_email() == "john.smith.test@example.com"


def test_add_candidate_without_required_fields(driver):
    login = LoginPage(driver)
    recruitment = RecruitmentPage(driver)
    candidate = AddCandidatePage(driver)

    login.open()
    login.login()

    recruitment.open_recruitment()
    candidate.open_add_candidate()

    candidate.save_candidate()

    errors = candidate.get_validation_errors()

    print("Validation errors:", errors)

    assert len(errors) >= 1