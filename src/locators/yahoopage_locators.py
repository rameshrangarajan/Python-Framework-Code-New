from selenium.webdriver.common.by import By


class YahooPageLocators(object):
    """
    Locators for the Yahoo Page.

    """
    yahoo_mail_button_loc = {
        'mail_button': (By.ID, 'header-mail-button')
    }

    yahoo_username_label_loc = {
        'username_label': (By.XPATH, "//span[@role='presentation']")
    }

    yahoo_signout_link_locator = {
        'signout_link': (By.XPATH, "//div[@id='ybarAccountContainer']//div[@id='ybarAccountMenuBody']//a[3]")
    }

    yahoo_sign_In_loc = {
        'sign_in_label': (By.XPATH, "//li[@id='header-profile-menu']//a[@id='header-signin-link']//span")
    }
