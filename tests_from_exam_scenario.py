# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:39:56 2021

@author: Nikola
"""

import time
import ui_test_functions
from ui_test_functions import ui_login


def TC1_Login():
    
    UN = "nikolacabi@yahoo.com"
    PW = "HTEC2021"
    
    ui_login(UN, PW)
    time.sleep(5)
    
    return ui_test_functions.ui_check_login()
    

def TC2_open_Use_Case():
    
    ui_test_functions.ui_start_uc_creating()
    time.sleep(2)
    
    return ui_test_functions.ui_check_uc_entered()


def TC3_Create_4_Use_Cases():
    
    ui_test_functions.ui_del_uc(100)
    
    result = []
    
    time.sleep(2)
    ui_test_functions.ui_add_use_case("Use Case 1", "Description 1", "Expected 1", "true", 1, ["Step 1"])
    time.sleep(2)
    result.append(ui_test_functions.ui_check_use_case(1, 1, "Use Case 1", "Description 1", "Expected 1", "true", 1, ["Step 1"]))
    time.sleep(2)
    ui_test_functions.ui_add_use_case("Use Case 2", "Description 2", "Expected 2", "false", 2, ["Step 1", "Step 2"])
    time.sleep(2)
    result.append(ui_test_functions.ui_check_use_case(1, 2, "Use Case 2", "Description 2", "Expected 2", "false", 2, ["Step 1", "Step 2"]))
    time.sleep(2)
    ui_test_functions.ui_add_use_case("Use Case 3", "Description 3", "Expected 3", "true", 3, ["Step 1", "Step 2", "Step 3"])
    time.sleep(2)
    result.append(ui_test_functions.ui_check_use_case(1, 3, "Use Case 3", "Description 3", "Expected 3", "true", 3, ["Step 1", "Step 2", "Step 3"]))
    time.sleep(2)
    ui_test_functions.ui_add_use_case("Use Case 4", "Description 4", "Expected 4", "false", 4, ["Step 1", "Step 2", "Step 3", "Step 4"])
    time.sleep(2)
    result.append(ui_test_functions.ui_check_use_case(1, 4, "Use Case 4", "Description 4", "Expected 4", "false", 4, ["Step 1", "Step 2", "Step 3", "Step 4"]))
    
    return result


def TC4_Edit_all_input_fields():
       
    ui_test_functions.ui_change_use_case(1, 4, 4)
    time.sleep(2)
    
    return ui_test_functions.ui_check_use_case(1, 4, "This field previously had 10 characters", "This field previously had 13 characters", "This field previously had 10 characters", "false", 4, ["This field previously had 6 characters", "This field previously had 6 characters", "This field previously had 6 characters", "This field previously had 6 characters"])   
    
# =============================================================================
# MAIN
# =============================================================================

result = {}
result['TC1_Login'] = TC1_Login()
result["TC2_open_Use_Case"] = TC2_open_Use_Case()
result["TC3_Create_4_Use_Cases"] = TC3_Create_4_Use_Cases()
result["TC4_Edit_all_input_fields"] = TC4_Edit_all_input_fields()
