#
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from pages.base_page import Base_page
#
# class Home_page(Base_page):
#     SEARCH_TEXT_BOX = (By.ID, "gh-ac")
#     SEARCH_BUTTON   = (By.ID, "gh-btn")
#     SEARCH_RESULTS  = (By.XPATH, '//h1/span[@class="BOLD"]')
#     # CATEGORY_DROPDOWN = (By.ID,"gh-cat")
#     # ADVANCED_SEARCH_LINK=(By.LINK_TEXT, 'Advanced')
#
#
#     def navigate_to_home_page(self):
#         self.chrome.get('https://www.ebay.com/')
#
#     def set_product_search(self):
#         self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("Iphone")
#
#
# #reinnterpretare a def-ului de mai sus pt a se putea folosi orice se produs se doreste, sa nu mai fie hardcodat
#     def set_product_serch_with_parameter(self, product):
#         self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product)
#
#     def click_search_button(self):
#         self.chrome.find_element(*self.SEARCH_BUTTON).click()
#         sleep(3)
#
#     def check_search_results(self):
#         result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
#         resultat_final = result_list[0].text.replace(',', '')
#         assert int(resultat_final) > 1
#         sleep(3)
# from time import sleep
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from pages.base_page import Base_page
#
# class Advanced_search_page(Base_page):
#     SEARCH_TEXT_BOX =(By.ID,"_nkw")
#     SUBMIT_SEARCH_BUTTON = (By.XPATH,"//div/button[@type='submit']")
#     # SEARCH_RESULTS = (By.XPATH, '//h1/span[@class="rcnt"]') --for IPhone
#     SEARCH_RESULTS = (By.XPATH, '//h1/span[@class="BOLD"]') # for Samsung Fold
#
# def check_search_advanced_results(self, number_of_results):
#     result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
#     print(f'{result_list}')
#     resultat_final = result_list[0].text.replace(',', '')
#     assert int(resultat_final) > int(number_of_results)

