# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 04:12:27 2021

@author: Nikola
"""

import ui_test_use_cases
import api_tests_playground
import ui_test_functions
import api_test_functions


ui_test_use_cases.TC1_Proper_login_UI()

ui_test_functions.ui_add_use_case("TC6_Update_technologies", "Update technologies using PUT", "Technologies name changed to Tech4", "true", 2, ["Create Tech3 in Technologies", "Send PUT command to change it to Tech4"])
ui_test_functions.ui_add_use_case("TC13_Create_teams_invalid", "Send invalid values for team name", "Team not created with appropriate response message", "true", 2, ["Send empty space char", "Send vfbgeerbvebrerbgerberberberjw31"])
ui_test_functions.ui_add_use_case("TC3_Improper_login_email", "Try to login with email that is not registered", "'email': 'User not found' text in response", "true", 1, "Send request containing unregistrated email")
ui_test_functions.ui_add_use_case("TC12_Multiple_Login_atempts", "Try to login multiple times in short period with wrong password", "Login impossible due to security", 'true', 11, ["Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password", "Input correct email and wrong password"])
