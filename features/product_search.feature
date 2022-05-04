# Created by KARTIK at 04-05-2022
Feature: Rakuten product search
  # Enter feature description here

  Scenario: create a new user
    Given user opens rakuten url for registration
    When user enters valid details
    Then user is registered successfully

  Scenario: verify search text box is shown on landing page
    Given a registered rakuten user
    When login is successful
    Then search text box is shown

  Scenario: Verify search url contains keyword "search-results"
    Given user logs into rakuten profile
    When "iphone" is typed in the search text box
    And user presses enter button
    Then verify that new page url contains keyword "search-results"

  Scenario: Print seller and price of each product to console