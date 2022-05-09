from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.time_out = 10

    def wait_for_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, self.time_out).until(EC.visibility_of_element_located
                                                               (locator=locator))

    def wait_for_presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, self.time_out).until(EC.presence_of_element_located(
            locator=locator))

    def press_enter(self, element):
        element.send_keys(Keys.ENTER)

    def press_page_down(self):
        html = self.driver.find_element(By.XPATH, '//body')
        html.send_keys(Keys.PAGE_DOWN)
