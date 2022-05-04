import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import webdriver_path, url
from selenium.webdriver.common.action_chains import ActionChains


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
driver.find_element(By.XPATH,"//input[@aria-label='First name']").send_keys("Kartik")
driver.find_element(By.XPATH, "//input[@aria-label='Last name']").send_keys("Gouti")
driver.find_element(By.XPATH, "//input[@aria-label='Email']").send_keys("abc.def@gmail.com")
driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys("Abc.123@gmail.com")
# time.sleep(100)
driver.find_element(By.CLASS_NAME,"s t wf hf").click()
time.sleep(100)
# b.perform()


