import pytest
import csv
from playwright.sync_api import Page, expect, Playwright

with open('logins.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)
@pytest.mark.parametrize("row", data)
def test_a_login_logout(playwright: Playwright, row):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(row['username'])
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect (page.locator("p.oxd-userdropdown-name")).to_have_text(row['fullname'])
    page.locator("p.oxd-userdropdown-name").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect (page.get_by_role("textbox", name="Username")).to_be_visible()
