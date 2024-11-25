from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


MAX_WAIT_TIME = 30

class NoRuntimeAvailableException(Exception):
    pass

def sso(driver):
    wait = WebDriverWait(driver, MAX_WAIT_TIME)

    home_url = "https://autowrx.digital.auto/"
    signin_selector = "#root > div.flex.h-screen.flex-col > header > div:nth-child(3) > button"
    SSO_selector = "body > div.MuiModal-root.css-8ndowl > div.da-popup-inner.relative > form > div:nth-child(3) > div > button"
    avatar_selector = "#root > div.flex.h-screen.flex-col > header > div:nth-child(4) > div > div > span > button"

    driver.get(home_url)

    signin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, signin_selector)))
    signin_button.click()

    SSO_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SSO_selector)))
    SSO_button.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, avatar_selector)))

def email_login(driver, email, password):
    wait = WebDriverWait(driver, MAX_WAIT_TIME)

    home_url = "https://autowrx.digital.auto/"
    signin_selector = "#root > div.flex.h-screen.flex-col > header > div:nth-child(3) > button"
    gmail_selector = "body > div.MuiModal-root.css-8ndowl > div.da-popup-inner.relative > form > div.flex.flex-col > div:nth-child(3) > div > input"
    password_selector = "body > div.MuiModal-root.css-8ndowl > div.da-popup-inner.relative > form > div.flex.flex-col > div:nth-child(4) > div > input"
    avatar_selector = "#root > div.flex.h-screen.flex-col > header > div:nth-child(4) > div > div > span > button"
    confirm_signin_selector = "body > div.MuiModal-root.css-8ndowl > div.da-popup-inner.relative > form > div.flex.flex-col > button"

    driver.get(home_url)

    signin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, signin_selector)))
    signin_button.click()

    gmail_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, gmail_selector)))
    gmail_input.clear()
    gmail_input.send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, password_selector)))
    password_input.clear()
    password_input.send_keys(password)

    confirm_signin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, confirm_signin_selector)))
    confirm_signin_button.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, avatar_selector)))


def check_runtime(driver, prototype_url):
    wait = WebDriverWait(driver, MAX_WAIT_TIME)
    python_runtime_available = True
    rust_compiler_available = True
    report_msg = ""
    
    #run_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-\[500px\].flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(2) > button:nth-child(1)"
    status_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-\[500px\].flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(2) > div.px-2.py-1.flex.items-center"
    expand_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-16.flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(4) > button"

    driver.get(prototype_url)

    expand_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, expand_selector)))
    expand_button.click()
    try:
        time.sleep(2)
        static_dropdown = Select(driver.find_element(By.XPATH, "//select[contains(@class, 'border')]"))
        options = [option.get_attribute("value") for option in static_dropdown.options]
        if len(options) == 0:
            python_runtime_available = False
            report_msg += "\n - Python Runtime: NOT Available\n"
            raise NoRuntimeAvailableException("No runtime available.")
        else:
            report_msg += f"\n - Python Runtime: {len(options)} Available\n"
            print(f"Success. Python Runtime: {len(options)} Available.")
        print("Waiting for Rust compiler status to turn into 1...")
        wait = WebDriverWait(driver, 10)
        # wait for status  0 --> 1
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, status_selector), "1"))
        report_msg += f"\n - Rust Compiler: Is Available\n"
    except TimeoutException:
        print("Failure. The status did not turn to 1 within 10 seconds.")
        rust_compiler_available = False
        report_msg += f"\n - Rust Compiler: NOT Available (Timed out)\n"
    except NoRuntimeAvailableException:
        print("Failure. No runtime available.")

    return python_runtime_available, rust_compiler_available, report_msg

def send_email(from_email, from_password, subject, body, to_email):

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

