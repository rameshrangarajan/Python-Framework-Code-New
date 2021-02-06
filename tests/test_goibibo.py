import pytest
from src.pages import goibibo_page as goibibo_search
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

scenarios('../feature_files/goibibo.feature')


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


@given('the user opens the goibibo website')
@pytest.fixture()
def goibibo_search_page(launch_goibibo_in_browser):
    _goibibo_page = goibibo_search.GoibiboPage(launch_goibibo_in_browser.driver)
    return _goibibo_page


@given('the user enter <origin> into from text box')
def enter_from_string_and_select_value(goibibo_search_page, origin):
    goibibo_search_page.enter_from_string(origin)
    time.sleep(3)
    goibibo_search_page.click_search_element('from_select_loc', 'from_select_value')


@given('the user enter <destination> into destination text box')
def enter_to_string_and_select_value(goibibo_search_page, destination):
    goibibo_search_page.enter_dest_string(destination)
    time.sleep(3)
    goibibo_search_page.click_search_element('dest_select_loc', 'dest_select_value')


@given('the user selects a departure date')
def select_departure_date(goibibo_search_page):
    time.sleep(3)
    goibibo_search_page.select_date('departure_date_loc', 'departure_date_value')


@given('the user selects a return date')
def select_return_date(goibibo_search_page):
    time.sleep(3)
    goibibo_search_page.click_return_calendar_element('return_calendar_loc', 'return_calendar')
    time.sleep(3)
    goibibo_search_page.select_date('return_date_loc', 'return_date_value')


@when('the user clicks the search button')
def click_search_button(goibibo_search_page):
    time.sleep(3)
    goibibo_search_page.click_search_element('search_button_loc', 'search_button')


@then(parsers.cfparse('the new page contains the text {farecalendar}'))
def verify_label(goibibo_search_page, farecalendar):
    time.sleep(6)
    assert farecalendar == goibibo_search_page.get_element_text('fare_calendar_label_loc', 'fare_calendar_label'), \
        "label names mismatch"


@then('the book button is displayed and enabled')
def verify_book_button(goibibo_search_page):
    time.sleep(3)
    assert goibibo_search_page.book_button('book_button_loc', 'book_button')
