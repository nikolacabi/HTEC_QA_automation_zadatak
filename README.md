# HTEC_QA_automation_zadatak

Project is split in several files:

api_test_functions.py is containing all functions for testing API (only Playground section covered so far). Combination of those functions is used to generate all test cases.

api_tests_playground.py is containing all test created for playground which is tested only by API tests. There are 34 tests there that cove most of functional scenarios.

playground_test_run_api is script that has structure for containing results of all Playground tests and it also writes results to console and to log file.

script_with_4_test_details_auto fill is script that will fill in Use Case section with 4 Use Cases (4 short tests which I selected from api_tests_playground.py). Reason for this is that Use Case is target of tests itself and is not suited to contain test requirements.

tests_from_exam_scenario.py is script that literally follows scenario from Exam section.

ui_test_functions.py is containing all functions for testing UI (only Use Case section covered so far). Combination of those functions is used to generate all test cases for UI as well as scenario from Exam and 4 Use Cases needed to have everything ready for submit

ui_test_use_cases.py is containing additional UI tests (more than ones from Exam scenario), to test Use Case section in more details.

use_case_test_run_ui.py is script that has structure for containing results of all Use Case tests and it also writes results to console and to log file.

In order to run all the tests, all scripts should be in same root folder. In order to have actual results visible in console just navigate to that root folder and run api_tests_playground.py and use_case_test_run_ui.py. 
(I assume its possible to run in parallel in different consoles)
