import pytest
from src.pages import google_search_page as google_search
import time
from src.pages import base_page as bp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

logger = logging.getLogger(__name__)

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

scenarios('../feature_files/google_search.feature')
# scenarios('../feature_files/download_func.feature')
# scenarios('../feature_files/training.feature')

class global_variables(object):
    def __init__(self):
        self.oldcount = None
        self.flag = 0
        self.oldcount1 = None
        self.oldcount2 = None
        self.timeperiod = None
        self.searchquery = None
        self.suggestionchiptext = None
        self.last_height = None
        self.new_height = None


gl_var = global_variables()


@given('the user opens the Google website')
@pytest.fixture()
def google_search_page(launch_browser):
    _search_page = google_search.GoogleSearchPage(launch_browser.driver)
    return _search_page


@given('the user enter <search_string> into search text box')
def enter_string(google_search_page, search_string):
    time.sleep(3)
    google_search_page.enter_search_string(search_string)


@when('the user presses the enter key')
def press_enter_key(google_search_page):
    time.sleep(2)
    google_search_page.press_enter_key('search_input_loc', 'search_input', Keys.ENTER)
    time.sleep(5)


@then('the new page contains the text <result_string>')
def verify_result_string(google_search_page, result_string):
    assert result_string.lower() == google_search_page.get_element_text('search_result_string_loc', 'result_string').lower(), \
        "result values mismatch"


@when('the user presses the down arrow key')
def press_down_arrow_key(google_search_page):
    time.sleep(1)
    google_search_page.press_enter_key('search_input_loc', 'search_input', Keys.ARROW_DOWN)


@when(parsers.cfparse('the user selects the option {search_option}'))
def select_search_suggestion(google_search_page, search_option):
    time.sleep(3)
    # google_search_page.click_search_element('google_search_suggestion', 'search_suggestion')
    google_search_page.select_from_list_box('google_search_suggestion', 'search_suggestion', search_option)
    time.sleep(3)


@when('the user selects the option selenium tutorial')
def select_search_suggestion(google_search_page):
    time.sleep(3)
    google_search_page.click_search_element('google_search_suggestion', 'search_suggestion')
    # google_search_page.select_from_list_box('google_search_suggestion', 'search_suggestion', search_option)
    time.sleep(3)
