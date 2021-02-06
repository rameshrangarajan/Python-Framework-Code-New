"""
This file stores the key value pair for locators used in the Search Page class.
"""

from selenium.webdriver.common.by import By


class SearchPageLocators(object):
    """
    Locators for the Search Page.

    """
    search_input_loc = {
        'search_input': (By.CSS_SELECTOR, '.react-autosuggest__input')
    }

    search_btn_loc = {
        'submit_search': (By.CSS_SELECTOR, '.btn.search-btn'),
    }


    search_text_loc = {
        'search_text': (By.CSS_SELECTOR, '.text-left.file-context:nth-child(1) strong:nth-child(1)'),
        'first_autosuggest_element': (By.CSS_SELECTOR, '#react-autowhatever-1--item-0 > div > span > span')
    }

    download_button_loc = {
        'btn_download': (By.XPATH,
                         "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][4]//button[@id='download-btn-click']")

    }

    download_button_preview_loc = {
        'btn_download': (By.XPATH,
                         "//div[@class='file-download']//a//img[@class='download-img']")

    }

    download_count_loc = {
        'download_count': (
        By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][3]//div[@class='text-left search-result-metadata col']//div[3]//span[2]")
    }

    profile_icon_loc = {
        'profile_icon': (
        By.XPATH, "//span[@class='justify-content-end navbar-text']//div[@class='dropdown ']//a//img[@title='User Profile']")
    }

    profile_username_loc = {
        'profile_username': (
        By.XPATH, "//div[@class='dropdown__content ']//ul//li[1]//div[1]")
    }

    profile_emailid_loc = {
        'profile_emailid': (
            By.XPATH, "//div[@class='dropdown__content ']//ul//li[1]//div[2]")
    }

    page_3_link_loc = {
        'page_three_link': (
            By.XPATH, "//ul[@class='pagination']//li[3]//a[contains(text(),'3')]")
    }

    page_2_link_loc = {
        'page_two_link': (
            By.XPATH, "//ul[@class='pagination']//li[2]//a[contains(text(),'2')]")
    }

    page_status = {
        'pagination_status': (
            By.XPATH, "//span[@class='page-count-range']")
    }

    next_page_link_loc = {
        'next_page_link': (
            By.XPATH, "//ul[@class='pagination']//li[8]//a[@title='Next']")
    }

    previous_page_link_loc = {
        'previous_page_link': (
            By.XPATH, "//ul[@class='pagination']//li[2]//a[@title='Previous']")
    }

    last_page_link_loc = {
        'last_page_link': (
            By.XPATH, "//ul[@class='pagination']//li[9]//a[@title='Last']")
    }

    first_page_link_loc = {
        'first_page_link': (
            By.XPATH, "//ul[@class='pagination']//li[1]//a[@title='First']")
    }

    preview_button_loc = {
        'preview_button': (
            By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][4]//div[@class='mt-2 btn-toolbar']//button[@class='btn btn-outline-primary preview-btn']")
    }

    like_dislike_loc = {
        'like_button': (
            By.XPATH, "//div[@id='PPT0']//img[@title='Like']"),

        'dislike_button': (
            By.XPATH, "//div[@id='PPT0']//img[@title='Dislike']")
    }

    like_dislike_count_loc = {
        'like_count': (
            By.XPATH, "//div[@id='PPT0']//span[@class='feedback-count mr-2']"),

        'dislike_count': (
            By.XPATH, "//div[@id='PPT0']//span[@class='feedback-count']")
    }

    preview_popup_locs = {
        'ppt_title': (
            By.XPATH, "//div[@class='modal-content']//div[1]//h5[@class='title-preview']"),

        'ppt_name': (
            By.XPATH, "//div[@class='modal-content']//div[2]//div[@class='file-download']//p[@class='title-fileName']"),

        'created_by': (
            By.XPATH, "//div[@class='col']//div[@class='justify-content-start mr-2 row'][1]//span"),

        'last_modified': (
            By.XPATH, "//div[@class='col']//div[@class='justify-content-start mr-2 row'][2]//span"),

        'slide_status': (
            By.XPATH, "//div[@class='col-sm-9']//div[@class='image-gallery-index']"),

        'occurrences_tiles': (
            By.XPATH, "//div[@class='occurence-div col-sm-3']//div[@class='thumbnail-list1']//img"),

        'download_count': (
            By.XPATH, "//div[@class='col col-lg-3 col']//div[@class='row']"
        ),
        'preview_close_button': (
            By.XPATH, "//div[@class='modal-content']//div//a[@title='Close']"
        )

    }

    document_details_loc = {
        'document_name': (
            By.XPATH, "//div[@id='PPT0']//div[@class='file-name float-left mb-2']"),
        'created_by': (
            By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][3]//div[@class='text-left search-result-metadata col'][1]//div[1]//span[@class='created-by-result']"),
        'modified_by': (
            By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][3]//div[@class='text-left search-result-metadata col'][1]//div[2]//span[@class='created-by-result']"),
        'created_date': (
            By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][3]//div[@class='text-left search-result-metadata col'][2]//div[1]"),
        'last_modified_date': (
            By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][3]//div[@class='text-left search-result-metadata col'][2]//div[2]"),

    }

    xoriant_icon_loc = {
        'xoriant_icon': (
            By.XPATH, "//a[@class='m-0 navbar-brand']")
    }

    landing_page_locs = {
        'landing_page_title': (
            By.XPATH, "//div[@class='col-sm-7']//div[@class='app-title mb-4']")
    }

    feedback_locs = {
        'feedback_sidebar': (
            By.XPATH, "//div[@id='feedback']//a"),
        'four_star_rating': (
            By.XPATH,
            "//div[@class='star-ratings']//div[@class='star-container'][4]"),
        'feedback_text_area': (
            By.XPATH,
            "//textarea[@class='form-control']"),
        'feedback_submit_button': (
            By.XPATH,
            "//button[@class='btn feedback-btn btn btn-primary btn-sm']"),
        'feedback_acknowledgement': (
            By.XPATH,
            "//div[@class='Toastify']//div[@class='Toastify__toast-container Toastify__toast-container--bottom-right']")

    }

    results_out_of_loc = {
        'results_out_of': (
            By.XPATH, "//div[@id='results-metadata']//div[@class='row-spacing col-sm-12']//span"),
    }

    suggestion_chip_loc = {
        'fifth_suggestion_chip': (
            By.XPATH, "//div[@class='file-info float-left col-sm-12']//div[@class='MuiButtonBase-root MuiChip-root float-left chip-style MuiChip-outlined MuiChip-clickable'][5]//span[1]"),
    }

    search_related_to_caption_loc = {
        'search_related_to': (
            By.XPATH,
            "//div[@class='search-related col-sm-12']"),
    }

    time_period_filter_loc = {
        'All_loc': (
            By.XPATH, "//div[@class='filter-div']//button[@class='btn btn-sm btn-light btn-custom active']"
        ),
        'thirty_days_loc': (
            By.XPATH, "//div[@class='filter-div']//button[@class='btn btn-sm btn-light btn-custom '][1]"
        ),

        'twelve_months_loc': (
            By.XPATH, "//div[@class='filter-div']//button[@class='btn btn-sm btn-light btn-custom '][2]"
        ),

        'three_years_loc': (
            By.XPATH, "//div[@class='filter-div']//button[@class='btn btn-sm btn-light btn-custom '][3]"
        )
    }

    results_section_loc = {
        'results_section': (
            By.XPATH, "//div[@class='container-fluid search-result-focus']//div[@class='search-result-focus']"
        )
    }

    no_results_error_message_loc = {
        'error_message': (
            By.XPATH, "//div[@id='root']//div[@class='App']//div[@class='alert alert-danger alert-margin']"
        )
    }

    search_bar_suggestions_loc = {
        'suggestions_list': (
            By.XPATH, "//ul[@class='react-autosuggest__suggestions-list']//li"
        ),
        'suggestions_root': (
            By.XPATH, "//ul[@class='react-autosuggest__suggestions-list']"
        )
    }

    thumbnail_loc = {
        'thumbnail_icon': (
            By.XPATH, "//div[@class='occurrences-thumbnail']//span[@class='img-space']//img[@class='mr-2 cust-img'][1]"
        ),
        'thumbnail_popup': (
            By.XPATH, "//div[@class='modal-content']//div[@class='modal-style modal-body']//img[@class='imgclass']"
        ),
        'thumbnail_close': (
            By.XPATH, "//div[@class='modal-content']//div//a[@title='Close']"
        )
    }

    third_occurrence_tile_loc = {
        'third_occurrence_tile': (
            By.XPATH, "//div[@class='occurence-div col-sm-3']//div[@class='thumbnail-list1']//img[@class='ml-2 mb-1 mr-2 img-cls'][3]"
        )
    }

    preview_popup_loc = {
        'preview_popup': (
            By.XPATH, "//div[@class='modal-content']"
        )
    }

    home_page_captions_loc = {
        'trending_searches': (
            By.XPATH, "//div[@class='query-row row']//div[@class='query-col col']//div[@class='trend-serach']"
        ),
        'topics': (
            By.XPATH, "//div[@class='query-row row']//div[@class=' query-col-2 col']//div[@class='trend-serach']"
        ),
        'recently_added': (
            By.XPATH, "//div[@class='query-row row']//div[@class='query-col-1 col']//div[@class='trend-serach']"
        ),
        'trending_searches__chips_count': (
            By.XPATH, "//div[@class='query-row row']//div[@class='query-col col']//div[@class='ui label trend-queries']"
        ),
        'topics_chips_count': (
            By.XPATH, "//div[@class='query-row row']//div[@class=' query-col-2 col']//div[@class='ui label trend-queries']"
        ),
        'recently_added_chips_count': (
            By.XPATH, "//div[@class='query-row row']//div[@class='query-col-1 col']//div[@class='ui label trend-queries']"
        ),
        'suggestion_chip1': (
            By.XPATH, "//div[@class='query-row row']//div[@class='query-col col']//div[@class='ui label trend-queries'][1]"
        ),
        'suggestion_chip2': (
            By.XPATH,
            "//div[@class='query-row row']//div[@class=' query-col-2 col']//div[@class='ui label trend-queries'][1]"
        ),
        'suggestion_chip3': (
            By.XPATH,
            "//div[@class='query-row row']//div[@class='query-col-1 col']//div[@class='ui label trend-queries'][1]"
        )
    }

    first_document_loc = {
            'first_doc': (
                By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']"
            )
        }

    last_document_loc = {
        'last_doc': (
            By.XPATH, "//div[@id='PPT9']//div[@class='col-sm-5']"
        )
    }

    slider_locs = {
        'number_three_setting': (
            By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][4]//div[@class='col-sm-7']//div[@class='col-space col-sm-10']//div[@class='rangeslider rangeslider-horizontal slider-cust-class mt-3']//ul[@class='rangeslider__labels']//li[@data-value='3']"
        ),
        'slider_bar': (
            By.XPATH, "//div[@id='PPT0']//div[@class='col-sm-5']//div[@class='file-info row'][4]//div[@class='col-sm-7']//div[@class='col-space col-sm-10']//div[@class='rangeslider rangeslider-horizontal slider-cust-class mt-3']"
        )
    }

    training_buttons_loc = {
        'submit_button': (
            By.XPATH, "//div[@class='footer-div']//div//button[contains(text(),'Submit')]"
        ),
        'reset_button': (
            By.XPATH, "//div[@class='footer-div']//div//button[contains(text(),'Reset')]"
        )
    }
