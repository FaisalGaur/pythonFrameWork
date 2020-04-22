cd %~dp0
pytest -n 2 --html=Reports/parallel_test_report.html
cd Reports
parallel_test_report.html
PAUSE