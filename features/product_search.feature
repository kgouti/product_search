# Created by KARTIK at 04-05-2022
Feature: Rakuten product search
  # Enter feature description here

  Scenario: create a new user
    Given user opens rakuten url for registration
    When user enters valid details
    And user is registered successfully
    Then search box is displayed on landing page

  Scenario: Verify search url contains keyword "search-results"
    Given user logs into rakuten profile
    When iphone is searched in the search text box
    Then verify that new page url contains keyword search-results

  Scenario: Print seller and price of each product to console
    Given user logs into rakuten profile
    When iphone is searched in the search text box
    Then verify price is available for each card
    And print seller and the price of each product