@google_search @tests
Feature: Test cases for google search scenarios

@tc_google_search-1 @sanity
Scenario Outline: Search for different
    Given the user opens the Google website
    And the user enter <search_string> into search text box
    When the user presses the enter key
    Then the new page contains the text <result_string>

    Examples:
    | search_string | result_string      |
    | selenium      | Selenium WebDriver |


@tc_google_search-2 @regression
Scenario Outline: Search for different terms
    Given the user opens the Google website
    And the user enter <search_string> into search text box
    When the user selects the option selenium tutorial
    Then the new page contains the text <result_string>

    Examples:
    | search_string | result_string                                               |
    | selenium      | Selenium Tutorial for Beginners: Learn WebDriver in 7 Days  |