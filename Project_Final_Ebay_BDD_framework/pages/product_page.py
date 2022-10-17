from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class ProductsPage(Base_page):
    RESULTS_TITLE = (By.XPATH, '//*[@id="srp-river-results"]/ul/li[1]/div/div[2]/a/div/span')
    VEZI_DETALII_COS_BTN = (By.XPATH, '//*[@id="gh-minicart-hover-body"]/div/div/div[4]/div[2]/a')
    ADD_TO_CART = (By.ID, 'isCartBtn_btn')

    def verify_results_contain_text(self, text):
        title_list = self.chrome.find_elements(*self.RESULTS_TITLE)
        for i in range(5):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def click_vezi_detalii_cos(self):
        self.wait_and_click_elem_by_selector(*self.VEZI_DETALII_COS_BTN)

    def add_to_cart(self, ):
        self.chrome.find_element(self.ADD_TO_CART).click()
