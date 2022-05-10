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
    search_results_text1 = (By.XPATH,"//h3[@class='search-results_searchResults__title__cOoGR']")
    see_all = (By.XPATH,"//div[@class='extended-search-bar_extendedSearchBar__options__jmFks']")

class search:
    z = "//div[@class='card-product-search_cardProductSearch__HC_DF']"
    notifications_no_button = (By.ID,'emarsys-consent-cancel')
    product_grid = (By.XPATH, z)
    seller1 = (By.XPATH, z + "/div[2]/span") #new
    price1 = (By.XPATH, z + "/div[4]") # new
    seller = (By.XPATH, "//div[@class='card-product-search_cardProductSearch__vendor__fO9FB']/span")
    price = (By.XPATH, "//div[@class='card-product-search_cardProductSearch__price__11edc']")
