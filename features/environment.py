from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import webdriver_path, url


def before_scenario(context, scenario):
    print('++++ Executing Scenario +++ ' + scenario.name)
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Chrome(executable_path = webdriver_path)
    # context.driver.find_element(By.CLASS_NAME,"profile-dropdown_profileIcon__Drxrp")
    context.driver.maximize_window()
    open_url(context)
    # context.driver.get(url)
    # return context.driver


def open_url(context):
    context.driver.get(url)
    try:
        privacy_agree_button = context.driver.find_element(By.ID, "didomi-notice-agree-button")
        privacy_agree_button.click()
    except NoSuchElementException:
        print("Element privacy_agree_button does not exist")




# def after_scenario(context, scenario):
#     print('++++Scenario {} ends +++++'.format(scenario.name))
#     # context.driver.close()