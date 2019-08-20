from selenium.webdriver.common.by import By
from step_impl.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DigiDojoLocators():
    REGISTER_TODAY      = (By.XPATH, "//span[contains(text(), 'Register Today')]")
    NEW_FORM            = (By.XPATH, "//div[@class='form-title' and text()='New Form']")
    GIVEN_NAME          = (By.XPATH, "//input[@x-autocompletetype='given-name']")
    SURNAME             = (By.XPATH, "//input[@x-autocompletetype='surname']")
    COUNTRY_CODE        = (By.XPATH, "//input[@x-autocompletetype='phone-country-code']")
    AREA_CODE           = (By.XPATH, "//input[@x-autocompletetype='phone-area-code']")
    PHONE_PREFIX        = (By.XPATH, "//input[@x-autocompletetype='phone-local-prefix']")
    PHONE_SUFFIX        = (By.XPATH, "//input[@x-autocompletetype='phone-local-suffix']")
    PHONE_EMAIL         = (By.NAME, "email")

class DigiDojoPage(BasePage, DigiDojoLocators):

    def register(self):
        self.click(DigiDojoLocators.REGISTER_TODAY)
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(DigiDojoLocators.NEW_FORM))
        self.set(DigiDojoLocators.SURNAME, "Panganiban")
        self.set(DigiDojoLocators.GIVEN_NAME, "Jayson")
        self.set(DigiDojoLocators.COUNTRY_CODE, "63")
        self.set(DigiDojoLocators.PHONE_EMAIL, "Jayson.Panganiban@digibpl.com")

