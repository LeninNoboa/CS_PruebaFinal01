from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

articulo = "licuadora"
driver = webdriver.Chrome()
driver.get("https://www.artefacta.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search")
search_box.send_keys(articulo)

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#search_mini_form > div.actions > button")
search_button.click()


#articulo_cards = driver.find_elements(By.CSS_SELECTOR, "#maincontent > div.columns > div.column.main > div.search.results > div.products.wrapper.grid.products-grid > ol")
#articulo_cards = driver.find_elements(By.CSS_SELECTOR, "#maincontent > div.columns > div.column.main > div.search.results > div.products.wrapper.grid.products-grid > ol > li")

articulo_cards = driver.find_elements(By.CSS_SELECTOR, "#maincontent > div.columns > div.column.main > div.search.results > div.products.wrapper.grid.products-grid > ol > li")
#vehicle_cards = driver.find_elements(By.CSS_SELECTOR, "#featuredUsed > div.xl3")




mongodb = MongoDriver()

for card in articulo_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "div > strong").text
        #price = card.find_element(By.CSS_SELECTOR, "div > div.price-box.price-final_price > span.special-price").text
        print(title)
        print(f"${price}")

        artic_actual = {
            "consulta": articulo,
            "resultado": {
                "title": title,
                 "price": price,
            }
        }

        mongodb.insert_record(record=artic_actual, username="LICUADORA")

        print("Correcto++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("Excepcion++++++++++++++++++++++++++++++++")


driver.close()