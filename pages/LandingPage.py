from pages.BasePage import BasePage
from locators import landing,search
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_presence_of_search_text_box(self):
        return self.wait_for_visibility_of_element(landing.search_text_box).is_displayed()
         # (By.XPATH, "//*[@id='desktop-search-input']")

    def search_for_product(self,product_name):
        search_text_box = self.wait_for_visibility_of_element(landing.search_text_box)
        # search_text_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located
        #                                     (landing.search_text_box))
        #(By.XPATH, "//*[@id='desktop-search-input']")

        search_text_box.send_keys(product_name)
        time.sleep(3)
        # self.wait_for_presence_of_element_located(landing.see_all)
        # time.sleep(2)
        self.press_enter(search_text_box)
        # self.driver.find_element(*landing.search_button).click()
        #By.XPATH,"//i[@class='icon icon--search ']"
        search = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                            (landing.search_results_text1))
        print(search.text)
        self.press_page_down()
        #(By.XPATH,"//div[@id='__next']/main/nav/ul/li[2]/a/div")

    def click_no_for_notifications(self):
        # time.sleep(100)
        self.wait_for_presence_of_element_located(search.notifications_no_button).click()
        # time.sleep(5)