import time

from playwright.sync_api import Page, expect, Playwright, sync_playwright
import random
from faker import Factory
fakerFR = Factory.create('fr_FR')

matricule = str(random.randrange (100000, 999999))
nom = fakerFR.last_name()
prenom = fakerFR.first_name()
birthday = fakerFR.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d")


class plw_orangehrm ():
    def __init__(self, page: Page):
        self.page = page
    def get_by_label(self, label):
        self.page = page
        element = page.locator(f"xpath=//label[text()='{label}']/../..//input")
        return (element)

    def login (self, username, password, fullname):
        page= self.page
        page.goto("https://opensource-demo.orangehrmlive.com")
        page.get_by_role("textbox", name="Username").fill(username)
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Login").click()
        # expect(page.locator("p.oxd-userdropdown-name")).to_have_text(fullname)

    def add_employee (self, first_name, last_name, id):
        page.get_by_role("link", name="PIM").click()
        page.get_by_role("button", name="Add").click()
        page.get_by_role("textbox", name="First Name").fill(first_name)
        page.get_by_role("textbox", name="Last Name").fill(last_name)
        plw.get_by_label('Employee Id').fill(id)
        page.get_by_role("button", name="Save").click()
        expect(page.get_by_text(f"{prenom} {nom}")).to_be_visible()

    def employee_details (self, last_name, first_name):
        page.get_by_role("link", name="PIM").click()
        plw.get_by_label('Employee Name').click()
        time.sleep(0.2)
        plw.get_by_label('Employee Name').type(last_name)
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
        date_of_birth.fill(birthday)
        page.locator("xpath=//label[text()='Male']").click()
        page.get_by_role("button", name="Save").nth(0).click()

    def logout (self):
        page= self.page
        page.locator("p.oxd-userdropdown-name").click()
        page.get_by_role("menuitem", name="Logout").click()
        expect (page.get_by_role("textbox", name="Username")).to_be_visible()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.set_default_timeout(10000)
    plw = plw_orangehrm(page)
    plw.login("Admin", "admin123", "Michael Keshav")
    #plw.add_employee('Hassan', 'IMHAH', matricule)
    plw.logout()
