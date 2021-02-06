@download_functionality @regression @training
Feature: Test cases for download file scenarios

@tc_download_func-1 @sanity
Scenario Outline: Verify Downloads count increases
    Given the user logs into the application
    And the user enter adcolony into search text box
    When the user clicks on search button
    And the user clicks on Download button for first result
    And the user clicks on search button
    Then verify download count increases and is displayed


@tc_download_func-2
Scenario Outline: Verify Downloads count from preview increases
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    And the user clicks on the preview button of first result
    When the user clicks on Download button in the preview popup
    And the user clicks on search button
    Then verify download count increases and is displayed

    Examples:
    | search_string |
    | adcolony    |
