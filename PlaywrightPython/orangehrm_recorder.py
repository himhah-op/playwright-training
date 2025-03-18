import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("manda user")).to_be_visible()


    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("Hassan")
    page.get_by_role("textbox", name="First Name").press("Tab")
    page.get_by_role("textbox", name="Middle Name").press("Tab")
    page.get_by_role("textbox", name="Last Name").fill("IMHAH")
    page.locator("form").get_by_role("textbox").nth(4).click()
    page.locator("form").get_by_role("textbox").nth(4).fill("987543")
    page.get_by_role("button", name="Save").click()


    page.locator("form").filter(has_text="Employee Full NameEmployee").locator("i").nth(1).click()
    page.locator("form").filter(has_text="Employee Full NameEmployee").locator("i").nth(2).click()
    page.get_by_role("option", name="Single").click()
    page.locator("div").filter(has_text=re.compile(r"^Date of BirthGenderMaleFemale$")).get_by_placeholder("yyyy-dd-mm").click()
    page.get_by_role("textbox", name="yyyy-dd-mm").nth(1).fill("2000-12-23")
    page.locator("label").filter(has_text=re.compile(r"^Male$")).locator("span").click()
    page.locator("form").filter(has_text="Employee Full NameEmployee").get_by_role("button").click()
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("textbox", name="Type for hints...").first.click()
    page.get_by_role("textbox", name="Type for hints...").first.fill("IMHAH")
    page.get_by_role("button", name="Search").click()
    page.get_by_text("987543").click(button="right")
    page.get_by_text("987543").click()
    page.get_by_role("link", name="Contact Details").click()
    page.locator("div:nth-child(2) > .oxd-input").first.click()
    page.locator("div:nth-child(2) > .oxd-input").first.fill("29")
    page.locator("div:nth-child(2) > .oxd-input").first.press("Tab")
    page.locator("div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input").first.fill("rue des sablons")
    page.locator("div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input").first.press("Tab")
    page.locator("div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-input").first.fill("75008")
    page.locator("div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-input").first.press("Tab")
    page.locator("div:nth-child(4) > .oxd-input-group > div:nth-child(2) > .oxd-input").fill("PARIS")
    page.locator("div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-input").first.click()
    page.locator("div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-input").first.click()
    page.locator("div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-input").first.fill("Paris")
    page.locator("div:nth-child(5) > .oxd-input-group > div:nth-child(2) > .oxd-input").click()
    page.locator("div:nth-child(5) > .oxd-input-group > div:nth-child(2) > .oxd-input").fill("75008")
    page.locator("form i").click()
    page.locator(".oxd-layout-context").click()
    page.locator("div:nth-child(6) > .oxd-grid-3 > div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input").click()
    page.locator("div:nth-child(6) > .oxd-grid-3 > div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input").fill("06575757")
    page.locator("div:nth-child(9) > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-input").first.click()
    page.locator("div:nth-child(9) > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-input").first.fill("hassan.imhah@playwright.test")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("link", name="PIM").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("95")
    page.get_by_role("textbox").nth(2).press("Enter")
    page.get_by_role("textbox").nth(2).fill("")
    page.get_by_role("textbox", name="Type for hints...").first.click()
    page.get_by_role("textbox", name="Type for hints...").first.fill("IMHAH")
    page.get_by_role("button", name="Search").click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("987543")
    page.get_by_role("textbox", name="Type for hints...").first.click()
    page.get_by_role("textbox", name="Type for hints...").first.fill("")
    page.get_by_role("button", name="Search").click()
    page.get_by_role("cell", name="").locator("i").click()
    page.get_by_role("button", name=" Delete Selected").click()
    page.get_by_role("button", name=" Yes, Delete").click()
    page.get_by_role("listitem").filter(has_text="firstName lastName").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
