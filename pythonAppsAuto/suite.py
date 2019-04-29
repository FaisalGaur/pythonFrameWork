import unittest
import HtmlTestRunner
import os
from Tests.test_admin_login import AdminLogin
from Tests.test_admin_dashboard import AdminDashboard

if __name__ == '__main__':
    current_dir = os.getcwd()

    admin_tests_login = unittest.TestLoader().loadTestsFromTestCase(AdminLogin)
    admin_tests_dashboard = unittest.TestLoader().loadTestsFromTestCase(AdminDashboard)

    test_suite = unittest.TestSuite([admin_tests_login, admin_tests_dashboard])
    
    runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Test_Suite_Report", add_timestamp=False)
    
    runner.run(test_suite)

