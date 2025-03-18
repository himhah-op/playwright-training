import random
import pytest
import csv
import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright

with open('logins.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

@pytest.fixture
def test_data():
    with open('logins.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

@pytest.mark.parametrize("row", data)
def test_exemple1(row):
    print (row)

def test_example2(test_data):
    for row in test_data:
	    print(row)

def get_input_by_label (page: Page, label):
    element = page.locator(f"xpath=//label[text()='{label}']/../..//input")
    return (element)
def test_add_employee(authenticated_context):
    page = authenticated_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="First Name").fill("Hassan")
    page.get_by_role("textbox", name="Last Name").fill("IMHAH")
    get_input_by_label(page, 'Employee Id').fill(str(random.randrange(100000, 999999)))
    page.get_by_role("button", name="Save").click()
    expect(page).to_have_url(re.compile(".*/pim/viewPersonalDetails/empNumber.*"))
    page.close()

