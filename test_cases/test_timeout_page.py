from selenium.common.exceptions import TimeoutException

def test_timeout_page(driver):
    try:
        driver.set_page_load_timeout(3)
        driver.get("https://httpstat.us/200?sleep=5000")
        return "fail"
    except TimeoutException:
        return "success"
