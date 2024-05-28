import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope="module")
def admin_page(driver):
    return AdminPage(driver)

def test_login(login_page):
    login_page.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login('Admin', 'admin123')

@pytest.mark.parametrize("menu_option", [
    "User Management",
    "Job",
    "Organization",
    "Qualifications",
    "Nationalities",
    "Corporate Banking",
    "Configuration"
])
def test_admin_menu_options(admin_page, menu_option):
    admin_page.click_menu_option(menu_option)
    assert admin_page.driver.current_url != "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", f"{menu_option} menu option failed"
