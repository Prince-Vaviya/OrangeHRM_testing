def test_google_title(driver):

    driver.get("https://www.google.com")

    assert driver.title == "Google"