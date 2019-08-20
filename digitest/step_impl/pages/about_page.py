from selenium.webdriver.common.by import By
from step_impl.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AboutUsPageLocators():
    MEET_MORE_OF_OUR_TEAM   = (By.XPATH, "//a[text()='Meet More of Our Team']")
    LINKEDIN_PAGE           =   "https://www.linkedin.com/company/18118689/"

class AboutUsPage(BasePage, AboutUsPageLocators):

    def click_meet_more_of_our_team(self):
        self.click(AboutUsPageLocators.MEET_MORE_OF_OUR_TEAM)
        WebDriverWait(self.driver, 100).until(EC.url_changes(AboutUsPageLocators.LINKEDIN_PAGE))

        
