import pytest
from src.pages import search_page as search
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

scenarios('../feature_files/basic_search.feature')
scenarios('../feature_files/download_func.feature')
scenarios('../feature_files/training.feature')

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
def search_page(app_login):
    _search_page = search.SearchPage(app_login.driver)
    return _search_page


@given('the user enter <search_string> into search text box')
@given(parsers.cfparse('the user enter {search_string} into search text box'))
def enter_string(search_page, search_string):
    time.sleep(20)
    search_page.enter_search_string(search_string)


@when(parsers.cfparse('the user enter {search_string} into search text box'))
def enter_search_string_1(search_page, search_string):
    search_page.enter_search_string(search_string)


@given('the user clicks on the search button')
def click_search_button(search_page):

    time.sleep(5)

    search_page.click_search_element('search_btn_loc','submit_search')
    time.sleep(25)



@given('the user clicks on the preview button of first result')
def click_preview_button(search_page):

    time.sleep(5)

    gl_var.oldcount = search_page.get_element_text('download_count_loc', 'download_count')
    search_page.click_search_element('preview_button_loc','preview_button')

    time.sleep(5)


@given('the Like button for first result is enabled or the dislike button is enabled')
def is_like_or_dislike_enabled(search_page):


    gl_var.oldcount1 = search_page.get_element_text('like_dislike_count_loc', 'like_count')
    gl_var.oldcount2 = search_page.get_element_text('like_dislike_count_loc', 'dislike_count')
    if (search_page.is_element_displayed_and_enabled('like_dislike_loc','like_button','fill') and
        not search_page.is_element_displayed_and_enabled('like_dislike_loc','dislike_button','fill')):
        gl_var.flag = 2

    if (not search_page.is_element_displayed_and_enabled('like_dislike_loc','like_button','fill') and
        search_page.is_element_displayed_and_enabled('like_dislike_loc','dislike_button','fill')):
        gl_var.flag = 1

    if (not search_page.is_element_displayed_and_enabled('like_dislike_loc','like_button','fill') and
        not search_page.is_element_displayed_and_enabled('like_dislike_loc','dislike_button','fill')):
        gl_var.flag = 0


@when('the user clicks on the Like or dislike link')
def click_like_or_dislike_button(search_page):
    time.sleep(5)

    if gl_var.flag == 1 or gl_var.flag == 0:
        search_page.click_search_element('like_dislike_loc', 'like_button')

    elif gl_var.flag == 2:
        search_page.click_search_element('like_dislike_loc', 'dislike_button')
    time.sleep(5)


@then('verify like count status or dislike count status')
def verify_like_or_dislike_count_status(search_page):
    if gl_var.flag == 1:
        print("Expected Like Count : " + str(int(gl_var.oldcount1) + 1))
        print("Actual Like Count : " + search_page.get_element_text('like_dislike_count_loc', 'like_count'))
        assert int(gl_var.oldcount1) + 1 == int(search_page.get_element_text('like_dislike_count_loc', 'like_count')), \
            "Like count mismatch "
        assert int(gl_var.oldcount2) - 1 == int(search_page.get_element_text('like_dislike_count_loc', 'dislike_count')), "Dislike count mismatch"
        assert search_page.is_element_displayed_and_enabled('like_dislike_loc', 'like_button', 'fill'), "Like icon is not filled"

    elif gl_var.flag == 2:
        print("Expected Dislike Count : " + str(int(gl_var.oldcount2) + 1))
        print("Actual Dislike Count : " + search_page.get_element_text('like_dislike_count_loc', 'dislike_count'))
        assert int(gl_var.oldcount2) + 1 == int(search_page.get_element_text('like_dislike_count_loc', 'dislike_count')), "Dislike count mismatch"
        assert int(gl_var.oldcount1) - 1 == int(search_page.get_element_text('like_dislike_count_loc', 'like_count')), "Like count mismatch"
        assert search_page.is_element_displayed_and_enabled('like_dislike_loc', 'dislike_button','fill'), "Dislike icon is not filled"

    elif gl_var.flag == 0:

        print("Expected Like Count : " + str(int(gl_var.oldcount1) + 1))
        print("Actual Like Count : " + search_page.get_element_text('like_dislike_count_loc', 'like_count'))
        assert int(gl_var.oldcount1) + 1 == int(search_page.get_element_text('like_dislike_count_loc', 'like_count')), \
            "Like count mismatch "
        assert search_page.is_element_displayed_and_enabled('like_dislike_loc', 'like_button','fill'), "Like icon is not filled"


@then('verify that one or more suggestions appear')
def verify_suggestions_appear(search_page):
    time.sleep(5)
    if search_page.findelement('search_bar_suggestions_loc','suggestions_root', 15):
        print("Number of suggestions : " + str(len(search_page.find_all_elements('search_bar_suggestions_loc','suggestions_list'))))

    assert search_page.findelement('search_bar_suggestions_loc','suggestions_root', 15), "No suggestions appeared"


@when('the user clicks on the first thumbnail of first result')
def click_thumbnail_icon(search_page):
    search_page.click_search_element('thumbnail_loc','thumbnail_icon')
    time.sleep(5)


@then('verify that the thumbnail opens up')
def verify_thumbnail_popup_opened_up(search_page):
    time.sleep(5)
    assert search_page.findelement('thumbnail_loc','thumbnail_popup', 15), 'Thumbnail popup is not opened up'


@then('verify that the thumbnail popup is closed')
def verify_thumbnail_popup_is_closed(search_page):
    time.sleep(5)
    assert not search_page.findelement('thumbnail_loc','thumbnail_popup', 15), 'Thumbnail popup is still opened up'


@when('user clicks on the third occurrence tile')
def click_third_ocurrence_tile_in_preview_popup(search_page):
    search_page.click_search_element('third_occurrence_tile_loc', 'third_occurrence_tile')
    time.sleep(5)


@when('the user clicks on search button')
def click_button(search_page):

    time.sleep(5)

    search_page.click_search_element('search_btn_loc','submit_search')

    time.sleep(25)


@when('the user clicks on the Profile icon')
def click_profile_icon(search_page):

    search_page.click_search_element('profile_icon_loc','profile_icon')

    time.sleep(5)


@when('the user clicks on page 3 link')
def click_page_three_link(search_page):

    element = search_page.findelement('page_3_link_loc','page_three_link')
    search_page.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    search_page.click_search_element('page_3_link_loc','page_three_link')

    time.sleep(25)


@when('the user clicks on next page link')
def click_next_page_link(search_page):

    element = search_page.findelement('next_page_link_loc', 'next_page_link')

    search_page.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    search_page.click_search_element('next_page_link_loc','next_page_link')

    time.sleep(25)


@when('the user clicks on the previous page link')
def click_previous_page_link(search_page):

    element = search_page.findelement('previous_page_link_loc', 'previous_page_link')
    search_page.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    search_page.click_search_element('previous_page_link_loc','previous_page_link')

    time.sleep(25)


@when('the user clicks on the last page link')
def click_last_page_link(search_page):

    element = search_page.findelement('last_page_link_loc', 'last_page_link')
    search_page.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    search_page.click_search_element('last_page_link_loc','last_page_link')

    time.sleep(25)


@when('the user clicks on the first page link')
def click_first_page_link(search_page):

    element = search_page.findelement('first_page_link_loc', 'first_page_link')
    search_page.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    search_page.click_search_element('first_page_link_loc','first_page_link')

    time.sleep(25)


@when('the user clicks on the Feedback sidebar')
def click_feedback_sidebar(search_page):

    search_page.click_search_element('feedback_locs','feedback_sidebar')

    time.sleep(5)


@when('the user selects a rating')
def select_feedback_rating(search_page):

    search_page.click_search_element('feedback_locs','four_star_rating')

    time.sleep(5)


@when(parsers.cfparse('the user enters some feedback text like {feedback_text}'))
def enter_feedback_text(search_page, feedback_text):

    search_page.enter_text_into_textfield('feedback_locs','feedback_text_area', feedback_text)

    time.sleep(5)


@when('the user clicks on the Submit button')
def click_feedback_submit_button(search_page):

    search_page.click_search_element('feedback_locs','feedback_submit_button')

    time.sleep(3)


@then(parsers.cfparse('verify that the message {message} appears'))
def verify_feedback_acknowledgement_message(search_page, message):
    print(search_page.get_element_text('feedback_locs','feedback_acknowledgement'))
    assert message in search_page.get_element_text('feedback_locs','feedback_acknowledgement'), 'Message not proper'


@then(parsers.cfparse('verify that the error message {error_message} appears'))
def verify_error_message(search_page, error_message):
    assert error_message in search_page.get_element_text('no_results_error_message_loc','error_message'), 'No error message or wrong message'


@given('the user clicks on next page link')
def click_next_page_link(search_page):

    element = search_page.findelement('next_page_link_loc', 'next_page_link')
    search_page.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    search_page.click_search_element('next_page_link_loc','next_page_link')

    time.sleep(25)


@then('verify page status as <page_status>')
def verify_result(search_page, page_status):
    assert page_status in search_page.get_element_text('page_status', 'pagination_status'), "Wrong pagination " \
                                                                                                   "status "


@then(parsers.cfparse('verify result is displayed with <search_string>'))
def verify_result(search_page, search_string):
    assert search_string.lower() == search_page.get_element_text().lower(), "Search string not present in result"


@then('verify result is displayed with <search_string1> and <search_string2>')
def verify_result(search_page, search_string1, search_string2):
    assert (search_string1.lower() == search_page.get_element_text('profile_username_loc', 'profile_username').lower()) and (search_string2.lower() == search_page.get_element_text('profile_emailid_loc', 'profile_emailid').lower()), "Profile values mismatch"


@when('the user clicks on Download button for first result')
def click_button(search_page):

    oldtab = search_page.get_window_handle()

    gl_var.oldcount = search_page.get_element_text('download_count_loc','download_count')

    search_page.click_search_element('download_button_loc','btn_download')
    search_page.switch_to_previous_tab(oldtab)


@when('the user clicks on the Xoriant icon')
def click_xoriant_icon(search_page):

    search_page.click_search_element('xoriant_icon_loc','xoriant_icon')
    time.sleep(5)


@when('the user clicks on Download button in the preview popup')
def click_button(search_page):
    oldtab = search_page.get_window_handle()

    search_page.click_search_element('download_button_preview_loc','btn_download')
    search_page.switch_to_previous_tab(oldtab)
    webdriver.ActionChains(search_page.driver).send_keys(Keys.ESCAPE).perform()


@when('the user presses the escape key of the keyboard')
def press_escape_key(search_page):
    webdriver.ActionChains(search_page.driver).send_keys(Keys.ESCAPE).perform()


@then('verify that the preview popup is closed')
def verify_preview_popup_is_closed(search_page):
    time.sleep(5)
    assert not search_page.findelement('preview_popup_loc','preview_popup', 15), 'Preview popup is still open'


@when('the user presses the enter key of the keyboard')
def press_enter_key(search_page):
    time.sleep(5)
    webdriver.ActionChains(search_page.driver).send_keys(Keys.ENTER).perform()
    time.sleep(5)


@when('the user clicks the Close button of the preview popup')
def click_preview_popup_close_button(search_page):
    search_page.click_search_element('preview_popup_locs','preview_close_button')


@when('the user clicks the Close button of the thumbnail popup')
def click_thumbnail_popup_close_button(search_page):
    search_page.click_search_element('thumbnail_loc','thumbnail_close')


@when(parsers.cfparse('the document {document_name} is displayed as first result'))
def document_is_displayed(search_page, document_name):
    assert search_page.get_element_text('document_details_loc','document_name') == document_name, 'Document name does not match'


@when('the user clicks on the fifth suggestion chip')
def click_suggestion_chip(search_page):

    gl_var.suggestionchiptext = search_page.get_element_text('suggestion_chip_loc','fifth_suggestion_chip')
    time.sleep(5)
    search_page.click_search_element('suggestion_chip_loc','fifth_suggestion_chip')
    time.sleep(5)


@when('the user clicks on the <time_period>')
def click_time_period_filter_button(search_page, time_period):
    if time_period == 'All':
        gl_var.timeperiod = "time period All"
        search_page.click_search_element('time_period_filter_loc','All_loc')
    elif time_period == 'thirty days':
        gl_var.timeperiod = "time period 30 days"
        search_page.click_search_element('time_period_filter_loc', 'thirty_days_loc')
    elif time_period == 'twelve months':
        gl_var.timeperiod = "time period 12 months"
        search_page.click_search_element('time_period_filter_loc','twelve_months_loc')
    elif time_period == 'three years':
        gl_var.timeperiod = "time period 3 years"
        search_page.click_search_element('time_period_filter_loc','three_years_loc')

    time.sleep(5)


@then(parsers.cfparse('verify results count status or error message as {error_message}'))
def verify_time_period_filter_functionality(search_page, error_message):
    if search_page.findelement('page_status','pagination_status'):
        index = search_page.get_element_text('results_out_of_loc', 'results_out_of').index('results out of')
        print("Total results count for " + gl_var.timeperiod + " : " + search_page.get_element_text('results_out_of_loc', 'results_out_of')[0:index - 1])
        assert len(search_page.find_all_elements('results_section_loc', 'results_section')) > 0, 'Results count not greater than zero'
    else:
        print("For " + gl_var.timeperiod + ", there were no results retrieved." +
              " Error message shown is : " + search_page.get_element_text('no_results_error_message_loc','error_message'))
        assert search_page.get_element_text('no_results_error_message_loc','error_message') == error_message, "No error message or mismatch in message"


@then(parsers.cfparse('verify that created by is {created_by}'))
def verify_created_by(search_page, created_by):
    assert search_page.get_element_text('document_details_loc','created_by') == created_by, 'Created by does not match'


@then(parsers.cfparse('verify that modified by is {modified_by}'))
def verify_modified_by(search_page, modified_by):
    assert search_page.get_element_text('document_details_loc','modified_by') == modified_by, 'Modified by does not match'


@then(parsers.cfparse('verify that created date is {created_date}'))
def verify_created_date(search_page, created_date):
    assert search_page.get_element_text('document_details_loc','created_date') == created_date, 'Created date does not match'


@then(parsers.cfparse('verify that last modified date is {last_modified_date}'))
def verify_last_modified_date(search_page, last_modified_date):
    assert search_page.get_element_text('document_details_loc','last_modified_date') == last_modified_date, 'Last modified date does not match'


@then(parsers.cfparse('verify download count increases and is displayed'))
def verify_download_count(search_page):

    assert int(search_page.get_element_text('download_count_loc', 'download_count')) == int(gl_var.oldcount) + 1, "Download Count not matching "


@then('verify slide title as <ppt_title>')
def verify_preview_popup_ppt_title(search_page, ppt_title):
    assert search_page.get_element_text('preview_popup_locs', 'ppt_title') == ppt_title, 'PPT titles do not match'


@then('verify slide name as <ppt_name>')
def verify_preview_popup_ppt_name(search_page, ppt_name):
    assert search_page.get_element_text('preview_popup_locs', 'ppt_name') == ppt_name, 'PPT names do not match'


@then('verify created by as <created_by>')
def verify_preview_popup_created_by(search_page, created_by):
    assert search_page.get_element_text('preview_popup_locs', 'created_by') == created_by, 'Created by do not match'


@then('verify last modified as <last_modified>')
def verify_preview_popup_last_modified(search_page, last_modified):
    assert search_page.get_element_text('preview_popup_locs', 'last_modified') == last_modified, 'Last modified do not match'


@then(parsers.cfparse('verify slide number status as {slide_status}'))
@then('verify slide number status as <slide_status>')
def verify_preview_popup_slide_status(search_page, slide_status):
    assert search_page.get_element_text('preview_popup_locs', 'slide_status') == slide_status, 'Slide status do not match'


@then('verify number of occurrences tiles as <number_occurrences_tiles>')
def verify_preview_popup_number_occurrences_tiles(search_page, number_occurrences_tiles):
    assert str(len(search_page.find_all_elements('preview_popup_locs','occurrences_tiles'))) == (str(number_occurrences_tiles)).strip(), 'Occurrences tiles number mismatch'


@then('verify that the download count in the preview popup is a number')
def verify_preview_popup_download_count_is_number(search_page):
    index = search_page.get_element_text('preview_popup_locs', 'download_count').index(':')
    print("Text after caption :" + search_page.get_element_text('preview_popup_locs', 'download_count')[index + 1 :])
    assert int(search_page.get_element_text('preview_popup_locs','download_count')[index+1 :]), 'No number present for download count'


@then(parsers.cfparse('verify that the landing page with title as {landing_page_title} is displayed'))
def verify_landing_page_title(search_page, landing_page_title):
    assert search_page.get_element_text('landing_page_locs','landing_page_title') == landing_page_title, 'Landing page not displayed'


@then('verify that a number appears before and after the caption results out of')
def verify_results_out_of_caption(search_page):
    index = search_page.get_element_text('results_out_of_loc','results_out_of').index('results out of')
    index_of_round_bracket = search_page.get_element_text('results_out_of_loc','results_out_of').index('(')
    print ("Text before caption :" + search_page.get_element_text('results_out_of_loc','results_out_of')[0:index-1])
    print("Text after caption :" + search_page.get_element_text('results_out_of_loc', 'results_out_of')[index + 15:index_of_round_bracket-1])
    assert int(search_page.get_element_text('results_out_of_loc','results_out_of')[0:index-1]), 'No number present before caption'
    assert int(search_page.get_element_text('results_out_of_loc','results_out_of')[index + 15:index_of_round_bracket-1]), 'No number present after caption'


@then(parsers.cfparse('the search bar contains the text {text}'))
def verify_search_bar_contents(search_page, text):
    assert search_page.findelement('search_input_loc','search_input').get_attribute("value") == text, 'No text or wrong text in search bar'


@then(parsers.cfparse('the Search related to caption shows {text}'))
def verify_search_bar_contents(search_page, text):
    assert text in search_page.get_element_text('search_related_to_caption_loc','search_related_to'), 'No text or wrong text in search related to caption'


@then('the search bar contains the suggestion chip text')
def verify_search_bar_contents(search_page):
    assert search_page.findelement('search_input_loc','search_input').get_attribute("value") == gl_var.suggestionchiptext, 'No text or wrong text in search bar'


@then('the Search related to caption shows the suggestion chip text')
def verify_search_bar_contents(search_page):
    assert gl_var.suggestionchiptext in search_page.get_element_text('search_related_to_caption_loc','search_related_to'), 'No text or wrong text in search related to caption'


@then(parsers.cfparse('verify that {trending_searches} and {topics} and {recently_added} captions appear on home page'))
def verify_home_page_captions(search_page, trending_searches, topics, recently_added):
    time.sleep(5)
    assert search_page.get_element_text('home_page_captions_loc','trending_searches') == trending_searches, 'trending searches caption mismatch'
    assert search_page.get_element_text('home_page_captions_loc','topics') == topics, 'topics caption mismatch'
    assert search_page.get_element_text('home_page_captions_loc','recently_added') == recently_added, 'recently added caption mismatch'


@then(parsers.cfparse('verify on home page that Trending Searches has {num1} chips and Topics has {num2} chips and Recently added has {num3} chips'))
def verify_home_page_captions(search_page, num1, num2, num3):
    time.sleep(5)
    assert len(search_page.find_all_elements('home_page_captions_loc','trending_searches__chips_count')) == int(num1), 'trending searches count mismatch'
    assert len(search_page.find_all_elements('home_page_captions_loc','topics_chips_count')) == int(num2), 'topics count mismatch'
    assert len(search_page.find_all_elements('home_page_captions_loc','recently_added_chips_count')) == int(num3), 'recently added count mismatch'


@when('the user clicks on a <suggestion_chip>')
def click_on_home_page_suggestion_chip(search_page, suggestion_chip):
    if suggestion_chip == 'suggestionchip1':
        gl_var.searchquery = search_page.findelement('home_page_captions_loc','suggestion_chip1').get_attribute('title')
        search_page.click_search_element('home_page_captions_loc','suggestion_chip1')
    elif suggestion_chip == 'suggestionchip2':
        gl_var.searchquery = search_page.findelement('home_page_captions_loc', 'suggestion_chip2').get_attribute('title')
        search_page.click_search_element('home_page_captions_loc','suggestion_chip2')
    elif suggestion_chip == 'suggestionchip3':
        gl_var.searchquery = search_page.findelement('home_page_captions_loc', 'suggestion_chip3').get_attribute('title')
        search_page.click_search_element('home_page_captions_loc','suggestion_chip3')

    print("The suggestion chip caption was -: " + gl_var.searchquery)


@then('verify that the search bar contains the search query text')
def verify_search_bar_contents(search_page):
    time.sleep(5)
    assert search_page.findelement('search_input_loc','search_input').get_attribute("value") == gl_var.searchquery, 'No text or wrong text in search bar'


@given('the user clicks on the grader handle')
def click_grader_handle(search_page):
    print("Name of first document : " + search_page.get_element_text('document_details_loc','document_name'))
    search_page.click_search_element('slider_locs','number_three_setting')
    time.sleep(5)


@when('user clicks on the Submit button')
def click_grader_submit_button(search_page):
    search_page.click_search_element('training_buttons_loc', 'submit_button')
    time.sleep(3)


@when('user clicks on the Reset button')
def click_grader_reset_button(search_page):
    search_page.click_search_element('training_buttons_loc', 'reset_button')
    time.sleep(5)


@then('verify that the slider handle is at position Na')
def verify_slider_handle_position(search_page):
    assert int(search_page.findelement('slider_locs','slider_bar').get_attribute("aria-valuenow")) == 0, 'slider handle not at position 0'


@given('the user clears the search bar')
def clear_search_bar(search_page):
    # search_page.findelement('search_input_loc', 'search_input').clear()
    search_page.findelement('search_input_loc', 'search_input').send_keys(Keys.CONTROL, 'a')
    time.sleep(5)
    search_page.findelement('search_input_loc', 'search_input').send_keys(Keys.BACKSPACE)
    time.sleep(10)
