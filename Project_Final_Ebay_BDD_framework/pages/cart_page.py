from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class CartPage(Base_page):
    SUBTOTAL = (By.XPATH, '(//*[@id="mainContent"]/div/div[4]/div/div[2]/div[4]/div[2]/span/span/span)[1]')
    REMOVE_FROM_CART= (By.XPATH, '(//*[@id="mainContent"]/div/div[3]/div[1]/div/ul/li/div[1]/div/div/div[2]/span[2]/button)')
    COSUL_TAU_ESTE_GOL_MSG = (By.XPATH, '/*[@id="mainContent"]/div/div[3]/div/div/div[1]/span/span/span')
    CHECKOUT_BTN = (By.XPATH, '(//*[@id="mainContent"]/div/div[4]/div/div[1]/button')

    def total_price(self, expected_price):
        self.chrome.find_element(*self.SUBTOTAL).text

    def click_remove_link(self):
        self.wait_and_click_elem_by_selector(*self.REMOVE_FROM_CART)

    def verify_empty_cart_msg(self):
        self.verify_element_is_displayed_by_selector(*self.COSUL_TAU_ESTE_GOL_MSG)

    def click_checkout_btn(self):
        self.wait_and_click_elem_by_selector(*self.CHECKOUT_BTN)



