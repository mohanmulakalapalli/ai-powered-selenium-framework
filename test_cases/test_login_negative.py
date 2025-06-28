from keywords.login_keywords import perform_login

def test_login_negative(driver):
    perform_login(driver, "wronguser", "wrongpass")
    return "success" if "Your username is invalid!" in driver.page_source else "fail"
