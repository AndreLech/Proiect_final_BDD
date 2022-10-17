Feature: Testing scenarios on ebay.com
#  Background:
#    Given Home Page: I am on Ebay homepage
#    Then Home Page: I have at least 2 results returned

  @T1
  Scenario: Searching product on Ebay home page
    Given Home Page: I am on Ebay homepage
    When Home Page: I search an item
    Then Home Page: I have at least 2 results returned

  @T2 @parameter
  Scenario:
    Given Home Page: I am on Ebay homepage
    When Home Page: I search for "Crescendo" in "Books"
    Then Home Page: I have at least 2 results returned

  @T3 @outline, @parameter
  Scenario Outline:
    Given Home Page: I am on Ebay homepage
    When Home Page: I search for "<product_name>" in "<category_name>"
    Then Home Page: I have at least "<number_of_results>" results returned
    Examples:
      | product_name                                                                    | category_name        | number_of_results |  |
      | becca fitzpatrick                                                               | Books                | 1000              |  |
      | omega                                                                           | All Categories       | 1000              |  |
      | VINTAGE OMEGA SEAMASTER                                                         | All Categories       | 200               |  |



######## Feature: Select Product and add to cart

  @TC1_select_product @shop
  Scenario: Add to cart one product
    Given Home Page: I am on Ebay homepage
    When Home Page: I have searched the "Snail Mucin" product
    Then Home Page: I add product to basket

  @TC2_remove_product_negative_scenario_on_return_to_shop @shop
  Scenario: Remove the product from cart
    Given Home Page: I verify that I have the product in my cart
    When Home Page: I delete the product
    Then Home Page: I start shoping again

