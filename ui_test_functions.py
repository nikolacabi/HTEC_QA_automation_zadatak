# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 23:39:50 2021

@author: Nikola
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
            
        else:
            print('Check login - FAILED')
            
    except:
        print("Login cant be verifed")
    
    
def ui_check_improper_login():
    
    USER_NOT_FOUND_XPATH = "/html/body/div/div/div[2]/div/div/div/div/form/div[1]/div"
    PASSWORD_INCORRECT_XPATH = "/html/body/div/div/div[2]/div/div/div/div/form/div[2]/div"
    
    try:      
        if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/login' and firefox.find_element_by_xpath(USER_NOT_FOUND_XPATH).is_displayed():
            print('Check login user not found - PASSED')
    except:
        pass
            
    try:        
        if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/login' and firefox.find_element_by_xpath(PASSWORD_INCORRECT_XPATH).is_displayed():  
            print('Check login incorrect password - PASSED')
    except:
        pass     
                    

def ui_add_use_case(uc_title_txt, uc_desc_txt, uc_exp_txt, uc_auto, uc_step_count, uc_step_txt):
        
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/use-cases"
        firefox.get(URL)
        
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
        
        if uc_auto:
            UC_AUTOMATED_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[4]/div/div/label'
            element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_AUTOMATED_XPATH)))
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
    
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/use-cases"
        firefox.get(URL)
        
        if tot == 1:
            uc_xpath = '/html/body/div/div/div[2]/div/div/a'
        else:
            uc_xpath = '/html/body/div/div/div[2]/div/div/a[' + str(pos) + ']'
            
        element = wait.until(EC.element_to_be_clickable((By.XPATH, uc_xpath)))
        checkElement = firefox.find_element_by_xpath(uc_xpath)
        if checkElement.text == uc_title_txt:
            print('Check Title outside - PASSED')
        else:
            print('Check Title outside - FAILED')
                                     
        element = firefox.find_element_by_xpath(uc_xpath)
        element.click()
        
        UC_TITLE_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[1]/input'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_TITLE_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_TITLE_XPATH)
        if checkElement.get_attribute('value') == uc_title_txt:
            print('Check Title inside - PASSED')
        else:
            print('Check Title inside - FAILED')
            print(checkElement.get_attribute('value'))

        
        UC_DESC_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[2]/textarea"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_DESC_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_DESC_XPATH)
        if checkElement.get_attribute('value') == uc_desc_txt:
            print('Check Description  - PASSED')
        else:
            print('Check Description - FAILED')
            print(checkElement.get_attribute('value'))
        
        
        UC_EXP_XPATH = "/html/body/div/div/div[2]/div/div/div/form/div[3]/input"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, UC_EXP_XPATH)))
        checkElement = firefox.find_element_by_xpath(UC_EXP_XPATH)
        if checkElement.get_attribute('value') == uc_exp_txt:
            print('Check Expected - PASSED')
        else:
            print('Check Expected - FAILED')
            print(checkElement.get_attribute('value'))
            
        
        UC_AUTOMATED_XPATH = '//*[@id="switch"]'
        checkElement = firefox.find_element_by_xpath(UC_AUTOMATED_XPATH)
        if checkElement.get_attribute('value') == uc_auto:
            print('Check Automated? - PASSED')
        else:
            print('Check Automated? - FAILED')
            print(checkElement.get_attribute('value'))
            
        
        for i in range (0, uc_step_count):
                           
            step_css = '.col-xl-12 > form:nth-child(1) > div:nth-child(' + str(12 + i) + ') > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, step_css)))
            checkElement = firefox.find_element_by_css_selector(step_css)
            if checkElement.get_attribute('value') == uc_step_txt[i]:
                print('Check Step', i+1, ' - PASSED')
            else:
                print('Check Step', i+1, ' - FAILED')
                print(checkElement.get_attribute('value'))
                                   
    except:
        print("Use Case cant be checked")
                 
        
def ui_change_use_case(pos, tot, uc_step_count):
    
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/use-cases"
        firefox.get(URL)
        
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
        

def ui_start_uc_creating():
    
    try:
        
        URL = "https://qa-sandbox.apps.htec.rs/create-usecase"
        firefox.get(URL)
    
    except:
        print('Cant start Use Case creation')
                       
    
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
    
    TITLE_MISSING_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[1]/div'
    EXPECTED_MISSING_XPATH = '/html/body/div/div/div[2]/div/div/div/form/div[3]/div'
    STEP_MISSING = '/html/body/div/div/div[2]/div/div/div/form/div[5]/div/div/div'
    
    if firefox.current_url == 'https://qa-sandbox.apps.htec.rs/use-cases':
        print('Use Case created, imporeper login - FAILED')
        
    elif firefox.current_url == 'https://qa-sandbox.apps.htec.rs/create-usecase':
            
        try:
            if firefox.find_element_by_xpath(TITLE_MISSING_XPATH).is_displayed():
                print('Check "Title is required" visible - PASSED')
        except:
            pass
        try:
            if firefox.find_element_by_xpath(EXPECTED_MISSING_XPATH).is_displayed():
                print('Check "Expected result is required" visible - PASSED')
        except:
            pass
        try:
            if firefox.find_element_by_xpath(STEP_MISSING).is_displayed():
                print('Check "There must be at least one test step" visible - PASSED')
        except:
            pass
    
    
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
        
        else:
            print('Logout unsuccessful - FAILED')
    
    except:
        print('Cant check logout')    
    

 
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

ui_del_uc(10)  
time.sleep(2)
ui_check_logout()
time.sleep(2)

ui_start_uc_creating()
time.sleep(2)
ui_write_uc_title("Title1")
ui_write_uc_description('Desc1')
ui_write_uc_expected(' ')
ui_write_uc_step('UseCase1')
ui_press_uc_submit()
time.sleep(1)
ui_check_improper_uc()
time.sleep(1)
ui_logout()
time.sleep(1)
ui_check_logout()

time.sleep(2)
ui_check_use_case(1, 1, "Title1", "Desc1", "Expected1", 'false', 1, ['UseCase1'])

ui_login('nikolacabi@yahoo.com', 'HTEC2021')
time.sleep(4)
ui_check_login()
ui_del_uc(10)        
ui_add_use_case("Title1", "Desc1", "Expected1", True, 3, ['UseCase1', 'UseCase2', 'UseCase3'])
time.sleep(2)
ui_check_use_case(1, 1, "Title1", "Desc1", "Expected1", 'true', 3, ['UseCase1', 'UseCase2', 'UseCase3'])
ui_check_use_case(1, 1, "Title1", "Desc1", "Expected1", 'false', 3, ['UseCase1', 'UseCase2', 'UseCase3'])
time.sleep(1)
ui_add_use_case("Title2", "Desc2", "Expected2", 2, ['UseCase1', 'UseCase2'])
time.sleep(1)
ui_check_use_case(1, 2, "Title2", "Desc2", "Expected2", 2, ['UseCase1', 'UseCase2'])
time.sleep(1)
ui_check_use_case(2, 2, "Title1", "Desc1", "Expected1", 3, ['UseCase1', 'UseCase2', 'UseCase3'])
time.sleep(1)
ui_add_use_case("Title3", "Desc3", "Expected3", 4, ['UseCase1', 'UseCase2', 'UseCase3', 'UseCase4'])
time.sleep(1)
ui_check_use_case(1, 3, "Title3", "Desc3", "Expected3", 4, ['UseCase1', 'UseCase2', 'UseCase3', 'UseCase4'])
time.sleep(1)
ui_check_use_case(3, 3, "Title1", "Desc1", "Expected1", 3, ['UseCase1', 'UseCase2', 'UseCase3'])
time.sleep(1)

# =============================================================================
# change_use_case(1, 1, 3)
# time.sleep(2)
# check_use_case(1, 1, "This field previously had " + str(len("Title1")) + " characters", "This field previously had " + str(len("Desc1")) + " characters", "This field previously had " + str(len("Expected1")) + " characters", 3, ["This field previously had " + str(len("UseCase1")) + " characters", "This field previously had " + str(len("UseCase2")) + " characters", "This field previously had " + str(len("UseCase3")) + " characters"])
# 
# =============================================================================
#del_uc(10)
