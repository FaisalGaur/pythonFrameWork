from Locators.locators import Locators


class CustomerHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_home_search_button = Locators.customer_home_search_button

    def text_customer_home_search_button(self):
        return self.driver.find_element_by_xpath(self.customer_home_search_button).get_attribute("placeholder")

