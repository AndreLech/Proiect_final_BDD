from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class Advanced_search_page(Base_page):
    SEARCH_TEXT_BOX =(By.ID,"_nkw")
    SUBMIT_SEARCH_BUTTON = (By.XPATH,"//div/button[@type='submit']")
    # SUBMIT_SEARCH_BUTTON = (By.XPATH,"//*[@id='adv_search_from'']")
    # SEARCH_RESULTS = (By.XPATH, '//h1/span[@class="rcnt"]') --for IPhone
    SEARCH_RESULTS = (By.XPATH, '//h1/span[@class="BOLD"]') # for Samsung Fold

    #adaugare home page Ebay_advanced
    def navigate_to_advanced_home_page(self):
        self.chrome.get('https://www.ebay.com/sch/ebayadvsearch')

    def set_product_search(self,product_to_be_searched):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product_to_be_searched)
        sleep(3)

    def click_search_button_in_advanced(self):
        self.chrome.find_element(*self.SUBMIT_SEARCH_BUTTON).click()
        sleep(3)

    def check_search_advanced_results(self, number_of_results):
        result_list2 = self.chrome.find_elements(*self.SEARCH_RESULTS)
        rezultat_final2 = result_list2.text.replace(',', '')
        assert int(rezultat_final2) > int(number_of_results)

    def check_search_results_advanced(self):
        list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        rezultat_final_advanced = list[0].text.replace(',', '')
        assert int(rezultat_final_advanced) > 100




