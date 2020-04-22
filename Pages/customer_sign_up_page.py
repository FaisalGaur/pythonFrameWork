from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains


class CustomerSignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_sign_up_first_name_field = Locators.customer_sign_up_first_name_field
        self.customer_sign_up_last_name_field = Locators.customer_sign_up_last_name_field
        self.customer_sign_up_phone_field = Locators.customer_sign_up_phone_field
        self.customer_sign_up_email_field = Locators.customer_sign_up_email_field
        self.customer_sign_up_show_password = Locators.customer_sign_up_show_password
        self.customer_sign_up_password_field = Locators.customer_sign_up_password_field
        self.customer_sign_up_news_letter_yes = Locators.customer_sign_up_news_letter_yes
        self.customer_sign_up_agree_policy = Locators.customer_sign_up_agree_policy
        self.customer_sign_up_submit_button = Locators.customer_sign_up_submit_button

    def enter_customer_sign_up_first_name(self, customer_sign_up_first_name):
        self.driver.find_element_by_xpath(self.customer_sign_up_first_name_field).clear()
        self.driver.find_element_by_xpath(self.customer_sign_up_first_name_field).send_keys(customer_sign_up_first_name)

    def enter_customer_sign_up_last_name(self, customer_sign_up_last_name):
        self.driver.find_element_by_xpath(self.customer_sign_up_last_name_field).clear()
        self.driver.find_element_by_xpath(self.customer_sign_up_last_name_field).send_keys(customer_sign_up_last_name)

    def enter_customer_sign_up_phone(self, customer_sign_up_phone):
        self.driver.find_element_by_xpath(self.customer_sign_up_phone_field).clear()
        self.driver.find_element_by_xpath(self.customer_sign_up_phone_field).send_keys(customer_sign_up_phone)

    def enter_customer_sign_up_email(self, customer_sign_up_email):
        self.driver.find_element_by_xpath(self.customer_sign_up_email_field).clear()
        self.driver.find_element_by_xpath(self.customer_sign_up_email_field).send_keys(customer_sign_up_email)

    def enter_customer_sign_up_password(self, customer_sign_up_password):
        self.driver.find_element_by_xpath(self.customer_sign_up_password_field).clear()
        self.driver.find_element_by_xpath(self.customer_sign_up_password_field).send_keys(customer_sign_up_password)

    def click_customer_sign_up_show_password(self):
        self.driver.find_element_by_xpath(self.customer_sign_up_show_password).click()

    def click_customer_sign_up_news_letter_yes(self):
        element = self.driver.find_element_by_xpath(self.customer_sign_up_news_letter_yes)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def click_customer_sign_up_agree_policy(self):
        element = self.driver.find_element_by_xpath(self.customer_sign_up_agree_policy)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def click_customer_sign_up_submit_button(self):
        self.driver.find_element_by_xpath(self.customer_sign_up_submit_button).click()
