from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def count_sel():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.selenium.dev/")
    count = len(driver.find_elements(By.XPATH, "//*[text()[contains(.,'Selenium')]]"))
    print(count)


count_sel()
