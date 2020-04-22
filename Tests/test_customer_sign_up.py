import unittest
from Pages.customer_sign_up_page import CustomerSignUpPage
from Pages.customer_home_page import CustomerHomePage
from Base.base import BaseClass


class CustomerSignUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_object = BaseClass()
        cls.driver = cls.base_object.browser_open()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_customer_sign_up_case_valid(self):
        driver = self.driver
        driver.get(self.base_object.read_config("login.txt", "BASE", "URL") + "/account/register")
        login = CustomerSignUpPage(driver)
        login.enter_customer_sign_up_first_name(self.base_object.read_config("login.txt", "CUSTOMER", "FIRST_NAME"))
        login.enter_customer_sign_up_last_name(self.base_object.read_config("login.txt", "CUSTOMER", "LAST_NAME"))

        master_email = self.base_object.read_config("login.txt", "BASE", "MASTER_EMAIL")
        master_domain = self.base_object.read_config("login.txt", "BASE", "MASTER_DOMAIN")
        time_stamp = self.base_object.time_stamp()
        email = master_email + "+" + time_stamp + "@" + master_domain
        self.base_object.write_data("data.txt", "a+", email)
        login.enter_customer_sign_up_email(email)

        login.enter_customer_sign_up_phone(self.base_object.read_config("login.txt", "CUSTOMER", "PHONE"))

        login.click_customer_sign_up_show_password()
        login.enter_customer_sign_up_password(self.base_object.read_config("login.txt", "CUSTOMER", "PASSWORD"))

        login.click_customer_sign_up_news_letter_yes()
        login.click_customer_sign_up_agree_policy()

        login.click_customer_sign_up_submit_button()

        home = CustomerHomePage(driver)
        text_search_button = home.text_customer_home_search_button()
        self.assertEqual(text_search_button, "Enter your search key")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Tests Finished")


if __name__ == '__main__':
    unittest.main()

