from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def wait(self, element):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))

    def click(self, element):
        self.wait(element)
        self.driver.find_element(*element).click()

    def set(self, element, value):
        self.wait(element)
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(element))
    #     def get_element(self, element, wait=15):
    #     return WebDriverWait(self.driver, wait).until(lambda driver: self.driver.find_element(*element))

    # def click(self, element, use_action_chains=False):
    #     self.get_element(element).click()