from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def before_scenario(context, scenario):
    print('++++ Executing Scenario +++ ' + scenario.name)
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    return context.driver


def after_scenario(context, scenario):
    print('++++Scenario {} ends +++++'.format(scenario.name))
    context.driver.close()