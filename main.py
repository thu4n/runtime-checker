from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor

def sso(driver):
    home_url = "https://autowrx.digital.auto/"
    signin_selector = "#root > div.flex.h-screen.flex-col > header > div:nth-child(3) > button"
    SSO_selector = "body > div.MuiModal-root.css-8ndowl > div.da-popup-inner.relative > form > div:nth-child(3) > div > button"

    driver.get(home_url)
    time.sleep(5)

    signin_button = driver.find_element(By.CSS_SELECTOR, signin_selector)
    signin_button.click()
    time.sleep(2)

    SSO_button = driver.find_element(By.CSS_SELECTOR, SSO_selector)
    SSO_button.click()
    time.sleep(10)

def run_prototype(driver):
    prototype_url = "https://autowrx.digital.auto/model/6729e29627616b0027b1dd3f/library/prototype/6729e62ddf948800271de6f2/dashboard"
    driver.execute_script(f"window.open('{prototype_url}', '_blank');")
    time.sleep(10)

    expand_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-16.flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(4) > button"
    expand_button = driver.find_element(By.CSS_SELECTOR, expand_selector)
    print(expand_button)
    expand_button.click()
    time.sleep(10)

    run_selector = "#root > div.flex.h-screen.flex-col > div.h-full.overflow-y-auto > div > div.flex.flex-col.h-full.overflow-y-auto > div > div > div.absolute.bottom-0.right-0.top-0.z-10.w-\[500px\].flex.flex-col.justify-center.bg-da-gray-darkest.px-1.py-2.text-da-gray-light > div:nth-child(2) > button:nth-child(1)"
    run_button = driver.find_element(By.CSS_SELECTOR, run_selector)
    run_button.click()

def process():
    # Tùy chọn cho Selenium
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)

    # Đăng nhập
    sso(driver)

    # Chạy
    run_prototype(driver)

    input("Nhấn Enter để tắt browser")
    driver.quit()

def main():
    # NUM_TABS = 3
    # with ThreadPoolExecutor(max_workers=NUM_TABS) as executor:
    #     executor.map(process, range(1, NUM_TABS + 1))

    process()

main()

