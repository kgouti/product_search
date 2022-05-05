import time

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
        # time.sleep(5)
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='First name']")))

    def enter_user_details_for_registration(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_email()
        self.enter_password()
        self.select_terms_conditions()
        self.click_create_new_account_button()
        # self.click_complete_registration_button()

    def enter_first_name(self):
        self.driver.find_element(By.XPATH,"//input[@aria-label='First name']").send_keys("Kartik")

    def enter_last_name(self):
        self.driver.find_element(By.XPATH, "//input[@aria-label='Last name']").send_keys("Gouti")

    def enter_email(self):
        self.driver.find_element(By.XPATH, "//input[@aria-label='Email']").send_keys("Abc13.def@gmail.com")

    def enter_password(self):
        self.driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys("A2bc.223@gmail.com")

    def select_terms_conditions(self):
        self.driver.find_element(By.XPATH,"//*[contains(text(),'By re')]").click()

    def click_create_new_account_button(self):
        self.driver.find_element(By.ID,'cta').click()

    def click_complete_registration_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                       ((By.XPATH, "//*[@id='scrollingLayer']/div[2]/div[6]"))).click()
