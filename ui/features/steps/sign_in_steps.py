from behave import when, then, given
from ui.src.pages.sign_in import SigninAppPage
from utilties.data_generator import AccountCreation


def get_data(context):
    ac = AccountCreation().account_creation_data()
    return ac


@given("I Verify Login account screen page displayed")
def login_account_screen_page(context):
    context.new_page = SigninAppPage()
    context.new_page.verify_login_header_visible()


@when("And I Click on Signup to redirect create account page")
def click_on_signup_redirect(context):
    context.new_page.click_on_sign_up_redirect()


@then("Verify Create account screen page displayed")
def create_account_screen_page(context):
    context.new_page.verify_create_account_visible()


@then("Enter First Name")
def enter_first_name(context):
    fn = get_data(context)['first_name']
    context.new_page.firstname_inputtext(firstname=fn)


@then("Enter Last Name")
def enter_last_name(context):
    ln = get_data(context)['last_name']
    context.new_page.lastname_inputtext(lastname=ln)


@then("Select Country")
def select_country_name(context):
    country = get_data(context)['country']
    context.new_page.select_country(country)


@then("I click on continue button")
def click_on_continue_button(context):
    context.new_page.click_continue_button()


@then("I entering email in email field")
def entering_email(context):
    email = get_data(context)['email']
    context.new_page.enter_email_field(email)


@then("I entering password in password field")
def entering_password(context):
    password = get_data(context)['password']
    context.new_page.enter_password_field(password)


@then("I Click on Register button")
def click_on_register_button(context):
    context.new_page.click_on_register_button()


@then("I Click on next button on register page")
def click_on_register_button_page_next(context):
    context.new_page.click_on_next_button_register()


@when("I Click on Login button")
def click_on_login_button(context):
    context.new_page.click_on_login_button()

@then("I verify for email error field msg")
def email_error_field_msg(context):
    context.new_page.verify_email_field_error_msg()
