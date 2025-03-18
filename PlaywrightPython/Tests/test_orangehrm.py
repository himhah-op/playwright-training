import Libs.plw_orangehrm as plw
from playwright.sync_api import Page

def test_login_logout(page: Page):
    p = plw.LoginPage(page)
    p.login("Admin", "admin123")
    p.check_pim_menu()

def test_add_employee (page:Page, authenticated_context):
    page = authenticated_context.new_page()
    p = plw.AddEmployeePage(page)
    page.close()

def test_employee_details (page:Page, authenticated_context):
    page = authenticated_context.new_page()
    p = plw.EmployeeDetailsPage(page)
    page.close()
