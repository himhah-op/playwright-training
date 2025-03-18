import pytest
import csv
from playwright.sync_api import Page, expect, Playwright


def test_a_login_logout(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect (page.locator("p.oxd-userdropdown-name")).to_have_text("hassan")
    page.locator("p.oxd-userdropdown-name").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect (page.get_by_role("textbox", name="Username")).to_be_visible()
