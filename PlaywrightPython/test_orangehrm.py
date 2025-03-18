import Libs.plw_orangehrm as plw
from playwright.sync_api import Page, expect, Playwright
def test_a_orangehrm(page: Page):
    orm = plw.plw_orangehrm(page)
    orm.login("Admin", "admin123", "First Name Last Name")

    page.get_by_role("link", name="PIM").click()
    page.locator("xpath=//label[text()='Employee Name']/../..//input").click()
    page.locator("xpath=//label[text()='Employee Name']/../..//input").fill("IMHAH")
    page.get_by_role("button", name="Search").click()



    orm.logout()