# Automated Software Testing of OrangeHRM Web Application

A comprehensive automated testing framework for the **OrangeHRM Open Source Demo** web application. This project demonstrates automated quality assurance practices covering **UI browser automation**, **data-driven validation**, **end-to-end (E2E) workflow testing**, and **baseline HTTP performance testing**.

---

## 1. Project Overview

The project validates the stability, functional accuracy, and response behavior of key HR workflows within the OrangeHRM platform—focusing primarily on authentication, administrative navigation, and candidate recruitment operations.

### Key Objectives
* **Functional & UI Validation:** Automate verification of page titles, login workflows, and navigation into the Recruitment module.
* **End-to-End Workflow Testing:** Validate the complete candidate management cycle from form submission to confirmation and listing.
* **Data-Driven & Boundary Validation:** Test field validations and mandatory inputs (e.g., missing first/last name combinations) using parameterized test cases.
* **Baseline Performance Testing:** Gauge HTTP response times and stability across key application endpoints (Login, Dashboard, Recruitment).
* **Test Reporting & Evidence:** Produce execution evidence via HTML reports and CSV performance logs.

---

## 2. Tools & Technologies

| Tool / Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language for automation scripts |
| **Selenium WebDriver** | Browser interaction and UI automation (tested on Microsoft Edge) |
| **pytest** | Test execution framework, assertions, and test organization |
| **pytest-html** | HTML report generation for functional test execution |
| **Locust** | Load generation and HTTP response performance testing |
| **uv** | Fast Python package and dependency management |

---

## 3. Test Suites & Coverage

### Functional Testing (10 Test Cases — 100% Pass)
* **TC01:** Verify browser title on load.
* **TC02:** Login with valid user credentials.
* **TC03:** Navigate to the Recruitment module.
* **TC04:** Add candidate with valid required details.
* **TC05:** Submit candidate form with empty required fields (validation check).
* **TC06:** Verify candidate directory records display.
* **TC07:** Form submission with missing first name.
* **TC08:** Form submission with missing last name.
* **TC09:** Form submission with both names missing.
* **TC10:** Complete candidate creation and verification workflow.

### Data-Driven Testing
Implemented using `pytest.mark.parametrize` to execute reusable validation scenarios against required fields across multiple inputs (empty first name, empty last name, both empty).

### End-to-End (E2E) Workflow
Automates the full recruitment pipeline:
1. Open OrangeHRM and authenticate.
2. Navigate to the **Recruitment** section.
3. Open the **Add Candidate** form.
4. Fill required candidate details and submit.
5. Verify success alert: `"Successfully Saved"`.
6. Navigate to the **Candidate List** and verify the created record appears.

### Performance Testing (Locust)
Simulates baseline HTTP traffic to measure response metrics across core endpoints:
* **Endpoints Tested:** Login (`/auth/login`), Dashboard, and Recruitment.
* **Baseline Results:** 0% failure rate with average response times under ~460 ms across recorded test runs.

---

## 4. Test Reporting & Evidence

Execution logs and reports are generated in the `reports/` directory:
* `reports/functional_test_report.html` — Detailed pytest HTML execution report.
* `reports/performance_report.html` — Locust load testing summary report.
* `reports/*.csv` — Locust endpoint response times, request stats, and history metrics.
* `OrangeHRM_Software_Testing_Report.pdf` — Complete consolidated testing report document.

