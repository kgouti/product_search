from pages import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage():
    def __init__(self, driver):
        # super().__init__(driver=driver)
        self.driver = driver

    def check_presence_of_search_text_box(self):
        return    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located
                                            ((By.XPATH, "//*[@id='desktop-search-input']"))).is_displayed()
         # return True if  len(self.driver.find_elements(By.XPATH,"//*[@id='desktop-search-input']")) > 0 else False
