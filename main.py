from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

articulo = "lavadora"
driver = webdriver.Chrome()
driver.get("https://www.artefacta.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search")
search_box.send_keys(articulo)

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#search_mini_form > div.actions > button")
search_button.click()

articulo_cards = driver.find_elements(By.CSS_SELECTOR, "#maincontent > div.columns > div.column.main > div.search.results > div.products.wrapper.grid.products-grid > ol")


mongodb = MongoDriver()

for card in articulo_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "div > strong").text
        price = card.find_element(By.CSS_SELECTOR, "div > div.price-box.price-final_price > span.special-price").text
        print(title)
        print(f"${price}")


        #title = card.find_element(By.CSS_SELECTOR,"div > div > div > div.card-info.card-content > div.module.tittle").text
        #price = card.find_element(By.CSS_SELECTOR, "div > div > div > div.card-info.card-content > strong").text

        artic_actual = {
            "title": title,
            "price": price
        }

        mongodb.insert_record(record=artic_actual, username="LAVADORA")

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()