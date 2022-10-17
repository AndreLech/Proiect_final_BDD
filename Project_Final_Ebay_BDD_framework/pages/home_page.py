from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class Home_page(Base_page):
    SEARCH_TEXT_BOX = (By.ID, "gh-ac")
    SEARCH_BUTTON   = (By.ID, "gh-btn")
    SEARCH_RESULTS  = (By.XPATH, '//h1/span[@class="BOLD"]')
    CATEGORY_DROPDOWN = (By.ID,"gh-cat")
    ADVANCED_SEARCH_LINK=(By.LINK_TEXT, "Advanced")
    # #ADVANCED_SEARCH_LINK = (By.ID, "gh-as-a")
    CONTINUA_BTN = (By.ID, 'sgnBt')
    PRODUCT = (By.XPATH, "//*[@id='gh-ac']")
    SELECT_PRODUCT= (By.XPATH, '//*[@id="srp-river-results"]/ul/li[2]/div/div[2]/a/div/span')
    ADD_CART = (By.XPATH, '//*[@id="isCartBtn_btn"]')
    CART = (By.XPATH, '//*[@id="gh-cart-n"]')
    REMOVE = (By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[1]/div/ul/li/div[1]/div/div/div[2]/span[2]/button')
    STRAT_SHOP = (By.XPATH, '//*[@id="mainContent"]/div/div[3]/div/div/div[3]/a[2]')




    def navigate_to_home_page(self):
        self.chrome.get('https://www.ebay.com/')

    #adaugare home page Ebay_advanced
    def navigate_to_advanced_home_page(self):
        self.chrome.get('https://www.ebay.com/sch/ebayadvsearch')

    def set_product_search(self):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("1dx mark")

#reinnterpretare a def-ului de mai sus pt a se putea folosi orice se produs se doreste, sa nu mai fie hardcodat
    def set_product_serch_with_parameter(self, product):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        sleep(5)

    def check_search_results(self):
        result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final = result_list[0].text.replace(',', '')
        assert int(resultat_final) > 1
        sleep(5)

    def set_product_search_with_parameter(self,product):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product)
        sleep(5)

    def check_search_results_with_parameters(self,number_of_results):
        result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final=result_list[0].text.replace(',', '')
        assert int(resultat_final) >= int(number_of_results)
        sleep(5)

    def choose_category(self,category):
        category_dropdown = Select(self.chrome.find_element(*self.CATEGORY_DROPDOWN))
        category_dropdown.select_by_visible_text(category)
        sleep(5)

    def click_advanced_search_link(self):
        self.chrome.find_element(*self.ADVANCED_SEARCH_LINK).click()


######## Feature: Select Product and add to cart

  # @TC1_select_product
    def set_product_search_product_snail(self):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("Snail Mucin")

    def select_product_snail(self):
        list=self.chrome.find_elements(*self.SELECT_PRODUCT)
        list[0].click()
        sleep(7)

    def add_to_cart(self):
        self.chrome.find_element(self.chrome.find_element(By.XPATH, '//*[@id="isCartBtn_btn"]'))
        snail = self.chrome.find_element(*self.ADD_CART)
        snail.click()
        sleep(15)

    def click_cart_button(self):
        button=self.chrome.find_element(*self.CART)
        button.click()
        sleep(7)

    def remove_from_cart(self):
        self.chrome.find_element(*self.REMOVE).click()
        sleep(7)

    def continue_shop(self):
        shop=self.chrome.find_element(*self.STRAT_SHOP)
        shop.click()







