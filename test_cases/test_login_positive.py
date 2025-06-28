from keywords.login_keywords import perform_login

def test_login_positive(driver):
    perform_login(driver, "student", "Password123")
    return "success" if "Logged In Successfully" in driver.page_source else "fail"
