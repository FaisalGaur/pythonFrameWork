import configparser
import os
import time
from selenium import webdriver


class BaseClass:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.browser = self.read_config("login.txt", "BASE", "BROWSER")
        if self.browser == "CHROME":
            self.driver = webdriver.Chrome(self.current_directory + r'\Resource\driver\chromedriver.exe')
        elif self.browser == "FIREFOX":
            self.driver = webdriver.Firefox(
                executable_path=self.current_directory + r'\Resource\driver\geckodriver.exe')
        else:
            print("Browser property value is not correct! should be CHROME or FIREFOX only")

    def browser_open(self):
        return self.driver

    def read_config(self, filename, section, variable):
        config_parser = configparser.RawConfigParser()
        config_file_path = self.current_directory + r'\Resource\configs\\' + filename
        print(config_file_path)
        config_parser.read(config_file_path)
        return config_parser.get(section, variable)

    def write_data(self, filename, mode, data):
        output_file = open(self.current_directory + r'\Resource\data\\' + filename, mode)
        output_file.write(data+"\n")
        output_file.close()

    def time_stamp(self):
        self.is_not_used()
        return time.strftime("%Y%m%d%H%M%S")

    def is_not_used(self):
        pass


if __name__ == '__main__':
    login = BaseClass()
