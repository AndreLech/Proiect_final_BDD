from unittest import skip

from behave import *

@given('Advanced Search Page: I am on Ebay advanced page')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()
    # context.home_page_object.navigate_to_advanced_home_page()

@when('Advanced Search Page: I click on the Advanced Search Link and I search for "{product_to_be_searched}"')
def step_impl(context,product_to_be_searched):
    context.home_page_object.click_advanced_search_link()
    context.advanced_page_object.set_product_search(product_to_be_searched)
    context.advanced_page_object.click_search_button_in_advanced()

# @then('Advanced Search Page: I get at least "{number_of_results}" results')
# def step_impl(context,number_of_results):
#     context.advanced_page_object.check_search_advanced_results(number_of_results)

@then('Advanced Search Page: I get at least 100 results')
def step_impl(context):
    context.advanced_page_object.check_search_results_advanced()

