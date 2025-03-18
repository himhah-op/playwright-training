import pytest
from playwright.sync_api import Browser, BrowserContext, expect
@pytest.fixture(scope="module")
def authenticated_context(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    # SETUP : Login
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect (page.locator("a[href*='/pim/viewPimModule']")).to_have_text("PIM")

    yield context  # Exécution des tests

    # TEARDOWN : Logout
    page.locator("p.oxd-userdropdown-name").click()
    page.get_by_role("menuitem", name="Logout").click()
    context.close()
