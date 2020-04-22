from Locators.locators import Locators


class CustomerLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_login_email_field = Locators.customer_login_email_field
        self.customer_login_password_field = Locators.customer_login_password_field
        self.customer_login_sign_in_button = Locators.customer_login_sign_in_button

    def enter_customer_login_email(self, customer_login_email):
        self.driver.find_element_by_xpath(self.customer_login_email_field).clear()
        self.driver.find_element_by_xpath(self.customer_login_email_field).send_keys(customer_login_email)

    def enter_customer_login_password(self, customer_login_password):
        self.driver.find_element_by_xpath(self.customer_login_password_field).clear()
        self.driver.find_element_by_xpath(self.customer_login_password_field).send_keys(customer_login_password)

    def click_login_sign_in_button(self):
        self.driver.find_element_by_xpath(self.customer_login_sign_in_button).click()



