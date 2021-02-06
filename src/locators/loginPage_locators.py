"""
This file stores the key value pair for locators used in the LoginPage class.
"""

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """
    Locators for the Login Page.

    """
    login_input_field_loc = {
        'username': (By.NAME, 'username'),
        'password': (By.NAME, 'password')
    }

    login_button_loc = {
        'btn_next': (By.NAME, 'signin'),
        'stay_signed_in': (By.XPATH, "//div[@class='helper-links-container']//span[@class='stay-signed-in checkbox-container']//label"),
        'btn_submit': (By.NAME, 'verifyPassword')
    }
