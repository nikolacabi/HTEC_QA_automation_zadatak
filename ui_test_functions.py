# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 23:39:50 2021

@author: Nikola
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
wait = WebDriverWait(firefox, 2)


def ui_login(email, pw):
    
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/login"
        firefox.get(URL)
        
        EMAIL_XPATH = "/html/body/div/div/div[2]/div/div/div/div/form/div[1]/input"
        inputElement = firefox.find_element_by_xpath(EMAIL_XPATH)
        inputElement.send_keys(email)
        
        PW_XPATH = '/html/body/div/div/div[2]/div/div/div/div/form/div[2]/input'
        inputElement = firefox.find_element_by_xpath(PW_XPATH)
        inputElement.send_keys(pw)
        
        inputElement.send_keys(Keys.ENTER)
        inputElement.submit() 
        
        
    except:
        print("Failed login")
        
        
def ui_check_login():
    
    try:
        
        if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/dashboard':
            print('Check login - PASSED')
            return 'PASSED'
            
        else:
            print('Check login - FAILED')
            return "FAILED"
            
    except:
        print("Login cant be verifed")
        return "ERROR"
    
    
def ui_check_improper_login():
    
    USER_NOT_FOUND_XPATH = "/html/body/div/div/div[2]/div/div/div/div/form/div[1]/div"
    PASSWORD_INCORRECT_XPATH = "/html/body/div/div/div[2]/div/div/div/div/form/div[2]/div"
    
    try:      
        if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/login' and firefox.find_element_by_xpath(USER_NOT_FOUND_XPATH).is_displayed():
            print('Check login user not found - PASSED')
            return 'PASSED'
    except:
        pass
            
    try:        
        if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/login' and firefox.find_element_by_xpath(PASSWORD_INCORRECT_XPATH).is_displayed():  
            print('Check login incorrect password - PASSED')
            return 'PASSED'
            
    except:
        return 'ERROR' 
                    

def ui_add_use_case(uc_title_txt, uc_desc_txt, uc_exp_txt, uc_auto, uc_step_count, uc_step_txt):
        
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/use-cases"
        firefox.get(URL)
        time.sleep(2)
        
        CREATE_UC_XPATH = '/html/body/div/div/div[2]/div/a[2]'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, CREATE_UC_XPATH)))
        element.click()
            
        UC_TITLE_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[1]/input'
        inputElement = firefox.find_element_by_xpath(UC_TITLE_XPATH)
        inputElement.send_keys(uc_title_txt)
        
        UC_DESC_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[2]/textarea"
        inputElement = firefox.find_element_by_xpath(UC_DESC_XPATH)
        inputElement.send_keys(uc_desc_txt)
        
        UC_EXP_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[3]/input"
        inputElement = firefox.find_element_by_xpath(UC_EXP_XPATH)
        inputElement.send_keys(uc_exp_txt)
                
        UC_AUTOMATED_XPATH_SW = '//*[@id="switch"]'
        UC_AUTOMATED_XPATH_LBL = '/html/body/div/div/div[2]/div/div/div/form/div[4]/div/div/label'
        checkElement = firefox.find_element_by_xpath(UC_AUTOMATED_XPATH_SW)
        if uc_auto == 'true' and checkElement.get_attribute('value') == "false":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_AUTOMATED_XPATH_LBL)))
            element.click()
        elif uc_auto == 'false' and checkElement.get_attribute('value') == "true":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_AUTOMATED_XPATH_LBL)))
            element.click()                      
                
        UC_STEP_CSS = '.col-xl-12 > form:nth-child(1) > div:nth-child(11) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        inputElement = firefox.find_element_by_css_selector(UC_STEP_CSS)
        inputElement.send_keys(uc_step_txt[0])
                
        if uc_step_count > 1:
            
            for i in range (1, uc_step_count):
                
                ADD_STEP_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[' + str(5 + i) + ']/button/span'
                element = wait.until(EC.element_to_be_clickable((By.XPATH, ADD_STEP_XPATH)))
                element.click()
                
                UC_STEP_CSS = '.col-xl-12 > form:nth-child(1) > div:nth-child(' + str(11 + i) + ') > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
                inputElement = firefox.find_element_by_css_selector(UC_STEP_CSS)
                inputElement.send_keys(uc_step_txt[i])
                
                
        UC_SUBMIT_XPATH = '/html/body/div/div/div[2]/div/div/div/form/button'      
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_SUBMIT_XPATH)))
        element.click()
        
    except:
        print("Use Case cant be created")
        
        
def ui_check_use_case(pos, tot, uc_title_txt, uc_desc_txt, uc_exp_txt, uc_auto, uc_step_count, uc_step_txt):
    
    result = []
    
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/use-cases"
        firefox.get(URL)
        time.sleep(2)
        
        if tot == 1:
            uc_xpath = '/html/body/div/div/div[2]/div/div/a'
        else:
            uc_xpath = '/html/body/div/div/div[2]/div/div/a[' + str(pos) + ']'
            
        element = wait.until(EC.element_to_be_clickable((By.XPATH, uc_xpath)))
        checkElement = firefox.find_element_by_xpath(uc_xpath)
        if checkElement.text == uc_title_txt:
            print('Check Title outside - PASSED')
            result.append('Check Title outside - PASSED')
        else:
            print('Check Title outside - FAILED')
            result.append('Check Title outside - FAILED')
                                     
        element = firefox.find_element_by_xpath(uc_xpath)
        element.click()
        
        UC_TITLE_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[1]/input'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_TITLE_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_TITLE_XPATH)
        if checkElement.get_attribute('value') == uc_title_txt:
            print('Check Title inside - PASSED')
            result.append('Check Title inside - PASSED')
        else:
            print('Check Title inside - FAILED')
            result.append('Check Title inside - FAILED')
            
        
        UC_DESC_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[2]/textarea"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_DESC_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_DESC_XPATH)
        if checkElement.get_attribute('value') == uc_desc_txt:
            print('Check Description  - PASSED')
            result.append('Check Description  - PASSED')
        else:
            print('Check Description - FAILED')
            result.append('Check Description - FAILED')
        
        
        UC_EXP_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[3]/input"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_EXP_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_EXP_XPATH)
        if checkElement.get_attribute('value') == uc_exp_txt:
            print('Check Expected - PASSED')
            result.append('Check Expected - PASSED')
        else:
            print('Check Expected - FAILED')
            result.append('Check Expected - FAILED')
            
        
        UC_AUTOMATED_XPATH = '//*[@id="switch"]'
        checkElement = firefox.find_element_by_xpath(UC_AUTOMATED_XPATH)
        if checkElement.get_attribute('value') == uc_auto:
            print('Check Automated? - PASSED')
            result.append('Check Automated? - PASSED')
        else:
            print('Check Automated? - FAILED')
            result.append('Check Automated? - FAILED')
            
        for i in range (0, uc_step_count):
                                  
            step_css = '.col-xl-12 > form:nth-child(1) > div:nth-child(' + str(12 + i) + ') > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, step_css)))
            checkElement = firefox.find_element_by_css_selector(step_css)
            
            if checkElement.get_attribute('value') == uc_step_txt[i]:
                print('Check Step', i+1, ' - PASSED')
                result.append('Check Step ' + str(i+1) + ' - PASSED')
            else:
                print('Check Step', i+1, ' - FAILED')
                result.append('Check Step ' + str(i+1) + ' - FAILED')
                
        return result
                                                           
    except:
        return "ERROR"
        
                
def ui_change_use_case(pos, tot, uc_step_count):
    
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/use-cases"
        firefox.get(URL)
        time.sleep(2)
        
        if tot == 1:
            uc_xpath = '/html/body/div/div/div[2]/div/div/a'
        else:
            uc_xpath = '/html/body/div/div/div[2]/div/div/a[' + str(pos) + ']'
            
        element = firefox.find_element_by_xpath(uc_xpath)
        element.click()
        
        UC_TITLE_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[1]/input'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_TITLE_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_TITLE_XPATH)
        uc_title_txt = 'This field previously had ' + str(len(checkElement.get_attribute('value'))) + ' characters'
        checkElement.clear()  
        inputElement = checkElement
        inputElement.send_keys(uc_title_txt)
        
        
        UC_DESC_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[2]/textarea"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_DESC_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_DESC_XPATH)
        uc_desc_txt = 'This field previously had ' + str(len(checkElement.get_attribute('value'))) + ' characters'
        checkElement.clear()  
        inputElement = checkElement
        inputElement.send_keys(uc_desc_txt)
      
        
        UC_EXP_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[3]/input"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_EXP_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_EXP_XPATH)
        uc_exp_txt = 'This field previously had ' + str(len(checkElement.get_attribute('value'))) + ' characters'
        checkElement.clear()  
        inputElement = checkElement
        inputElement.send_keys(uc_exp_txt)
        
                    
        for i in range (0, uc_step_count):
                           
            step_css = '.col-xl-12 > form:nth-child(1) > div:nth-child(' + str(12 + i) + ') > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, step_css)))
            checkElement = firefox.find_element_by_css_selector(step_css)
            uc_step_txt = 'This field previously had ' + str(len(checkElement.get_attribute('value'))) + ' characters'
            checkElement.clear()  
            inputElement = checkElement
            inputElement.send_keys(uc_step_txt)
            
            
        UC_SUBMIT_XPATH = '/html/body/div/div/div[2]/div/div/div/form/button'      
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_SUBMIT_XPATH)))
        element.click()
                                   
    except:
        print("Use Case cant be changed")
        
                              
def ui_del_uc(num_to_del):
    
    for i in range(0, num_to_del):
    
        try:
            
            URL = "https://qa-sandbox.apps.htec.rs/use-cases"
            firefox.get(URL)
            
            
            UC_CHECK_XPATH = '/html/body/div/div/div[2]/div/div/a'
            element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_CHECK_XPATH)))
            element.click()
            
            UC_DEL_BTN = '/html/body/div/div/div[2]/div/div/div/form/span[2]/button'
            element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_DEL_BTN)))
            element.click()
            
            
            UC_DEL_CONFIRM_BTN = '/html/body/div/div/div[2]/div/div/div/form/span[2]/div/div[2]/p/span[2]/button'
            element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_DEL_CONFIRM_BTN)))
            element.click()  
                                            
        except:
            print('all Use Cases deleted')
            break
        

def ui_check_uc_del():
        
    try:  
        
        URL = "https://qa-sandbox.apps.htec.rs/use-cases"
        firefox.get(URL)
        time.sleep(2)
        
        UC_XPATH = '/html/body/div/div/div[2]/div/div/a'        
        checkElement = firefox.find_elements_by_xpath(UC_XPATH)
       
        if len(checkElement):
            print('Check Use Case deleted, Use Case exists - FAILED')
            return "FAILED"
        else:
            print('Check Use Case deleted, Use Case doesnt exists- PASSED')
            return "PASSED"
        
    except:
        print('Cant check Use Case deleted')
        return "ERROR"
        

def ui_start_uc_creating():
       
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/dashboard"
        firefox.get(URL)
        
        XPATH_UC = '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div/a/div/span/img'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_UC)))
        element.click()

    except:
        print('Cant start Use Case creation')
  

def ui_check_uc_entered():
    
    try:    
    
        if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/use-cases':
            print('Check login - PASSED')
            return 'PASSED'
        
        else:
            print('Check login - FAILED')
            return 'FAILED'
    
    except:
        print('Cant check is Use Case entered')        
        return 'ERROR'
                     
    
def ui_write_uc_title(uc_title_txt):
    
    try:
        
        UC_TITLE_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[1]/input'
        inputElement = firefox.find_element_by_xpath(UC_TITLE_XPATH)
        inputElement.send_keys(uc_title_txt)
        
    except:
        print('Cant write Use Case title')
                         
        
def ui_write_uc_description(uc_desc_txt):
    
    try:
        
        UC_DESC_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[2]/textarea"
        inputElement = firefox.find_element_by_xpath(UC_DESC_XPATH)
        inputElement.send_keys(uc_desc_txt)

    except:
        print('Cant write Use Case Description')        


def ui_write_uc_expected(uc_exp_txt):
    
    try: 
        
        UC_EXP_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[3]/input"
        inputElement = firefox.find_element_by_xpath(UC_EXP_XPATH)
        inputElement.send_keys(uc_exp_txt)

    except:
        print('Cant write Use Case Expected Result')   
        
        
def ui_write_uc_step(uc_step_txt):
    
    try: 
        
        UC_STEP_CSS = '.col-xl-12 > form:nth-child(1) > div:nth-child(11) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
        inputElement = firefox.find_element_by_css_selector(UC_STEP_CSS)
        inputElement.send_keys(uc_step_txt)

    except:
        print('Cant write Use Case Expected Result')        
        
      
def ui_press_uc_submit():

    try:
        
        UC_SUBMIT_XPATH = '/html/body/div/div/div[2]/div/div/div/form/button'      
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_SUBMIT_XPATH)))
        element.click()      
        
    except:
        print('Cant press Submit button')     


def ui_check_improper_uc():
    
    result = []
    
    TITLE_MISSING_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[1]/div'
    EXPECTED_MISSING_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[3]/div'
    STEP_MISSING = '/html/body/div/div/div[2]/div/div/div/form/div[5]/div/div/div'
    
    if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/use-cases':
        print('Use Case created, imporeper login - FAILED')
        return "FAILED"
        
    elif firefox.current_url == 'https://qa-sandbox.apps.htec.rs/create-usecase':
            
        try:
            if firefox.find_element_by_xpath(TITLE_MISSING_XPATH).is_displayed():
                print('Check "Title is required" visible - PASSED')
                result.append('Check "Title is required" visible - PASSED')
                return "PASSED"
            
        except:
            pass
        try:
            if firefox.find_element_by_xpath(EXPECTED_MISSING_XPATH).is_displayed():
                print('Check "Expected result is required" visible - PASSED')
                result.append('Check "Expected result is required" visible - PASSED')
                return 'PASSED'
                
        except:
            pass
        try:
            if firefox.find_element_by_xpath(STEP_MISSING).is_displayed():
                print('Check "There must be at least one test step" visible - PASSED')
                result.append('Check "There must be at least one test step" visible - PASSED')
                return 'PASSED'
                
        except:
            return "ERORR"
    

def ui_logout():
    
    try:
        
        LOGOUT_XPATH = '/html/body/div/div/nav/div/div/ul/li[4]/a'      
        element = wait.until(EC.element_to_be_clickable((By.XPATH, LOGOUT_XPATH)))
        element.click()      
        
    except:
        print('Cant logout')            


def ui_check_logout():
    
    try:
        
        if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/':
            print('Logout successful - PASSED')
            return 'PASSED'
        
        else:
            print('Logout unsuccessful - FAILED')
            return 'FAILED'
    
    except:
        print('Cant check logout')    
        return 'ERROR'
    

 
# =============================================================================
# login('nikolacab@yahoo.com', 'HTEC2021')        
# time.sleep(2)
# check_login()
# check_improper_login()
# 
# login('nikolacabi@yahoo.com', 'HTEC202')
# time.sleep(2)
# check_login()
# check_improper_login()
# =============================================================================

ui_login('nikolacabi@yahoo.com', 'HTEC2021')
time.sleep(5)
ui_check_login()

#ui_del_uc(10)

# =============================================================================
# ui_add_use_case("Use Case 1", "Description 1", "Expected1", True, 3, ["Step 1", "Step 2", "Step 3"])
# time.sleep(1)
# ui_check_use_case(1, 1, "Use Case 1", "Description 1", "Expected1", True, 3, ["Step 1", "Step 2", "Step 3"])
# time.sleep(1)
# ui_change_use_case(1, 1, 3)
# time.sleep(1)
# ui_check_use_case(1, 1, "This field previously had 10 characters", "This field previously had 13 characters", "This field previously had 9 characters", True, 3, ["This field previously had 6 characters", "This field previously had 6 characters", "This field previously had 6 characters"])
# =============================================================================
