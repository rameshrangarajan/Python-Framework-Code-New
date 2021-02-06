@goibibo @tests
Feature: Test cases for goibibo scenarios

@tc_goibibo-1 @sanity
Scenario Outline: Search for different flights
    Given the user opens the goibibo website
    And the user enter <origin> into from text box
    And the user enter <destination> into destination text box
    And the user selects a departure date
    And the user selects a return date
    When the user clicks the search button
    Then the new page contains the text Fare Calendar
    And the book button is displayed and enabled

    Examples:
    | origin | destination |
    | mumbai | pune        |