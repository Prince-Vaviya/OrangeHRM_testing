
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.candidate_list_page import CandidateListPage


def test_candidate_list(driver):
    login = LoginPage(driver)
    recruitment = RecruitmentPage(driver)
    candidate_list = CandidateListPage(driver)

    login.open()
    login.login()

    recruitment.open_recruitment()
    candidate_list.open_candidate_list()

    assert candidate_list.get_record_count() > 0

    assert candidate_list.candidate_exists(
        "John Michael Smith"
    )

    print("Total records:", candidate_list.get_record_count())
    print("Candidate found successfully!")
