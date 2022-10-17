

Feature: Check the search on the advanced search page
  @T1_advanced
  Scenario: Check that we can make a basic search in the advanced search page
    Given Advanced Search Page: I am on Ebay advanced page
    When Advanced Search Page: I click on the Advanced Search Link and I search for "Samsung Fold"
    Then Advanced Search Page: I get at least 100 results