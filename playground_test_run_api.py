# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 01:42:47 2021

@author: Nikola
"""

import api_tests_playground
from datetime import datetime


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    
    now = datetime.now()
    now_string = now.strftime("%d-%m-%Y" + '_' + "%H%M%S")
        
    log_file_name = "API_test_log_" + now_string + ".txt"
    f = open(log_file_name, "x")
    f.write("Test Case / Result" + '\n')
    print("Test Case / Result")
    
    try:
        api_tests_playground.Clean_up()
    
        test_run_results = {}
        
        test_run_results['TC1_Login'] = api_tests_playground.TC1_Proper_login()
        test_run_results['TC2_Improper_login_password'] = api_tests_playground.TC2_Improper_login_password()
        test_run_results['TC3_Improper_login_email'] = api_tests_playground.TC3_Improper_login_email() 
        
        test_run_results['TC4_Create_technologies_valid'] = api_tests_playground.TC4_Create_technologies_valid() 
        test_run_results['TC5_Create_technologies_invalid'] = api_tests_playground.TC5_Create_technologies_invalid() 
        test_run_results['TC6_Update_technologies'] = api_tests_playground.TC6_Update_technologies() 
        test_run_results['TC7_Create_existing_technologies'] = api_tests_playground.TC7_Create_existing_technologies() 
        
        test_run_results['TC8_Create_seniorities_valid'] = api_tests_playground.TC8_Create_seniorities_valid() 
        test_run_results['TC9_Create_seniorities_invalid'] = api_tests_playground.TC9_Create_seniorities_invalid() 
        test_run_results['TC10_Update_seniorities'] = api_tests_playground.TC10_Update_seniorities() 
        test_run_results['TC11_Create_existing_seniorities'] = api_tests_playground.TC11_Create_existing_seniorities() 
        
        test_run_results['TC12_Create_teams_valid'] = api_tests_playground.TC12_Create_teams_valid() 
        test_run_results['TC13_Create_teams_invalid'] = api_tests_playground.TC13_Create_teams_invalid() 
        test_run_results['TC14_Update_teams'] = api_tests_playground.TC14_Update_teams() 
        test_run_results['TC15_Create_existing_teams'] = api_tests_playground.TC15_Create_existing_teams() 
    
        test_run_results["TC16_Create_people_valid_name"] = api_tests_playground.TC16_Create_people_valid_name()
        test_run_results['TC17_Create_people_other_fields'] = api_tests_playground.TC17_Create_people_other_fields()
        test_run_results['TC18_Create_people_invalid_name'] = api_tests_playground.TC18_Create_people_invalid_name()
        test_run_results['TC19_Create_people_invalid_fields'] = api_tests_playground.TC19_Create_people_invalid_fields()
        test_run_results['TC20_Update_people_existing_fields'] = api_tests_playground.TC20_Update_people_existing_fields()
        test_run_results['TC21_Update_people_add_fields'] = api_tests_playground.TC21_Update_people_add_fields()
        test_run_results['TC22_Update_people_remove_fields'] = api_tests_playground.TC22_Update_people_remove_fields()
        test_run_results['TC23_Create_existing_people'] = api_tests_playground.TC23_Create_existing_people()
        test_run_results['TC24_Delete_team_from_people()'] = api_tests_playground.TC24_Delete_team_from_people()
        test_run_results['TC25_Delete_seniorities_from_people'] = api_tests_playground.TC25_Delete_seniorities_from_people()
        test_run_results['TC26_Delete_1_technologies_from_people'] = api_tests_playground.TC26_Delete_1_technologies_from_people()
        test_run_results['TC27_Delete_seniorities_from_people'] = api_tests_playground.TC27_Delete_seniorities_from_people()
    
        test_run_results['TC28_Create_Projects_valid'] = api_tests_playground.TC28_Create_Projects_valid()
        test_run_results['TC29_Create_Projects_add_people'] = api_tests_playground.TC29_Create_Projects_add_people()
        test_run_results['TC30_Create_Projects_invalid'] = api_tests_playground.TC30_Create_Projects_invalid()
        test_run_results['TC31_Create_Projects_add_ivalid_people'] = api_tests_playground.TC31_Create_Projects_add_ivalid_people()
        test_run_results['TC32_Update_Projects'] = api_tests_playground.TC32_Update_Projects()
        test_run_results['TC33_Create_existing_Projects'] = api_tests_playground.TC33_Create_existing_Projects()
    
        test_run_results['TC34_Multiple_Login_atempts'] = api_tests_playground.TC34_Multiple_Login_atempts()
    
        
        for k in test_run_results.keys():
            
            line = k + " - " + test_run_results[k]
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