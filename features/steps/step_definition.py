from behave import given,when,then,step
from pages.Login import Login
from pages.LandingPage import LandingPage
from pages.ResultsPage import Results


@given("user opens rakuten url for registration")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page = Login(context.driver)
    context.login_page.navigate_to_login_page()
    print("Usr1")


@when("user enters valid details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page.enter_user_details_for_registration()
    print("Usr2")

@step("user is registered successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page.click_complete_registration_button()
    print("Usr3")


@then("search box is displayed on landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.landing_page = LandingPage(context.driver)
    actual_search_box_visible = context.landing_page.check_presence_of_search_text_box()
    assert actual_search_box_visible is True


@given("user logs into rakuten profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page = Login(context.driver)
    context.login_page.navigate_to_login_page()
    context.login_page.enter_user_details_for_registration()
    context.login_page.click_complete_registration_button()


@when("{product} is searched in the search text box")
def step_impl(context,product):
    """
    :param product: product to search for
    :type context: behave.runner.Context
    """
    context.landing_page = LandingPage(context.driver)
    context.landing_page.click_no_for_notifications()
    context.landing_page.search_for_product(product_name=product)


@then("verify that new page url contains keyword {search_text}")
def step_impl(context,search_text):
    """
    :param search_text: Expected text to be searched in the url
    :type context: behave.runner.Context
    """
    # actual_url = context.driver.current_url
    # assert actual_url.count(search_text) > 0
    context.results_page = Results(context.driver)
    actual_search_text_available = context.results_page.check_for_search_results_text(search_text)
    print(actual_search_text_available)
    assert actual_search_text_available is True


@then("verify price is available for each card")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.results_page = Results(context.driver)
    context.list_of_sellers_prices = context.results_page.find_products()

    for i in context.list_of_sellers_prices:
        assert i[1] is not None


@step("print seller and the price of each product")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.list_of_sellers_prices)