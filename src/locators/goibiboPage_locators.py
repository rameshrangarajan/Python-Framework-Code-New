from selenium.webdriver.common.by import By


class GoibiboPageLocators(object):
    """
    Locators for the Search Page.

    """
    from_input_loc = {
        'from_input': (By.ID, 'gosuggest_inputSrc')
    }

    from_select_loc = {
        'from_select_value': (By.XPATH, "//*[. = 'Mumbai, India']")
    }

    destination_input_loc = {
        'dest_input': (By.ID, 'gosuggest_inputDest')
    }

    dest_select_loc = {
        'dest_select_value': (By.XPATH, "//*[. = 'Pune, India']")
    }

    departure_date_loc = {
        'departure_date_value': (By.XPATH, "//div[@class='DayPicker-Body']//div[@class='DayPicker-Week'][2]//div["
                                           "@class='DayPicker-Day'][4]")
    }

    return_calendar_loc = {
        'return_calendar': (By.ID, 'returnCalendar')
    }

    return_date_loc = {
        'return_date_value': (By.XPATH, "//div[@class='DayPicker-Body']//div[@class='DayPicker-Week'][3]//div["
                                        "@class='DayPicker-Day'][6]")
    }

    search_button_loc = {
        'search_button': (By.ID, 'gi_search_btn')
    }

    fare_calendar_label_loc = {
        'fare_calendar_label': (By.XPATH, "//div[@class='fb curPointFlt quicks ico14']")
    }

    book_button_loc = {
        'book_button': (By.XPATH, "//input[@value='BOOK']")
    }
