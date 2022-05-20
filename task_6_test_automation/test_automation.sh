cd /C/Users/Admin/venv/Scripts
#Activate python project virtual environment
source activate
#Execute test suite
pytest /E/Forage/Quantium/Task1/quantium-starter-repo/task_6_test_automation/dash_app_visualization_test.py
#returns exit code for a test suite execution
#Exit code 0 : All tests were collected and passed successfully
#Exit code 1 : Tests were collected and run but some of the tests failed
echo "exit code is : "$?