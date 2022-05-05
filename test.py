import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import webdriver_path, url
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(executable_path = webdriver_path)
driver.maximize_window()
driver.get(url)
# time.sleep(1)
privacy_button =  driver.find_element(By.ID,"didomi-notice-agree-button")
if privacy_button:
    privacy_button.click()
time.sleep(3)
a = ActionChains(driver=driver)
m = driver.find_element(By.CLASS_NAME,"profile-dropdown_profileIcon__Drxrp")
b = a.move_to_element(m).perform()
driver.find_element(By.LINK_TEXT,"Join Rakuten").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@aria-label='First name']").send_keys("Kartik1")
driver.find_element(By.XPATH, "//input[@aria-label='Last name']").send_keys("Gouti1")
driver.find_element(By.XPATH, "//input[@aria-label='Email']").send_keys("abc2.def@gmail.com")
driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys("A2bc.223@gmail.com")
# time.sleep(100)
# body = driver.find_element(By.CSS_SELECTOR,'body')
# body.send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,"//*[contains(text(),'By re')]").click()
driver.find_element(By.ID,'cta').click()
# time.sleep(5)

WebDriverWait(driver,5).until(EC.element_to_be_clickable
                              ((By.XPATH,"//*[@id='scrollingLayer']/div[2]/div[6]"))).click()
# driver.find_element(By.XPATH,"//*[@id='scrollingLayer']/div[2]/div[6]").click()
driver.find_element(By.ID,"//input[@id='desktop-search-input']").is_displayed()
time.sleep(100)
# b.perform()
WebDriverWait(driver,5).until(EC.visibility_of_element_located("//*[@id='scrollingLayer']/div[2]/div[6]")).is_displayed()

