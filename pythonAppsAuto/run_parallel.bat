cd %~dp0
pytest -n 5 --html=Reports/parallel_test_report.html --css=Reports/assets/custom.css
cd Reports
parallel_test_report.html
PAUSE