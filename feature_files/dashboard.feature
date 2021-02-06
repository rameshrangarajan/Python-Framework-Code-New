@dashboard @regression
Feature: Test cases for dashboard scenarios

@tc_dashboard-1
Scenario Outline: Verify dashboard screen opens up and it has all columns
    Given the user logs into the dashboard
    Then verify that the columns No. of Users , No. of Queries , No. of Downloads , Downloads on 1st Page , Ratings Received , Avg. Query Time (s) and No. of accepted suggestions exist

@tc_dashboard-2
Scenario Outline: Verify dashboard screen opens up and it has all rows
    Given the user logs into the dashboard
    Then verify that the rows Today : , This Week : , Last Week : , This Month : , Last Month : and This Year : exist

@tc_dashboard-3
Scenario Outline: Verify that all cells in dashboard are non empty
    Given the user logs into the dashboard
    Then verify that all cells in the table are non empty

@tc_dashboard-4
Scenario Outline: Verify that the labels Recent Queries and Trending Queries are present and they are non empty
    Given the user logs into the dashboard
    Then verify the labels Recent Queries and Trending Queries are present
    And verify that the recent queries and trending queries sections are non empty and contain 15 items each

@tc_dashboard-5
Scenario Outline: Verify that the dashboard title appears on dashboard page
    Given the user logs into the dashboard
    Then verify that the caption Dashboard appears
