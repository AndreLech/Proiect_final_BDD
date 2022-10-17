from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class Login_page(Base_page):

    # #PASSWORD_INPUT = (By.ID, 'pass')
    # #CONTINUA_BTN = (By.ID, 'sgnBt')
    # #LOGO_IMG = (By.XPATH, '//*[@id="gh-logo]')
    # #ERROR_MSG = (By.ID, 'errormsg')


    def nav_home_page(self):
        self.chrome.get('https://www.ebay.com/')



    # def navigate_to_login_page(self):
    #     self.chrome.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2Fmys%2Fhome%3Fsource%3DGBH')

    # def set_email(self, email):
    #     self.chrome.find_element(*self.EMAIL_INPUT, email)

    # def set_password(self, email):
    #     self.chrome.find_element(*self.PASSWORD_INPUT, email)

    # def click_continua_btn(self):
    #     self.chrome.find_element(*self.CONTINUA_BTN)

    # def click_logo_img(self):
    #     self.chrome.find_element(*self.LOGO_IMG).click()
    #     self.chrome.find_element(*self.CHECK_BOX).click()
    #
    # def verify_error_msg(self):
    #     self.chrome.find_element(*self.ERROR_MSG)






