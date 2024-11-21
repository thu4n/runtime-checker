from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_WAIT_TIME = 30

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

def email_login(driver):
    wait = WebDriverWait(driver, MAX_WAIT_TIME)

    gmail = "vy@gmail.com"
    password = "12345678"
    # gmail, password = account

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
    gmail_input.send_keys(gmail)

    password_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, password_selector)))
    password_input.clear()
    password_input.send_keys(password)

    confirm_signin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, confirm_signin_selector)))
    confirm_signin_button.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, avatar_selector)))


def run_prototype(driver, prototype_url):
    wait = WebDriverWait(driver, MAX_WAIT_TIME)
    
    run_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-\[500px\].flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(2) > button:nth-child(1)"
    status_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-\[500px\].flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(2) > div.px-2.py-1.flex.items-center"
    expand_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-16.flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(4) > button"

    driver.get(prototype_url)

    expand_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, expand_selector)))
    expand_button.click()

    # wait for status  0 --> 1
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, status_selector), "1"))

    run_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, run_selector)))
    run_button.click()

def process(prototype_url):
    prototype, url = prototype_url

    # Tùy chọn cho Selenium
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)

    # Đăng nhập
    # sso(driver)
    email_login(driver)

    # Chạy
    run_prototype(driver, url)

    input("Nhấn Enter để tắt {}".format(prototype))
    driver.quit()

def main():
    prototype_map = {
        # "get-current-value": "6729e349df948800271de230",
        # "get-target-value": "6729e527df948800271de469",
        # "set-current-value": "6729e553df948800271de51c",
        "set-target-value": "6729e583df948800271de576",
        "subscribe-current-value": "6729e5bbdf948800271de5c2",
        "subscribe-target-value": "6729e5d8df948800271de614",
        "auto-blink-basic": "6729e62ddf948800271de6f2",
        # "auto-blink-advanced": "6729e655df948800271de74a",
        # "smart-wipers-basic": "6729e688df948800271de7b6",
        # "smart-wipers-medium": "6729e69adf948800271de7fa",
        # "smart-wipers-advanced": "6729e6acdf948800271de835",
        
        # "2_get-current-value": "6729e349df948800271de230",
        # "2_get-target-value": "6729e527df948800271de469",
        # "2_set-current-value": "6729e553df948800271de51c",
        # "2_set-target-value": "6729e583df948800271de576",
        # "2_subscribe-current-value": "6729e5bbdf948800271de5c2",
        # "2_subscribe-target-value": "6729e5d8df948800271de614",
        # "2_auto-blink-basic": "6729e62ddf948800271de6f2",
        # "2_auto-blink-advanced": "6729e655df948800271de74a",
        # "2_smart-wipers-basic": "6729e688df948800271de7b6",
        # "2_smart-wipers-medium": "6729e69adf948800271de7fa",
        # "2_smart-wipers-advanced": "6729e6acdf948800271de835",

        # "3_get-current-value": "6729e349df948800271de230",
        # "3_get-target-value": "6729e527df948800271de469",
        # "3_set-current-value": "6729e553df948800271de51c",
        # "3_set-target-value": "6729e583df948800271de576",
        # "3_subscribe-current-value": "6729e5bbdf948800271de5c2",
        # "3_subscribe-target-value": "6729e5d8df948800271de614",
        # "3_auto-blink-basic": "6729e62ddf948800271de6f2",
        # "3_auto-blink-advanced": "6729e655df948800271de74a",
        # "3_smart-wipers-basic": "6729e688df948800271de7b6",
        # "3_smart-wipers-medium": "6729e69adf948800271de7fa",
        # "3_smart-wipers-advanced": "6729e6acdf948800271de835",

        # "4_get-current-value": "6729e349df948800271de230",
        # "4_get-target-value": "6729e527df948800271de469",
        # "4_set-current-value": "6729e553df948800271de51c",
        # "4_set-target-value": "6729e583df948800271de576",
        # "4_subscribe-current-value": "6729e5bbdf948800271de5c2",
        # "4_subscribe-target-value": "6729e5d8df948800271de614",
        # "4_auto-blink-basic": "6729e62ddf948800271de6f2",
        # "4_auto-blink-advanced": "6729e655df948800271de74a",
        # "4_smart-wipers-basic": "6729e688df948800271de7b6",
        # "4_smart-wipers-medium": "6729e69adf948800271de7fa",
        # "4_smart-wipers-advanced": "6729e6acdf948800271de835",
    }

    prototype_template = "https://autowrx.digital.auto/model/6729e29627616b0027b1dd3f/library/prototype/{}/dashboard"

    prototype_urls = {
        key: prototype_template.format(value) for key, value in prototype_map.items()
    }

    with ThreadPoolExecutor(max_workers=len(prototype_map)) as executor:
        executor.map(process, prototype_urls.items())

main()

