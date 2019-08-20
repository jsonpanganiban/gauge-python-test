from selenium.webdriver.common.by import By
from step_impl.pages.base_page import BasePage
from getgauge.python import step, DataStoreFactory
import time

class HomePageLocators():

    def get_navigation_xpath(self, navigation_item):
        return (By.XPATH, "//a[text()='{0}']".format(navigation_item))

class HomePage(BasePage, HomePageLocators):

    def visit(self, page):
        page = page.lower()
        if page == "digidojo":
            self.driver.get("https://www.digibpl.com/digidojo-en")
        elif page == "aboutus":
            self.driver.get("https://www.digibpl.com/about-en")
        else:
            self.driver.get("https://www.digibpl.com/")
    
    def navigate_to(self, navigation_item):
        elem =  self.get_navigation_xpath(navigation_item)
        self.click(elem)
