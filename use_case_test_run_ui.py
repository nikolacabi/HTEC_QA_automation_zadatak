# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 03:57:44 2021

@author: Nikola
"""

import ui_test_use_cases
from datetime import datetime
import api_tests_playground

# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    
    now = datetime.now()
    now_string = now.strftime("%d-%m-%Y" + '_' + "%H%M%S")
        
    log_file_name = "UI_test_log" + now_string + ".txt"
    f = open(log_file_name, "x")
    f.write("Test Case / Result" + '\n')
    print("Test Case / Result")
    
    try:
        
        api_tests_playground.Clean_up()

        test_run_results = {}
        
        test_run_results['TC1_Proper_login_UI'] = ui_test_use_cases.TC1_Proper_login_UI()
        test_run_results['TC2_Create_Use_Case_missing_title'] = ui_test_use_cases.TC2_Create_Use_Case_missing_title()
        test_run_results['TC3_Create_Use_Case_title_empty_space'] = ui_test_use_cases.TC3_Create_Use_Case_title_empty_space()  
        test_run_results['TC4_Create_Use_Case_title_too_short'] = ui_test_use_cases.TC4_Create_Use_Case_title_too_short() 
        test_run_results['TC5_Create_Use_Case_missing_expected_result'] = ui_test_use_cases.TC5_Create_Use_Case_missing_expected_result() 
        test_run_results['TC6_Create_Use_Case_expected_empty_space'] = ui_test_use_cases.TC6_Create_Use_Case_expected_empty_space() 
        test_run_results['TC7_Create_Use_Case_expected_too_short'] = ui_test_use_cases.TC7_Create_Use_Case_expected_too_short() 
        test_run_results['TC8_Create_Use_Case_missing_step'] = ui_test_use_cases.TC8_Create_Use_Case_missing_step() 
        test_run_results['TC9_Create_Use_Case_step_empty_space'] = ui_test_use_cases.TC9_Create_Use_Case_step_empty_space() 
        test_run_results['TC10_Use_Case_edge_cases'] = ui_test_use_cases.TC10_Use_Case_edge_cases() 
        test_run_results['TC11_Logout'] = ui_test_use_cases.TC11_Logout() 
        test_run_results['TC12_Multiple_Login_atempts'] = ui_test_use_cases.TC12_Multiple_Login_atempts() 
        
        for k in test_run_results.keys():
            
            line = k + " - " + str(test_run_results[k])
            print(line)
            f.write(line + '\n')
            
        print(log_file_name + " has been created")
        f.close()
        
        input("Press Any Key To Exit")
        
    except:
        
        print("ERROR occurred")
        f.write("ERROR occurred\n")
        
        print(log_file_name + " has been created")
        f.close()
        input("Press Any Key To Exit")