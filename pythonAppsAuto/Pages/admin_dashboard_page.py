from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class AdminDashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.subscription_window = "//span[text()='Subscription Details']"
        self.quick_links = "//span[text()='Quick Links']"
        self.close_button = "//*[text()='Close']"
        self.sign_out = "//a[text()='Sign Out']"
        self.status_update = "//*[text()='This is a test status update']"
        self.confirm_remove_status = "//*[text()='Yes']"
        self.remove_status_update = "//a[contains(@title,'Remove')]"
        self.status_update_field = "//*[@id='c49ca63e807bbf5a42857841_inputdashboard']"
        self.share_button = "//*[@id='sharebuttondashboard']"

    def text_admin_dashboard_quick_links(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.quick_links))
        )
        return element.text

    def close_switch_window(self):
        time.sleep(5)
        close_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.close_button))
        )
        close_button.click()

    def update_status(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, self.close_button))
        )
        self.driver.find_element_by_xpath(self.status_update_field).send_keys("This is a test status update")

        self.driver.find_element_by_xpath(self.share_button).click()

        status_update = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.status_update))
        )
        return status_update.text

    def delete_status(self):
        time.sleep(5)
        remove_status_update = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.remove_status_update))
        )
        remove_status_update.click()

        time.sleep(5)

        confirm_remove_status = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_remove_status))
        )

        confirm_remove_status.click()

        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, self.status_update))
        )

    def user_sign_out(self):
        user_sign_out = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.sign_out))
        )
        user_sign_out.click()






