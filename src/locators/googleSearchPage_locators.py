"""
This file stores the key value pair for locators used in the Search Page class.
"""

from selenium.webdriver.common.by import By


class GoogleSearchPageLocators(object):
    """
    Locators for the Search Page.

    """
    search_input_loc = {
        'search_input': (By.NAME, 'q')
    }

    search_result_string_loc = {
        'result_string': (By.XPATH, "//div[@class='tF2Cxc']//div[@class='yuRUbf']//a//h3//span")
    }

    search_btn_loc = {
        'submit_search': (By.CSS_SELECTOR, '.btn.search-btn'),
    }

    google_search_suggestion = {
        'search_suggestion': (By.XPATH, "//*[. = 'selenium tutorial']")
    }
