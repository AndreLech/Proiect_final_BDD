from behave import *
from selenium.webdriver.common.by import By


@given('Home Page: I am on Ebay homepage')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()

@when('Home Page: I search an item')
def step_impl(context):
    context.home_page_object.set_product_search()
    context.home_page_object.click_search_button()

@when('Home Page: I search for "{product_name}" in "{category_name}"')
def step_impl(context,product_name,category_name):
    context.home_page_object.set_product_search_with_parameter(product_name)
    context.home_page_object.choose_category(category_name)
    context.home_page_object.click_search_button()

@then('Home Page: I have at least 2 results returned')
def step_impl(context):
    context.home_page_object.check_search_results()

@then('Home Page: I have at least "{number_of_results}" results returned')
def step_impl(context,number_of_results):
    context.home_page_object.check_search_results_with_parameters(number_of_results)



######## Feature: Select Product and add to cart

  # @TC1_select_product
@when('Home Page: I have searched the "Snail Mucin" product')
def step_impl(context):
    context.home_page_object.set_product_search_product_snail()
    context.home_page_object.click_search_button()

@then('Home Page: I add product to basket')
def step_impl(context):
    context.home_page_object.select_product_snail()


  # @TC2_remove_product
@given('Home Page: I verify that I have the product in my cart')
def step_impl(context):
    var = context.home_page_object.navigate_to_home_page
    var = context.home_page_object.click_cart_button

@when('Home Page: I delete the product')
def step_impl(context):
    var = context.home_page_object.remove_from_cart

@then('Home Page: I start shoping again')
def step_impl(context):
    context.home_page_object.continue_shop()




