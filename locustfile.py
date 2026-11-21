
from locust import HttpUser, task, between


class OrangeHRMUser(HttpUser):

    wait_time = between(2, 5)

    @task(3)
    def visit_login(self):
        self.client.get(
            "/web/index.php/auth/login",
            name="Login Page"
        )

    @task(2)
    def visit_recruitment(self):
        self.client.get(
            "/web/index.php/recruitment/viewCandidates",
            name="Recruitment Page"
        )

    @task(1)
    def visit_dashboard(self):
        self.client.get(
            "/web/index.php/dashboard/index",
            name="Dashboard Page"
        )
