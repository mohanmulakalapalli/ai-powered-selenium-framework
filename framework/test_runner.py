from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from test_cases import test_login_failed, test_login_positive, test_login_negative, test_timeout_page
from framework import ai_report, email_sender, logger, history_tracker, dashboard_generator
from datetime import datetime
import os

def run_tests():
    # Setup headless Chrome with Selenium Manager (built-in)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Use Selenium's built-in manager (Selenium 4.6+)
    driver = webdriver.Chrome(options=options)

    results = []
    screenshot_dir = "selenium_ai_framework/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Test Case 1: Login Positive
    try:
        res = test_login_positive.test_login_positive(driver)
        results.append(("Login Positive", res))
        if res != "success":
            logger.log_error("Login Positive failed")
            driver.save_screenshot(f"{screenshot_dir}/failure_Login_Positive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        else:
            logger.log_info("Login Positive passed")
    except Exception as e:
        results.append(("Login Positive", f"error: {e}"))
        logger.log_error(f"Login Positive exception: {e}")
        driver.save_screenshot(f"{screenshot_dir}/error_Login_Positive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

    # Test Case 2: Login Negative
    try:
        res = test_login_negative.test_login_negative(driver)
        results.append(("Login Negative", res))
        if res != "success":
            logger.log_error("Login Negative failed")
            driver.save_screenshot(f"{screenshot_dir}/failure_Login_Negative_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        else:
            logger.log_info("Login Negative passed")
    except Exception as e:
        results.append(("Login Negative", f"error: {e}"))
        logger.log_error(f"Login Negative exception: {e}")
        driver.save_screenshot(f"{screenshot_dir}/error_Login_Negative_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

    # Test Case 3: Page Timeout
    try:
        res = test_timeout_page.test_timeout_page(driver)
        results.append(("Page Timeout", res))
        if res != "success":
            logger.log_error("Page Timeout failed")
            driver.save_screenshot(f"{screenshot_dir}/failure_Timeout_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        else:
            logger.log_info("Page Timeout passed")
    except Exception as e:
        results.append(("Page Timeout", f"error: {e}"))
        logger.log_error(f"Page Timeout exception: {e}")
        driver.save_screenshot(f"{screenshot_dir}/error_Timeout_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

# Test Case 4 : Login Failure
    try:
        res = test_login_failed.test_login_failed(driver)
        results.append(("Login Failed", res))
        if res != "success":
            logger.log_error("Login Failed failed")
            driver.save_screenshot(f"{screenshot_dir}/failure_Login_Failed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        else:
            logger.log_info("Login Failed passed")
    except Exception as e:
        results.append(("Login Failed", f"error: {e}"))
        logger.log_error(f"Login Failed exception: {e}")
        driver.save_screenshot(f"{screenshot_dir}/error_Login_Failed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

    driver.quit()

    # Summary
    pass_count = sum(1 for _, r in results if r == "success")
    fail_count = len(results) - pass_count

    # Generate report
    html_report_path = ai_report.generate_report(results)

    # Save history
    history_tracker.append_history(pass_count, fail_count, html_report_path)

    # Generate dashboard
    dashboard_generator.generate_dashboard()

    # Send email
    email_sender.send_email_with_report(html_report_path, pass_count, fail_count)

if __name__ == "__main__":
    run_tests()