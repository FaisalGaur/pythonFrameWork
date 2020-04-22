import unittest
import HtmlTestRunner
import os
from Tests.test_customer_login import CustomerLogin
from Tests.test_customer_sign_up import CustomerSignUp

if __name__ == '__main__':
    current_dir = os.getcwd()

    customer_tests_login = unittest.TestLoader().loadTestsFromTestCase(CustomerLogin)
    customer_tests_sign_up = unittest.TestLoader().loadTestsFromTestCase(CustomerSignUp)

    test_suite = unittest.TestSuite([customer_tests_sign_up, customer_tests_login])
    
    runner = HtmlTestRunner.HTMLTestRunner(output=current_dir + "\\Reports")
    
    runner.run(test_suite)

