import unittest
from Pages.admin_login_page import AdminLoginPage
from Pages.admin_dashboard_page import AdminDashboardPage
from Base.base import BaseClass


class AdminDashboard(unittest.TestCase):
    def setUp(self):
        self.base_object = BaseClass()
        self.driver = self.base_object.browser_open()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_admin_dashboard_load(self):
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

    def test_admin_dashboard_status_update(self):
        driver = self.driver
        driver.get(self.base_object.read_config("login.txt", "BASE", "URL"))
        login = AdminLoginPage(driver)
        login.enter_admin_login_email(self.base_object.read_config("login.txt", "ADMIN", "EMAIL"))
        login.enter_admin_login_password(self.base_object.read_config("login.txt", "ADMIN", "PASSWORD"))
        login.click_login_button()
        home = AdminDashboardPage(driver)
        home.close_switch_window()
        text_status_update = home.update_status()
        self.assertEqual(text_status_update, "This is a test status update")
        home.delete_status()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Tests Finished")


if __name__ == '__main__':
    unittest.main()



