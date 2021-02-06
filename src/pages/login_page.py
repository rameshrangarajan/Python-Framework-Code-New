import logging
from src.pages import base_page
from src.locators.loginPage_locators import LoginPageLocators
import time


class LoginPage(base_page.Page):
    @base_page.log_func_name
    def get_title(self):
        """Return the page title"""
        logger = logging.getLogger(__name__)
        logger.info("Getting page title %s", self.driver.title)
        return self.driver.title

    @base_page.log_func_name
    def set_user_name(self, username):
        """Set the user name field """
        self.set_field_value(LoginPageLocators.login_input_field_loc['username'], username)
        time.sleep(2)

    @base_page.log_func_name
    def uncheck_stay_signed_in(self):
        """uncheck the stay signed in checkbox"""
        self.click_element(LoginPageLocators.login_button_loc['stay_signed_in'])
        time.sleep(2)

    @base_page.log_func_name
    def click_next_button(self):
        """click the Next button"""
        self.click_element(LoginPageLocators.login_button_loc['btn_next'])
        time.sleep(3)

    @base_page.log_func_name
    def set_password(self, password):
        """Set the password field """
        self.set_field_value(LoginPageLocators.login_input_field_loc['password'], password)
        time.sleep(2)

    @base_page.log_func_name
    def submit_login(self, button):
        """Submit login form for adfs server"""
        self.click_element(LoginPageLocators.login_button_loc['btn_submit'])
        time.sleep(5)
        return LoginPage(self.driver)

    @base_page.log_func_name
    def verify_element(self, type_of_locator, element):
        return self.verify_element_is_displayed_and_enabled(LoginPageLocators.__dict__[type_of_locator][element])

    @base_page.log_func_name
    def login_user(self, user_name, password):
        logger = logging.getLogger(__name__)
        logger.info("Logging in user %s.", user_name)
        try:
            self.set_user_name(user_name)
            self.uncheck_stay_signed_in()
            self.click_next_button()
            self.set_password(password)
            return self.submit_login('btn_submit')
        except:
            logger.info("User is already logged in")
            return LoginPage(self.driver)
