import time

from selenium.common.exceptions import NoSuchElementException

from pages.BasePage import BasePage
from properties import customer
from locators import login
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def navigate_to_login_page(self):
        a = ActionChains(driver=self.driver)
        m = self.driver.find_element(*login.user_profile_icon)#By.CLASS_NAME,"profile-dropdown_profileIcon__Drxrp")
        a.move_to_element(m).perform()
        self.driver.find_element(*login.join_rakuten_text).click() #By.LINK_TEXT, "Join Rakuten"
        # time.sleep(5)
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(
            login.first_name)) #By.XPATH,"//input[@aria-label='First name']"

    def enter_user_details_for_registration(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_email()
        self.enter_password()
        self.select_terms_conditions()
        self.click_create_new_account_button()
        # self.click_complete_registration_button()

    def enter_first_name(self):
        self.driver.find_element(*login.first_name).send_keys(customer.get("first_name"))
        #By.XPATH,"//input[@aria-label='First name']"
    def enter_last_name(self):
        self.driver.find_element(*login.last_name).send_keys(customer.get("last_name"))
        #By.XPATH,"//input[@aria-label='Last name']"
    def enter_email(self):
        self.driver.find_element(*login.email).send_keys(customer.get("email"))
        #By.XPATH, "//input[@aria-label='Email']"
    def enter_password(self):
        self.driver.find_element(*login.password).send_keys(customer.get("password"))
        #By.XPATH, "//input[@aria-label='Password']"

    def select_terms_conditions(self):
        self.driver.find_element(*login.terms_conditions).click()
        #By.XPATH,"//*[contains(text(),'By re')]"

    def click_create_new_account_button(self):
        self.driver.find_element(*login.create_new_button).click()
        #By.ID,'cta'

    def click_complete_registration_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                       (login.complete_registration_button)).click()
        #(By.XPATH, "//*[@id='scrollingLayer']/div[2]/div[6]")