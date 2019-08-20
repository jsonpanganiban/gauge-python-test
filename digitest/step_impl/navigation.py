from getgauge.python import step, DataStoreFactory
from step_impl.pages.page_factory import PageFactory

@step('Navigate to <page> Page')
def navigate(page):
    PageFactory.home_page.visit(page)

@step('Populate Registration')
def register():
    PageFactory.digidojo_page.register()

@step('Click Meet more of our team')
def linkedin_page():
    PageFactory.about_page.click_meet_more_of_our_team()