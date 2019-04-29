import unittest
from Pages.admin_login_page import AdminLoginPage
from Pages.admin_dashboard_page import AdminDashboardPage
from Base.base import BaseClass


class AdminLogin(unittest.TestCase):
    def setUp(self):
        self.base_object = BaseClass()
        self.driver = self.base_object.browser_open()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_admin_login_case_valid(self):
        driver = self.driver
        driver.get(self.base_object.read_config("login.txt", "BASE", "URL"))
        login = AdminLoginPage(driver)
        login.enter_admin_login_email(self.base_object.read_config("login.txt", "ADMIN", "EMAIL"))
        login.enter_admin_login_password(self.base_object.read_config("login.txt", "ADMIN", "PASSWORD"))
        login.click_login_button()
        home = AdminDashboardPage(driver)
        home.close_switch_window()
        text_quick_links = home.text_admin_dashboard_quick_links()
        self.assertEqual(text_quick_links, "Quick Links")

    def test_admin_login_case_invalid(self):
        driver = self.driver
        driver.get(self.base_object.read_config("login.txt", "BASE", "URL"))
        login = AdminLoginPage(driver)
        login.enter_admin_login_email(self.base_object.read_config("login.txt", "ADMIN", "EMAIL"))
        login.enter_admin_login_password(self.base_object.read_config("login.txt", "ADMIN", "WRONG_PASSWORD"))
        login.click_login_button()
        text_authentication_failure = login.check_authentication_failure()
        self.assertEqual(text_authentication_failure, "Authentication failed")

    def test_admin_sign_out(self):
        driver = self.driver
        driver.get(self.base_object.read_config("login.txt", "BASE", "URL"))
        login = AdminLoginPage(driver)
        login.enter_admin_login_email(self.base_object.read_config("login.txt", "ADMIN", "EMAIL"))
        login.enter_admin_login_password(self.base_object.read_config("login.txt", "ADMIN", "PASSWORD"))
        login.click_login_button()
        home = AdminDashboardPage(driver)
        home.close_switch_window()
        home.text_admin_dashboard_quick_links()
        home.user_sign_out()
        text_reset_password = login.change_password_link()
        self.assertEqual(text_reset_password, "Forgot username/password?")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Tests Finished")


if __name__ == '__main__':
    unittest.main()



