from selenium import webdriver
from dotenv import load_dotenv
from actions import email_login, check_runtime, send_email
import time
import os

if __name__ == "__main__":
    # Run `docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome` beforehand.
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
            )
    driver.maximize_window()
    url = 'https://autowrx.digital.auto/model/6729e29627616b0027b1dd3f/library/prototype/6729e349df948800271de230/dashboard'

    load_dotenv()
    autowrx_email = os.getenv('AUTOWRX_EMAIL')
    autowrx_password = os.getenv('AUTOWRX_PASSWORD')
    email_login(driver, autowrx_email, autowrx_password)

    time.sleep(1)
    python_runtime_available, rust_compiler_available, report_msg  = check_runtime(driver, url)
    print(report_msg)
    if python_runtime_available is False or rust_compiler_available is False:
            
        from_email = os.getenv("REPORT_EMAIL")
        from_password = os.getenv("REPORT_PASSWORD")
        subject = "[digital.auto] - Status Report: Runtimes are not available on the website"
        body = report_msg
        to_email = os.getenv("TO_EMAIL")
        send_email(from_email, from_password, subject, body, to_email)

    driver.close()
    driver.quit()