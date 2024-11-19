from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor

WAIT_TIME = 10

def sso(driver):
    home_url = "https://autowrx.digital.auto/"
    signin_selector = "#root > div.flex.h-screen.flex-col > header > div:nth-child(3) > button"
    SSO_selector = "body > div.MuiModal-root.css-8ndowl > div.da-popup-inner.relative > form > div:nth-child(3) > div > button"

    driver.get(home_url)
    time.sleep(WAIT_TIME)

    signin_button = driver.find_element(By.CSS_SELECTOR, signin_selector)
    signin_button.click()
    time.sleep(WAIT_TIME)

    SSO_button = driver.find_element(By.CSS_SELECTOR, SSO_selector)
    SSO_button.click()
    time.sleep(WAIT_TIME)

def run_prototype(driver, prototype_url):
    # driver.execute_script(f"window.open('{prototype_url}', '_blank');")
    driver.get(prototype_url)
    time.sleep(WAIT_TIME)

    expand_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-16.flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(4) > button"
    expand_button = driver.find_element(By.CSS_SELECTOR, expand_selector)
    print(expand_button)
    expand_button.click()
    time.sleep(WAIT_TIME)

    run_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-\[500px\].flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(2) > button:nth-child(1)"
    run_button = driver.find_element(By.CSS_SELECTOR, run_selector)
    run_button.click()

def process(prototype_url):
    # Tùy chọn cho Selenium
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)

    # Đăng nhập
    sso(driver)

    # Chạy
    run_prototype(driver, prototype_url)

    input("Nhấn Enter để tắt browser")
    driver.quit()

def main():
    prototype_map = {
        "get-current-value": "6729e349df948800271de230",
        "get-target-value": "6729e527df948800271de469",
        "set-current-value": "6729e553df948800271de51c",
        "set-target-value": "6729e583df948800271de576",
        "subscribe-current-value": "6729e5bbdf948800271de5c2",
        "subscribe-target-value": "6729e5d8df948800271de614",
        "auto-blink-basic": "6729e62ddf948800271de6f2",
        "auto-blink-advanced": "6729e655df948800271de74a",
        "smart-wipers-basic": "6729e688df948800271de7b6",
        "smart-wipers-medium": "6729e69adf948800271de7fa",
        "smart-wipers-advanced": "6729e6acdf948800271de835",
    }

    prototype_template = "https://autowrx.digital.auto/model/6729e29627616b0027b1dd3f/library/prototype/{}/dashboard"
    
    prototype_urls = [
        prototype_template.format(prototype_map["get-current-value"]),
        prototype_template.format(prototype_map["get-target-value"]),
        prototype_template.format(prototype_map["set-current-value"]),
        prototype_template.format(prototype_map["set-target-value"]),
        prototype_template.format(prototype_map["subscribe-current-value"]),
        prototype_template.format(prototype_map["subscribe-target-value"]),
        prototype_template.format(prototype_map["auto-blink-basic"]),
        prototype_template.format(prototype_map["auto-blink-advanced"]),
        prototype_template.format(prototype_map["smart-wipers-basic"]),
        prototype_template.format(prototype_map["smart-wipers-medium"]),
        prototype_template.format(prototype_map["smart-wipers-advanced"]),
    ]

    with ThreadPoolExecutor(max_workers=len(prototype_urls)) as executor:
        executor.map(process, prototype_urls)

main()

