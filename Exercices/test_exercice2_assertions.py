import pytest
import csv
from playwright.sync_api import Page, expect, Playwright
import random
import re
import time
matricule = str(random.randrange (100000, 999999))
def login (page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("a[href*='viewPimModule']")).to_be_visible()
def logout (page: Page):
    page.locator("p.oxd-userdropdown-name").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect (page.get_by_role("textbox", name="Username")).to_be_visible()

def get_input_by_label (page: Page, label):
    element = page.locator(f"xpath=//label[text()='{label}']/../..//input")
    return (element)

def test_a_add_employee(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login(page)
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="First Name").fill("Hassan")
    page.get_by_role("textbox", name="Last Name").fill("IMHAH")

    get_input_by_label(page, 'Employee Id').fill(matricule)

    page.get_by_role("button", name="Save").click()

    expect (page.locator("div.orangehrm-edit-employee-imagesection h6")).to_have_text("Hassan IMHAH")
    expect(page).to_have_url(re.compile(".*/pim/viewPersonalDetails/empNumber.*"))
    expect (page.locator("a[href*='viewPersonalDetails']")).to_have_text("Personal Details")

    page.locator("xpath=//label[text()='Nationality']/../..//i").click()
    time.sleep (0.2)
    page.locator("div[role='listbox']").get_by_text("French").click()
    logout(page)

