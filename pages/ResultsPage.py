import time

from pages.BasePage import BasePage
from locators import search

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Results(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def check_for_search_results_text(self, url_text):
        return WebDriverWait(self.driver, 5).until(EC.url_contains(url_text))

    def click_no_for_notifications(self):
        self.wait_for_presence_of_element_located(search.notifications_no_button).click()

    def find_products(self):
        time.sleep(5)
        list_of_sellers_elements = self.driver.find_elements(*search.seller1)
        list_of_seller_values = [j.text for j in list_of_sellers_elements]
        list_price_of_each_product_elements = self.driver.find_elements(*search.price1)
        list_price_of_each_product_values = [j.text for j in list_price_of_each_product_elements]
        combined_prices = [list(z) for z in zip(list_of_seller_values, list_price_of_each_product_values)]
        return combined_prices