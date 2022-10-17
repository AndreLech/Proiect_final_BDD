

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser
import unittest

class Base_page(Browser, unittest.TestCase):
    pass

class Login_page(Browser, unittest.TestCase):
    pass

