
class AdminLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name_field = "//*[@id='UserName']"
        self.password_field = "//*[@id='Password']"
        self.login_button = "//*[@id='LoginButton']"
        self.reset_password_link = "//*[@id='ResetPwdLnk']"
        self.authentication_failed = "//span[text()='Authentication failed']"

    def enter_admin_login_email(self, admin_login_email):
        self.driver.find_element_by_xpath(self.user_name_field).clear()
        self.driver.find_element_by_xpath(self.user_name_field).send_keys(admin_login_email)

    def enter_admin_login_password(self, admin_login_password):
        self.driver.find_element_by_xpath(self.password_field).clear()
        self.driver.find_element_by_xpath(self.password_field).send_keys(admin_login_password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def check_authentication_failure(self):
        return self.driver.find_element_by_xpath(self.authentication_failed).text

    def change_password_link(self):
        return self.driver.find_element_by_xpath(self.reset_password_link).text




