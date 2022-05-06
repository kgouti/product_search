from selenium.webdriver.common.by import By

class login:
    user_profile_icon = (By.CLASS_NAME,"profile-dropdown_profileIcon__Drxrp")
    join_rakuten_text = (By.LINK_TEXT, "Join Rakuten")
    first_name = (By.XPATH,"//input[@aria-label='First name']")
    last_name = (By.XPATH,"//input[@aria-label='Last name']")
    email = (By.XPATH, "//input[@aria-label='Email']")
    password = (By.XPATH, "//input[@aria-label='Password']")
    terms_conditions = (By.XPATH,"//*[contains(text(),'By re')]")
    create_new_button = (By.ID,'cta')
    complete_registration_button = (By.XPATH, "//*[@id='scrollingLayer']/div[2]/div[6]")

class landing:
    search_text_box = (By.XPATH, "//*[@id='desktop-search-input']")
    search_button = (By.XPATH,"//i[@class='icon icon--search ']")
    search_results_text = (By.XPATH,"//div[@id='__next']/main/nav/ul/li[2]/a/div")