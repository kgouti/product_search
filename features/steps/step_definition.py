from behave import *
from pages.Login import Login
from pages.LandingPage import LandingPage
use_step_matcher("re")


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