@basic_search @regression @training
Feature: Test cases for basic search scenarios

@tc_basic_search-1
Scenario Outline: Search for different terms
    Given the user logs into the application
    And the user enter <search_string> into search text box
    When the user clicks on search button
    Then the search bar contains the text xoriant

    Examples:
    | search_string |
    | xoriant     |

@tc_basic_search-2
Scenario Outline: Verify username and emailid after logging in
    Given the user logs into the application
    When the user clicks on the Profile icon
    Then verify result is displayed with <search_string1> and <search_string2>

    Examples:
    | search_string1          | search_string2                |
    | Ramesh Rangarajan       | Ramesh.Rangarajan@Xoriant.Com |

@tc_basic_search-3 @sanity
Scenario Outline: Traverse to a different page
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    When the user clicks on page 3 link
    Then verify page status as <page_status>

    Examples:
    | search_string | page_status |
    | iot           | 21-30 of    |

@tc_basic_search-4 @sanity
Scenario Outline: Traverse to next page
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    When the user clicks on next page link
    Then verify page status as <page_status>

    Examples:
    | search_string | page_status |
    | iot           | 11-20 of    |

@tc_basic_search-5
Scenario Outline: Traverse to previous page
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    And the user clicks on next page link
    When the user clicks on the previous page link
    Then verify page status as <page_status>

    Examples:
    | search_string | page_status |
    | iot           | 1-10 of     |

@tc_basic_search-6
Scenario Outline: Traverse to last page
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    When the user clicks on the last page link
    Then verify page status as <page_status>

    Examples:
    | search_string | page_status |
    | iot           | of          |

@tc_basic_search-7
Scenario Outline: Traverse to first page
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    And the user clicks on next page link
    When the user clicks on the first page link
    Then verify page status as <page_status>

    Examples:
    | search_string | page_status |
    | iot           | 1-10 of     |

@tc_basic_search-8 @sanity
Scenario Outline: Like/Dislike functionality
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    And the Like button for first result is enabled or the dislike button is enabled
    When the user clicks on the Like or dislike link
    Then verify like count status or dislike count status

    Examples:
    | search_string |
    | everbridge    |

@tc_basic_search-9 @sanity
Scenario Outline: Verify Preview popup contents
    Given the user logs into the application
    And the user enter <search_string> into search text box
    And the user clicks on the search button
    And the user clicks on the preview button of first result
    Then verify slide title as <ppt_title>
    And verify slide name as <ppt_name>
    And verify created by as <created_by>
    And verify last modified as <last_modified>
    And verify slide number status as <slide_status>
    And verify number of occurrences tiles as <number_occurrences_tiles>
    And verify that the download count in the preview popup is a number

    Examples:
    | search_string | ppt_title                           | ppt_name                                     | created_by                      | last_modified                           | slide_status | number_occurrences_tiles |
    | adcolony      | Xoriants Presentation for AdColony  | Xoriants Presentation for AdColony.pptx      | Created By :   Nikeetaa Mhaatre | Last Modified :  3/11/2019, 7:14:29 AM  | 1 of 22      | 4                        |


@tc_basic_search-10
Scenario Outline: Verify document details
    Given the user logs into the application
    And the user enter adcolony into search text box
    And the user clicks on the search button
    When the document Xoriants Presentation for AdColony is displayed as first result
    Then verify that created by is Nikeetaa Mhaatre
    And verify that modified by is Shishir Rode
    And verify that created date is Created Date :  6/1/2018, 6:36:15 AM
    And verify that last modified date is Last Modified :  3/11/2019, 7:14:29 AM


@tc_basic_search-11
Scenario Outline: Verify user is directed to landing page on clicking on the Xoriant icon
    Given the user logs into the application
    And the user enter everbridge into search text box
    And the user clicks on the search button
    When the user clicks on the Xoriant icon
    Then verify that the landing page with title as Knowledge Management Portal is displayed


@tc_basic_search-12 @sanity
Scenario Outline: Verify user is able to submit subjective feedback and the acknowledgement is seen
    Given the user logs into the application
    And the user enter everbridge into search text box
    And the user clicks on the search button
    When the user clicks on the Feedback sidebar
    And the user selects a rating
    And the user enters some feedback text like Good article!
    And the user clicks on the Submit button
    Then verify that the message Thank You. You have successfully submitted your feedback! appears


@tc_basic_search-13
Scenario Outline: Verify that a number appears before and after the caption results out of
    Given the user logs into the application
    And the user enter aws into search text box
    And the user clicks on the search button
    Then verify that a number appears before and after the caption results out of

@tc_basic_search-14 @sanity
Scenario Outline: Verify clicking on suggestion chip functionality
    Given the user logs into the application
    And the user enter aws into search text box
    And the user clicks on the search button
    When the user clicks on the fifth suggestion chip
    Then the search bar contains the suggestion chip text
    And the Search related to caption shows the suggestion chip text

@tc_basic_search-15
Scenario Outline: Verify search by pressing enter key of keyboard
    Given the user logs into the application
    And the user enter aws into search text box
    When the user presses the enter key of the keyboard
    Then verify page status as <page_status>

    Examples:
    | page_status |
    | 1-10 of     |

@tc_basic_search-16 @sanity
Scenario Outline: Verify search by clicking on the time period filter buttons
    Given the user logs into the application
    And the user enter aws into search text box
    And the user clicks on the search button
    When the user clicks on the <time_period>
    Then verify results count status or error message as Sorry! we could not find any search result for this term. Please try something else.

    Examples:
    | time_period   |
    | All           |
    | thirty days   |
    | twelve months |
    | three years   |

@tc_basic_search-17
Scenario Outline: Verify that when some text is typed into the search bar, some suggestions appear
    Given the user logs into the application
    And the user enter aws into search text box
    Then verify that one or more suggestions appear

@tc_basic_search-18
Scenario Outline: Verify that the thumbnail popup opens up on clicking on it
    Given the user logs into the application
    And the user enter everbridge into search text box
    And the user clicks on the search button
    When the user clicks on the first thumbnail of first result
    Then verify that the thumbnail opens up

@tc_basic_search-19
Scenario Outline: Verify that the correct slide appears on clicking on an occurrence tile in Preview popup
    Given the user logs into the application
    And the user enter adcolony into search text box
    And the user clicks on the search button
    And the user clicks on the preview button of first result
    When user clicks on the third occurrence tile
    Then verify slide number status as 18 of 22

@tc_basic_search-20
Scenario Outline: Verify that the Preview popup closes on pressing the Escape key
    Given the user logs into the application
    And the user enter everbridge into search text box
    And the user clicks on the search button
    And the user clicks on the preview button of first result
    When the user presses the escape key of the keyboard
    Then verify that the preview popup is closed

@tc_basic_search-21
Scenario Outline: Verify that the Preview popup closes on clicking the Close button
    Given the user logs into the application
    And the user enter everbridge into search text box
    And the user clicks on the search button
    And the user clicks on the preview button of first result
    When the user clicks the Close button of the preview popup
    Then verify that the preview popup is closed

@tc_basic_search-22
Scenario Outline: Verify that the thumbnail popup closes on pressing the Escape key
    Given the user logs into the application
    And the user enter everbridge into search text box
    And the user clicks on the search button
    When the user clicks on the first thumbnail of first result
    And the user presses the escape key of the keyboard
    Then verify that the thumbnail popup is closed

@tc_basic_search-23
Scenario Outline: Verify that the thumbnail popup closes on clicking the Close button
    Given the user logs into the application
    And the user enter everbridge into search text box
    And the user clicks on the search button
    When the user clicks on the first thumbnail of first result
    And the user clicks the Close button of the thumbnail popup
    Then verify that the thumbnail popup is closed

@tc_basic_search-24
Scenario Outline: Verify that the Trending Searches, Topics and Recently Added captions appear on the home page
    Given the user logs into the application
    Then verify that Trending Searches : and Topics : and Recently Added : captions appear on home page

@tc_basic_search-25
Scenario Outline: Verify number of chips for the Trending Searches, Topics and Recently Added sections on the home page
    Given the user logs into the application
    Then verify on home page that Trending Searches has 15 chips and Topics has 15 chips and Recently added has 10 chips

@tc_basic_search-26 @sanity
Scenario Outline: Verify that when suggestion chips on home page are clicked the results page opens up
    Given the user logs into the application
    When the user clicks on a <suggestion_chip>
    Then verify that the search bar contains the search query text

    Examples:
    | suggestion_chip   |
    | suggestionchip1   |
    | suggestionchip2   |
    | suggestionchip3   |

@tc_basic_search-27
Scenario Outline: Verify error message appears on conducting search when the search bar is empty
     Given the user logs into the application
     And the user enter everbridge into search text box
     And the user clicks on the search button
     And the user clears the search bar
     When the user clicks on search button
     Then verify that the error message Please enter a search key! appears

@tc_basic_search-28
Scenario Outline: Verify error message appears on conducting search for invalid search text
     Given the user logs into the application
     And the user enter everbridge into search text box
     And the user clicks on the search button
     And the user clears the search bar
     When the user enter hellooo into search text box
     And the user clicks on search button
     Then verify that the error message Sorry! we could not find any search result for this term. Please try something else. appears
