"""
This file stores the key value pair for locators used in the Dashboard Page class.
"""

from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    """
    Locators for the Search Page.

    """
    column_locs = {
        'no_of_users_title': (By.XPATH, "//tr[@class='table-head']//th[2]"),
        'no_of_queries_title': (By.XPATH, "//tr[@class='table-head']//th[3]"),
        'no_of_downloads_title': (By.XPATH, "//tr[@class='table-head']//th[4]"),
        'no_of_downloads_on_first_page_title': (By.XPATH, "//tr[@class='table-head']//th[5]"),
        'no_of_ratings_received_title': (By.XPATH, "//tr[@class='table-head']//th[6]"),
        'average_query_time_title': (By.XPATH, "//tr[@class='table-head']//th[7]"),
        'no_accepted_suggestions_title': (By.XPATH, "//tr[@class='table-head']//th[8]")
    }

    row_locs = {
        'today_title': (By.XPATH, "//div[@class='tableClass']//tbody//tr[1]//td[1]"),
        'this_week_title': (By.XPATH, "//div[@class='tableClass']//tbody//tr[2]//td[1]"),
        'last_week_title': (By.XPATH, "//div[@class='tableClass']//tbody//tr[3]//td[1]"),
        'this_month_title': (By.XPATH, "//div[@class='tableClass']//tbody//tr[4]//td[1]"),
        'last_month_title': (By.XPATH, "//div[@class='tableClass']//tbody//tr[5]//td[1]"),
        'this_year_title': (By.XPATH, "//div[@class='tableClass']//tbody//tr[6]//td[1]"),
        'single_row_loc': (By.XPATH, "//div[@class='tableClass']//tbody//tr"),
        'single_cell_loc': (By.XPATH, "//div[@class='tableClass']//tbody//tr//td//span//strong")
    }

    queries_loc = {
        'recent_queries_label': (By.XPATH, "//div[@class='row']//div[@class='tagClass'][1]//div[@class='card-body']//div[@class='card-title card-title h5']"),
        'trending_queries_label': (By.XPATH, "//div[@class='row']//div[@class='tagClass'][2]//div[@class='card-body']//div[@class='card-title card-title h5']"),
        'recent_queries_items': (By.XPATH, "//div[@class='row']//div[@class='tagClass'][1]//div[@class='card-body']//p[@class='card-text']//div[@class='ui label']"),
        'trending_queries_items': (By.XPATH, "//div[@class='row']//div[@class='tagClass'][2]//div[@class='card-body']//p[@class='card-text']//div[@class='ui label']")
    }

    dashboard_title_loc = {
        'dashboard_title': (By.XPATH, "//div[@class='dashboard-title']")
    }
