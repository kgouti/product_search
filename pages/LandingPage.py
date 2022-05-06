from pages import BasePage
from locators import landing

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage():
    def __init__(self, driver):
        # super().__init__(driver=driver)
        self.driver = driver

    def check_presence_of_search_text_box(self):
        return    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located
                                            (landing.search_text_box)).is_displayed()
         # (By.XPATH, "//*[@id='desktop-search-input']")

    def search_for_product(self,product_name):
        search_text_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located
                                            (landing.search_text_box))
        #(By.XPATH, "//*[@id='desktop-search-input']")

        search_text_box.send_keys(product_name)
        self.driver.find_element(*landing.search_button).click()
        #By.XPATH,"//i[@class='icon icon--search ']"
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located
                                            (landing.search_results_text))
        #(By.XPATH,"//div[@id='__next']/main/nav/ul/li[2]/a/div")

    def check_for_search_results_text(self,url_text):
        return WebDriverWait(self.driver, 5).until(EC.url_contains(url_text))