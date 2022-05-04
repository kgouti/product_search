from selenium.common.exceptions import NoSuchElementException

from pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def navigate_to_login_page(self):
        a = ActionChains(driver=self.driver)
        m = self.driver.find_element(By.CLASS_NAME,"profile-dropdown_profileIcon__Drxrp")
        a.move_to_element(m).perform()
        self.driver.find_element(By.LINK_TEXT, "Join Rakuten").click()
        # WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,"s t wc hc")))

    def enter_first_name(self):
        self.driver.find_element(By.XPATH,"//input[@aria-label='First name']").send_keys("Kartik")

    def enter_last_name(self):
        self.driver.find_element(By.XPATH, "//input[@aria-label='Last name']").send_keys("Gouti")

    def enter_email(self):
        self.driver.find_element(By.XPATH, "//input[@aria-label='Email']").send_keys("abc.def@gmail.com")

    def enter_password(self):
        self.driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys("abc.def@gmail.com")

    def click_create_new_account_button(self):
        self.driver.find_element(By.LINK_TEXT,"Create a new account").click()
