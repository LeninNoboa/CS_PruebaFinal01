from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.artefacta.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search-list")
search_box.send_keys("Audi A4")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#openSearch > div > div > div.search-ots.false > img")
search_button.click()


