import time
import Data.providers as dp
from playwright.sync_api import Page, expect, Playwright, sync_playwright

def get_by_label(page, label):
    element = page.locator(f"xpath=//label[text()='{label}']/../..//input")
    return (element)
class LoginPage:
    def __init__(self, page):
        self.page = page
    def login(self, username, password):
        page= self.page
        page.goto("https://opensource-demo.orangehrmlive.com")
        page.get_by_role("textbox", name="Username").fill(username)
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Login").click()
    def check_pim_menu(self):
        page = self.page
        expect(page.locator("a[href*='/pim/viewPimModule']")).to_have_text("PIM")

class AddEmployeePage:
    def __init__(self, page):
        self.page = page
        self.emp = dp.employee()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        page.get_by_role("link", name="PIM").click()
        page.get_by_role("button", name="Add").click()
        page.get_by_role("textbox", name="First Name").fill(self.emp.first_name)
        page.get_by_role("textbox", name="Last Name").fill(self.emp.last_name)
        get_by_label(page, 'Employee Id').fill(self.emp.id)
        page.get_by_role("button", name="Save").click()
        expect(page.get_by_text(f"{self.emp.first_name} {self.emp.last_name}")).to_be_visible()

    def employee_details (self, last_name, first_name):
        page = self.page
        page.get_by_role("link", name="PIM").click()
        get_by_label(page, 'Employee Name').click()
        time.sleep(0.2)
        get_by_label(page, 'Employee Name').type(last_name)
        time.sleep(0.2)
        page.get_by_role("button", name="Search").click()
        page.locator("div.orangehrm-employee-list").locator("div[role='rowgroup']").nth(1).locator(
            "div[role='cell']").nth(2).click()
        expect(page.get_by_text(f"{first_name} {last_name}")).to_be_visible()
        page.locator("xpath=//label[text()='Nationality']/../..//i").click()
        page.locator("div[role='listbox']").get_by_text("French").click()
        page.locator("xpath=//label[text()='Marital Status']/../..//i").click()
        page.locator("div[role='listbox']").get_by_text("Single").click()
        date_of_birth = page.locator("xpath=//label[text()='Date of Birth']/../..").get_by_placeholder("yyyy-dd-mm")
        date_of_birth.fill(self.emp.birthday)
        page.locator("xpath=//label[text()='Male']").click()
        page.get_by_role("button", name="Save").nth(0).click()

    def logout (self):
        page= self.page
        page.locator("p.oxd-userdropdown-name").click()
        page.get_by_role("menuitem", name="Logout").click()
        expect (page.get_by_role("textbox", name="Username")).to_be_visible()

