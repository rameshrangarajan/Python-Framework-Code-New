import pytest
from src.pages import dashboard_page as dashboard
import time
from src.pages import base_page as bp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger(__name__)

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

scenarios('../feature_files/dashboard.feature')


class global_variables(object):
    def __init__(self):
        self.oldcount = None
        self.flag = 0
        self.oldcount1 = None
        self.oldcount2 = None
        self.timeperiod = None
        self.searchquery = None


gl_var = global_variables()


@given('the user logs into the dashboard')
@pytest.fixture()
def dashboard_page(dashboard_login):
    _dashboard_page = dashboard.DashboardPage(dashboard_login.driver)
    return _dashboard_page


@then(parsers.cfparse('verify that the columns {col1} , {col2} , {col3} , {col4} , {col5} , {col6} and {col7} exist'))
def verify_all_column_titles(dashboard_page, col1, col2, col3, col4, col5, col6, col7):
    time.sleep(30)
    print(dashboard_page.driver.current_url)
    print(dashboard_page.driver.page_source)
    assert dashboard_page.get_element_text('column_locs','no_of_users_title') == col1, 'No. of Users Column does not exist'
    assert dashboard_page.get_element_text('column_locs','no_of_queries_title') == col2, 'No. of Queries Column does not exist'
    assert dashboard_page.get_element_text('column_locs','no_of_downloads_title') == col3, 'No. of Downloads Column does not exist'
    assert dashboard_page.get_element_text('column_locs','no_of_downloads_on_first_page_title') == col4, 'No. of Downloads on first page Column does not exist'
    assert dashboard_page.get_element_text('column_locs','no_of_ratings_received_title') == col5, 'No. of Ratings Column does not exist'
    assert dashboard_page.get_element_text('column_locs','average_query_time_title') == col6, 'Average query time Column does not exist'
    assert dashboard_page.get_element_text('column_locs','no_accepted_suggestions_title') == col7, 'No. of accepted suggestions Column does not exist'


@then(parsers.cfparse('verify that the rows {row1} , {row2} , {row3} , {row4} , {row5} and {row6} exist'))
def verify_all_row_titles(dashboard_page, row1, row2, row3, row4, row5, row6):
    time.sleep(30)
    assert dashboard_page.get_element_text('row_locs','today_title') == row1, 'Today row does not exist'
    assert dashboard_page.get_element_text('row_locs','this_week_title') == row2, 'This week row does not exist'
    assert dashboard_page.get_element_text('row_locs','last_week_title') == row3, 'Last week row does not exist'
    assert dashboard_page.get_element_text('row_locs','this_month_title') == row4, 'This month row does not exist'
    assert dashboard_page.get_element_text('row_locs','last_month_title') == row5, 'Last month row does not exist'
    assert dashboard_page.get_element_text('row_locs','this_year_title') == row6, 'This year row does not exist'


@then('verify that all cells in the table are non empty')
def verify_cells_non_empty(dashboard_page):
    time.sleep(30)
    all_rows = dashboard_page.find_all_elements('row_locs','single_cell_loc')

    for each_cell in all_rows:
        print('\n' + each_cell.text)
        if "." in each_cell.text:
            assert type(float(each_cell.text)) == float, 'Cell value is not a number or is empty'
        else:
            assert type(int(each_cell.text)) == int, 'Cell value is not a number or is empty'


@then(parsers.cfparse('verify the labels {label1} and {label2} are present'))
def verify_labels(dashboard_page, label1, label2):
    time.sleep(30)
    assert dashboard_page.get_element_text('queries_loc','recent_queries_label') == label1, 'Recent queries label mismatch or not present'
    assert dashboard_page.get_element_text('queries_loc','trending_queries_label') == label2, 'Trending queries label mismatch or not present'


@then(parsers.cfparse('verify that the recent queries and trending queries sections are non empty and contain {num} items each'))
def verify_labels(dashboard_page, num):
    time.sleep(30)
    assert str(len(dashboard_page.find_all_elements('queries_loc','recent_queries_items'))) == num, 'Recent queries section has no items or less than 15 items'
    assert str(len(dashboard_page.find_all_elements('queries_loc','trending_queries_items'))) == num, 'Trending queries section has no items or less than 15 items'


@then(parsers.cfparse('verify that the caption {dashboard_title} appears'))
def verify_dashboard_caption(dashboard_page, dashboard_title):
    time.sleep(30)
    assert dashboard_page.get_element_text('dashboard_title_loc','dashboard_title') == dashboard_title, 'Dashboard title missing or not matching'
