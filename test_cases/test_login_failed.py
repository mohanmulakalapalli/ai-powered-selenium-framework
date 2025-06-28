from keywords.login_keywords import perform_login

def test_login_failed(driver):
    perform_login(driver, "student", "WrongPassword")
    return "success" if "Login Failed" in driver.page_source else "fail"