
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.add_candidate_page import AddCandidatePage
from pages.candidate_list_page import CandidateListPage


def test_add_candidate_end_to_end(driver):

    # 1. Login
    login = LoginPage(driver)
    login.open()
    login.login()

    # 2. Navigate to Recruitment
    recruitment = RecruitmentPage(driver)
    recruitment.open_recruitment()

    # 3. Open Add Candidate
    candidate = AddCandidatePage(driver)
    candidate.open_add_candidate()

    # 4. Enter unique candidate details
    first_name = "E2E"
    last_name = "TestCandidate"
    email = "e2e.testcandidate@example.com"

    candidate.enter_candidate_details(
        first_name, "Automation", last_name
    )
    candidate.enter_email(email)

    # 5. Save and verify success
    candidate.save_candidate()

    assert candidate.is_success_message_displayed(), \
        "Candidate creation failed!"

    # 6. Navigate to Candidate List
    candidate_list = CandidateListPage(driver)
    candidate_list.open_candidate_list()

    # 7. Verify candidate exists
    assert candidate_list.is_candidate_present(
        first_name, last_name
    ), "New candidate not found in candidate list!"
