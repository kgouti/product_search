# Created by KARTIK at 04-05-2022
Feature: Rakuten product search

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

  Scenario: Searching a non existing product should return "No results found" message
  Scenario: Number of products displayed to be defaulted to 10 per page
  Scenario: Pagnation is implemented correctly, displaying correct no of products per page
  Scenario: Filter / sort mechanism should work appropriately
  Scenario: Seller information displayed online should match with the seller information on the backend
  Scenario: See all XXXX Products should actually display XXXX products when expanded
  Scenario: number of products on the left filter should match with numbers displayed in "See all XXXX Products"
