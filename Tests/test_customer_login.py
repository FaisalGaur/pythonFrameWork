import unittest
from Pages.customer_login_page import CustomerLoginPage
from Base.base import BaseClass


class CustomerLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_object = BaseClass()
        cls.driver = cls.base_object.browser_open()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_customer_login_case_valid(self):
        driver = self.driver
        driver.get(self.base_object.read_config("login.txt", "BASE", "URL") + "/account/login")
        login = CustomerLoginPage(driver)
        login.enter_customer_login_email(self.base_object.read_config("login.txt", "CUSTOMER", "EMAIL"))
        login.enter_customer_login_password(self.base_object.read_config("login.txt", "CUSTOMER", "PASSWORD"))
        login.click_login_sign_in_button()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Tests Finished")


if __name__ == '__main__':
    unittest.main()



