# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 02:46:53 2021

@author: Nikola
"""

import time
import ui_test_functions
import api_test_functions
import json
import random

def TC1_Proper_login_UI():
    
    try:
    
        UN = "nikolacabi@yahoo.com"
        PW = "HTEC2021"
        
        ui_test_functions.ui_login(UN, PW)
        time.sleep(3)
        
        return ui_test_functions.ui_check_login()
    
    except:
        return "ERROR"


def TC2_Create_Use_Case_missing_title():
    
    time.sleep(1)
    
    try:
    
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_expected("Expected1")  
        ui_test_functions.ui_write_uc_step("Step1")
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()

    except:
        return "ERROR"


def TC3_Create_Use_Case_title_empty_space():
    
    time.sleep(1)
    
    try:
    
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_title(" ") 
        ui_test_functions.ui_write_uc_expected("Expected1")  
        ui_test_functions.ui_write_uc_step("Step1")
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()
    
    except:
        return "ERROR"


def TC4_Create_Use_Case_title_too_short():
    
    time.sleep(1)
    
    try:
        
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_title("Titl") 
        ui_test_functions.ui_write_uc_expected("Expected1")  
        ui_test_functions.ui_write_uc_step("Step1")
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()

    except:
        return "ERROR"


def TC5_Create_Use_Case_missing_expected_result():
    
    time.sleep(1)
    
    try:
    
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_title("Title1")  
        ui_test_functions.ui_write_uc_step("Step1")
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()

    except:
        return "ERROR"


def TC6_Create_Use_Case_expected_empty_space():
    
    time.sleep(1)
    
    try:
    
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_title("Title1") 
        ui_test_functions.ui_write_uc_expected(" ")  
        ui_test_functions.ui_write_uc_step("Step1")
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()

    except:
        return "ERROR"


def TC7_Create_Use_Case_expected_too_short():
    
    time.sleep(1)
    
    try:
    
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_title("Title1") 
        ui_test_functions.ui_write_uc_expected("Expe")  
        ui_test_functions.ui_write_uc_step("Step1")
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()

    except:
        return "ERROR"


def TC8_Create_Use_Case_missing_step():
    
    time.sleep(1)
    
    try:
    
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_title("Title1")  
        ui_test_functions.ui_write_uc_expected("Expected1")  
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()

    except:
        return "ERROR"


def TC9_Create_Use_Case_step_empty_space():
    
    time.sleep(1)
    
    try:
    
        ui_test_functions.ui_start_uc_creating()
        time.sleep(1)
        ui_test_functions.ui_write_uc_title("Title1") 
        ui_test_functions.ui_write_uc_expected("Expected1") 
        ui_test_functions.ui_write_uc_step(" ")
        ui_test_functions.ui_press_uc_submit()
        
        return ui_test_functions.ui_check_improper_uc()

    except:
        return "ERROR"
    

def TC10_Use_Case_edge_cases():
    
    time.sleep(1)
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_use_cases(token)
    
    try:
        
        ui_test_functions.ui_add_use_case("Title", "uc_desc_txt", "Expec", "false", 1, "Step1")
    
        return ui_test_functions.ui_check_use_case(1, 1, "Title", "uc_desc_txt", "Expec", "false", 1, "Step1") 

    except:
        return "ERROR"
    
    
def TC11_Logout():
    
    time.sleep(1)
    
    try:
        ui_test_functions.ui_logout()
        
        time.sleep(1)
        
        return ui_test_functions.ui_check_logout()
    
    except:
        return "ERROR"


def TC12_Multiple_Login_atempts():
    
    time.sleep(1)
    TC11_Logout()
    time.sleep(1)
        
    try:
        for i in range (0, 11):
            
            UN = "nikolacabi@yahoo.com"
            PW = str(random.randint(100000, 999999))
            
            ui_test_functions.ui_login(UN, PW)
            time.sleep(3)

            
        res = TC1_Proper_login_UI()
        if res == "PASSED":
            return "FAILED"
        else:
            return "PASSED"
        
    except:
        return "ERROR"
   
