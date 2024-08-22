from ui.src.PlatformConfig import PlatformConfig
from ui.src.base.BaseAppPage import BaseAppPage
import logging

log = logging.getLogger(__name__)


class SigninAppPage(BaseAppPage):
    """Sign in screen PageObject"""

    def __init__(self):
        super().__init__()

    signIn_page_locators = {
        "Android": {
            "welcome_to_scopex": "//android.widget.TextView[@text='Welcome to ScopeX']",
            "next_button": "//android.view.ViewGroup[@content-desc='Next']",
            "register_next_button" : "//android.widget.Button[@content-desc='Next']",
            "skip_button": "//android.widget.TextView[@text='Skip']",
            "get_started_button": "//android.widget.TextView[@text='Get started']",
            "login_email_input": "login-email-input",
            "login_password_input": "login-password-input",
            "Log_In": "//android.widget.Button[@content-desc='Log In']",
            "register_button": "//android.widget.Button[@content-desc='Register']",
            "sign_up_redirect": "//android.widget.TextView[@resource-id='sign-up-redirect']",
            "first_name_input": "//android.widget.EditText[@resource-id='first-name-input']",
            "last_name_input": "//android.widget.EditText[@resource-id='last-name-input']",
            "continue_button": "//android.widget.TextView[@text='Continue']",
            "login_in_redirect": "//android.widget.TextView[@text='Log in']",
            "select_country": "//android.view.ViewGroup[@content-desc='Select']",
            "create_account_header": "//android.widget.TextView[@resource-id='register1-heading']",
            "login_to_scopex": "//android.widget.TextView[contains(@text,'Log in to ScopeX')]",
            "search_country": "//android.widget.EditText[@resource-id='countryCodesPickerSearchInput']",
            "select_searched_country": "//android.view.ViewGroup[contains(@content-desc, '{}')]",
            "email_field": "//android.widget.EditText[@resource-id='RNE__Input__text-input' and @text='Email']",
            "password_field": "//android.widget.EditText[@resource-id='RNE__Input__text-input' and @text='Password']",
            "confirm_password_field": "//android.widget.EditText[@resource-id='RNE__Input__text-input' and @text='Confirm Password']",
            "enter_email_address_error_msg": "//android.widget.TextView[@text='Please enter your email address!']"
        },
        "iOS": {
        }
    }

    def skip_walkthrough(self):
        log.info("Check if app launched first time, walkthrough will visible")
        walkthrough_status = self.check_visibility_of_element(
            self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                       element_key="welcome_to_scopex"), wait_time=5)
        if walkthrough_status:
            log.info("walk through is displayed")
            self.click_element(self.get_xpath_by_platform_from_dictionary(xpath_dict=self.signIn_page_locators,
                                                                          element_key="next_button"))
            self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                          element_key="get_started_button"))
            walkthrough_status = True
        else:
            log.info("walk through is not displayed")
            walkthrough_status = False
        return walkthrough_status

    def verify_login_header_visible(self):
        log.info("verify login header visible")
        self.check_if_element_displayed(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                                   element_key="login_to_scopex"))

    def verify_create_account_visible(self):
        log.info("verify create account visible")
        self.check_if_element_displayed(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                                   element_key="create_account_header"))

    def click_on_sign_up_redirect(self):
        log.info("Click on sign up redirect button")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="sign_up_redirect"))

    def click_on_skip_button(self):
        log.info("Click on Skip button in walkthrough screen")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="skip_button"))

    def firstname_inputtext(self, firstname):
        log.info("Enter firstname")
        self.send_keys(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                  element_key="first_name_input"), value=firstname)

    def lastname_inputtext(self, lastname):
        log.info("Enter lastname")
        self.send_keys(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                  element_key="last_name_input"), value=lastname)

    def select_country(self, country):
        log.info("Select Country")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="select_country"))
        self.send_keys(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                  element_key="search_country"), value=country)
        country_updated_xpath = self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                           element_key="select_searched_country").format(
            country)
        self.click_element(country_updated_xpath)

    def click_continue_button(self):
        log.info("Click on continue button")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="continue_button"))

    def enter_email_field(self, email_text):
        log.info("Enter email field")
        self.send_keys(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                  element_key="email_field"), value=email_text)

    def enter_password_field(self, password):
        log.info("Enter password field")
        self.send_keys(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                  element_key="password_field"), value=password)
        self.send_keys(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                  element_key="confirm_password_field"), value=password)

    def click_on_next_button(self):
        log.info("Click on next button")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="next_button"))

    def click_on_register_button(self):
        log.info("Click on register button")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="register_button"))

    def click_on_next_button_register(self):
        log.info("Click on register next button")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="register_next_button"))

    def click_on_login_button(self):
        log.info("Click on login button")
        self.click_element(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                      element_key="Log_In"))

    def verify_email_field_error_msg(self):
        log.info("verify email field error msg")
        self.check_if_element_displayed(self.get_xpath_by_platform_from_dictionary(self.signIn_page_locators,
                                                                                   element_key="enter_email_address_error_msg"))

