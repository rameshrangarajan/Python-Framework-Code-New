import pytest
from src.pages import yahoo_mail_page as yahoomail
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

scenarios('../feature_files/yahoo_login.feature')
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


@given('the user logs into the application')
@pytest.fixture()
def yahoo_mail_page(app_login):
    _yahoo_page = yahoomail.YahooMailPage(app_login.driver)
    return _yahoo_page


@when('the user clicks the Mail button')
def click_mail_link(yahoo_mail_page):

    # time.sleep(5)

    yahoo_mail_page.click_mail_button('yahoo_mail_button_loc', 'mail_button')
    time.sleep(3)


@then(parsers.cfparse('the login name label is {labelname}'))
def verify_login_label(yahoo_mail_page, labelname):
    assert labelname == yahoo_mail_page.get_element_text('yahoo_username_label_loc', 'username_label'), \
        "label names mismatch"


@given('the user clicks the Mail button')
def click_mail_link(yahoo_mail_page):

    # time.sleep(5)

    yahoo_mail_page.click_mail_button('yahoo_mail_button_loc', 'mail_button')
    time.sleep(5)


@when('the user clicks on the Sign Out link')
def click_sign_out_link(yahoo_mail_page):

    yahoo_mail_page.hover_over('yahoo_username_label_loc', 'username_label')
    time.sleep(3)
    yahoo_mail_page.click_signout_link('yahoo_signout_link_locator', 'signout_link')
    time.sleep(3)


@then(parsers.cfparse('the sign in label is {SignInLabel}'))
def verify_sign_in_label(yahoo_mail_page, SignInLabel):
    assert SignInLabel == yahoo_mail_page.get_element_text('yahoo_sign_In_loc', 'sign_in_label'), \
        "sign in label mismatch"

