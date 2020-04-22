import unittest
import HtmlTestRunner
import os
from Tests.test_customer_login import CustomerLogin
from Tests.test_customer_sign_up import CustomerSignUp

if __name__ == '__main__':
    current_dir = os.getcwd()

    customer_tests_sign_up = unittest.TestLoader().loadTestsFromTestCase(CustomerSignUp)
    customer_tests_login = unittest.TestLoader().loadTestsFromTestCase(CustomerLogin)

    test_suite = unittest.TestSuite([customer_tests_sign_up, customer_tests_login])
    
    runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Test_Suite_Report", add_timestamp=False)
    
    runner.run(test_suite)

