import pytest

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():

    options = Options()
    options.add_argument("--start-maximized")

    service = Service("./driver/msedgedriver")

    browser = webdriver.Edge(
        service=service,
        options=options
    )

    yield browser

    browser.quit()
