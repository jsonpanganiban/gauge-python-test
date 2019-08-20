from getgauge.python import before_suite, after_suite
from selenium import webdriver
import os  
from selenium.webdriver.chrome.options import Options  
import platform

from step_impl.pages.home_page import HomePage
from step_impl.pages.digidojo_page import DigiDojoPage
from step_impl.pages.about_page import AboutUsPage


class PageFactory:
    driver = None
    home_page = None
    digidojo_page = None
    about_page = None
    
@before_suite
def init():
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    PageFactory.driver = webdriver.Chrome()
    PageFactory.home_page = HomePage(PageFactory.driver)
    PageFactory.digidojo_page = DigiDojoPage(PageFactory.driver)
    PageFactory.about_page = AboutUsPage(PageFactory.driver)

@after_suite
def close():
    PageFactory.driver.close()
    PageFactory.driver.quit()