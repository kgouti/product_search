from behave import *
from pages.Login import Login
use_step_matcher("re")


@given("user opens rakuten url for registration")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    login_page = Login(context.driver)
    login_page.navigate_to_login_page()
    print("Usr1")


@when("user enters valid details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("Usr2")

@then("user is registered successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("Usr3")