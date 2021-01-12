# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:04:14 2021

@author: Nikola
"""

import api_test_functions
import json


def Clean_up():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_teams(token)
    api_test_functions.api_delete_all_projects(token)


# =============================================================================
# LOGIN
# =============================================================================
def TC1_Proper_login():
    
    response = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)
    
    try:
        if response['success'] == True:
            return "PASSED"
        else:
            return "FAILED"
    except:
        return "ERROR"    
    

def TC2_Improper_login_password():
    
    response = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC202').text)
    
    try:
        if response == {'password': 'Password incorrect'}:
            return "PASSED"
        else:
            return "PASSED"
    except:
        return "ERROR"    
    

def TC3_Improper_login_email():
    
    response = json.loads(api_test_functions.api_login('nikolacabi@yahoo.co', 'HTEC2021').text)
    
    try:
        if response == {'email': 'User not found'}:
            return "PASSED"
        else:
            return "PASSED"
    except:
        return "ERROR"    


# =============================================================================
# TECHNOLOGIES
# =============================================================================
def TC4_Create_technologies_valid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_technologies(token)
       
    try:
        api_test_functions.api_add_technologies(token, "Tech and Tech")
        api_test_functions.api_add_technologies(token, "Tech")
        api_test_functions.api_add_technologies(token, "1234567890")
        api_test_functions.api_add_technologies(token, "T1")
        api_test_functions.api_add_technologies(token, "vfbgeerbvebrerbgerberberbejh30")
        api_test_functions.api_add_technologies(token, "технологија")
        api_test_functions.api_add_technologies(token, r"!@#$%^&*()_+=-{}[]\\;:,.<>/?*")
        
        response = json.loads(api_test_functions.api_get_all_technologies(token).text)
        
        if (response[0]['technology_title'] == "!@#$%^&*()_+=-{}[]\\;:,.<>/?*" and response[1]['technology_title'] == "технологија" 
            and response[2]['technology_title'] == "vfbgeerbvebrerbgerberberbejh30" and response[3]['technology_title'] == "T1"
            and response[4]['technology_title'] == "1234567890" and response[5]['technology_title'] == "Tech" 
            and response[6]['technology_title'] == "Tech and Tech"):
            return "PASSED" 
        else:
            return "FAILED"
    
    except:
        return "ERROR"    
                    
        
def TC5_Create_technologies_invalid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]     
    api_test_functions.api_delete_all_technologies(token)

    try:
        response1 = json.loads(api_test_functions.api_add_technologies(token, "T").text)
        response2 = json.loads(api_test_functions.api_add_technologies(token, "vfbgeerbvebrerbgerberberberjw31").text) 
        response3 = json.loads(api_test_functions.api_add_technologies(token, " ").text)  
        
        if response1=={'technology_title': 'Title needs to be between 2 and 30'} and response1==response2 and response3=={'technology_title': 'Title is required'}:
            return "PASSED"
        else:
            return "FAILED"
    
    except:
        return "ERROR"  


def TC6_Upadete_technologies():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_technologies(token)
    
    try:
        response1 = json.loads(api_test_functions.api_add_technologies(token, "Tech3").text)
        response2 = json.loads(api_test_functions.api_change_technologies(token, response1['technology_id'], "Tech4").text)
        
        if response1['technology_id']==response2['technology_id'] and response2['technology_title']=='Tech4':
            return "PASSED"
        else:
            return "FAILED"

    except:
        return "ERROR"  
    
    
def TC7_Create_existing_technologies():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_technologies(token)
    
    try:
        api_test_functions.api_add_technologies(token, "Tech5")
        response1 = json.loads(api_test_functions.api_add_technologies(token, "Tech5").text)    

        if response1 == {'technology_title': 'Technology title already exists'}:
            return "PASSED"
        else:
            return "FAILED"

    except:
        return "ERROR"  



# =============================================================================
# SENIORITIES
# =============================================================================
def TC8_Create_seniorities_valid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_seniorities(token)
       
    try:
        api_test_functions.api_add_seniorities(token, "Medior level 3")
        api_test_functions.api_add_seniorities(token, "Medior")
        api_test_functions.api_add_seniorities(token, "1234567890")
        api_test_functions.api_add_seniorities(token, "L1")
        api_test_functions.api_add_seniorities(token, "vfbgeerbvebrerbgerberberbejh30")
        api_test_functions.api_add_seniorities(token, "Сениор")
        api_test_functions.api_add_seniorities(token, r"!@#$%^&*()_+=-{}[]\\;:,.<>/?*")
        
        response = json.loads(api_test_functions.api_get_all_seniorities(token).text)
        
        if (response[0]['seniority_title'] == "!@#$%^&*()_+=-{}[]\\;:,.<>/?*" and response[1]['seniority_title'] == "Сениор" 
            and response[2]['seniority_title'] == "vfbgeerbvebrerbgerberberbejh30" and response[3]['seniority_title'] == "L1"
            and response[4]['seniority_title'] == "1234567890" and response[5]['seniority_title'] == "Medior" 
            and response[6]['seniority_title'] == "Medior level 3"):
            return "PASSED" 
        else:
            return "FAILED"
    
    except:
        return "ERROR" 
                    
        
def TC9_Create_seniorities_invalid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]     
    api_test_functions.api_delete_all_seniorities(token)

    try:
        response1 = json.loads(api_test_functions.api_add_seniorities(token, "L").text)
        response2 = json.loads(api_test_functions.api_add_seniorities(token, "vfbgeerbvebrerbgerberberberjw31").text)        
        response3 = json.loads(api_test_functions.api_add_seniorities(token, " ").text)  
        
        if response1=={'seniority_title': 'Title needs to be between 2 and 30'} and response1==response2 and response3=={'seniority_title': 'Title is required'}:
            return "PASSED"
        else:
            return "FAILED"
    
    except:
        return "ERROR"  


def TC10_Upadete_seniorities():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_seniorities(token)
    
    try:
        response1 = json.loads(api_test_functions.api_add_seniorities(token, "lvl3").text)
        response2 = json.loads(api_test_functions.api_change_seniorities(token, response1['seniority_id'], "lvl4").text)
        
        if response1['seniority_id']==response2['seniority_id'] and response2['seniority_title']=='lvl4':
            return "PASSED"
        else:
            return "FAILED"

    except:
        return "ERROR"  
    
    
def TC11_Create_existing_seniorities():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_seniorities(token)
    
    try:
        api_test_functions.api_add_seniorities(token, "lvl5")
        response1 = json.loads(api_test_functions.api_add_seniorities(token, "lvl5").text)    

        if response1 == {'seniority_title': 'Seniority title already exists'}:
            return "PASSED"
        else:
            return "FAILED"

    except:
        return "ERROR"  


# =============================================================================
# TEAMS
# =============================================================================
def TC12_Create_teams_valid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_teams(token)
       
    try:
        api_test_functions.api_add_teams(token, "Big team")
        api_test_functions.api_add_teams(token, "Team")
        api_test_functions.api_add_teams(token, "1234567890")
        api_test_functions.api_add_teams(token, "T")
        api_test_functions.api_add_teams(token, "vfbgeerbvebrerbgerberberbejh30")
        api_test_functions.api_add_teams(token, "Тимчина")
        api_test_functions.api_add_teams(token, r"!@#$%^&*()_+=-{}[]\\;:,.<>/?*")
        
        response = json.loads(api_test_functions.api_get_all_teams(token).text)
        
        if (response[0]['role_name'] == "!@#$%^&*()_+=-{}[]\\;:,.<>/?*" and response[1]['role_name'] == "Тимчина" 
            and response[2]['role_name'] == "vfbgeerbvebrerbgerberberbejh30" and response[3]['role_name'] == "T"
            and response[4]['role_name'] == "1234567890" and response[5]['role_name'] == "Medior" 
            and response[6]['role_name'] == "Big team"):
            return "PASSED" 
        else:
            return "FAILED"
    
    except:
        return "ERROR" 
                    
        
def TC13_Create_teams_invalid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"] 
    api_test_functions.api_delete_all_teams(token)     

    try:
        response1 = json.loads(api_test_functions.api_add_teams(token, " ").text)
        response2 = json.loads(api_test_functions.api_add_teams(token, "vfbgeerbvebrerbgerberberberjw31").text)        

        if response1=={'role_name': 'Role name is required'} and response2=={'role_name': 'Role name needs to be between 1 and 30'}:
            return "PASSED"
        else:
            return "FAILED"
    
    except:
        return "ERROR"  


def TC14_Upadete_teams():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_teams(token)
    
    try:
        response1 = json.loads(api_test_functions.api_add_teams(token, "Team3").text)
        response2 = json.loads(api_test_functions.api_change_teams(token, response1['seniority_id'], "Team4").text)
        
        if response1['role_id']==response2['role_id'] and response2['role_id']=='Team4':
            return "PASSED"
        else:
            return "FAILED"

    except:
        return "ERROR"  
    
    
def TC15_Create_existing_teams():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_teams(token)
    
    try:
        api_test_functions.api_add_teams(token, "Team5")
        response1 = json.loads(api_test_functions.api_add_teams(token, "Team5").text)    

        if response1 == {'seniority_title': 'Seniority title already exists'}:
            return "PASSED"
        else:
            return "FAILED"

    except:
        return "ERROR"  



# =============================================================================
# PEOPLE
# =============================================================================
def TC16_Create_people_valid_name():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_people(token)
       
    try:
        api_test_functions.api_add_people(token, "Jonathan")
        api_test_functions.api_add_people(token, "Joe Doe")        
        api_test_functions.api_add_people(token, "1234567890")
        api_test_functions.api_add_people(token, "John")
        api_test_functions.api_add_people(token, "vfbgeerbvebrerbgerberberbejh30")
        api_test_functions.api_add_people(token, "Славољуб")
        api_test_functions.api_add_people(token, r"!@#$%^&*()_+=-{}[]\\;:,.<>/?*")
        
        response = json.loads(api_test_functions.api_get_all_people(token).text)
        
        if (response[0]['role_name'] == "!@#$%^&*()_+=-{}[]\\;:,.<>/?*" and response[1]['role_name'] == "Славољуб" 
            and response[2]['role_name'] == "vfbgeerbvebrerbgerberberbejh30" and response[3]['role_name'] == "John"
            and response[4]['role_name'] == "1234567890" and response[5]['role_name'] == "Joe Doe" 
            and response[6]['role_name'] == "Jonathan"):
            return "PASSED" 
        else:
            return "FAILED"
    
    except:
        return "ERROR" 


def TC16_Create_people_other_inputs():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_teams(token)
    
    res = "T"
       
    try:
        tech1_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech1").text))['technology_id']
        tech2_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech2").text))['technology_id']
        sen1_id = (json.loads(api_test_functions.api_add_seniorities(token, "L1").text))['seniority_id']
        team1_id = (json.loads(api_test_functions.api_add_teams(token, "Team1").text))['role_id']
                                         
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)
        if Joe1['seniority'] or Joe1['technologies']!=[] or Joe1['role']['role_id']!=team1_id:
            res = 'F'
                  
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        if Joe2['seniority'] or Joe2['technologies'][0]['technology_id']!=[tech1_id] or Joe2['role']:
            res = 'F'
        
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)
        if Joe3['seniority']['seniority_id']!=sen1_id or Joe3['technologies']!=[] or Joe3['role']:
            res = 'F'
                    
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)
        if Joe4['seniority'] or Joe4['technologies'][0]['technology_id']!=tech1_id or Joe4['technologies'][1]['technology_id']!=tech2_id or Joe4['role']['role_id']!=team1_id:
            res = 'F'                    
                    
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        if Joe5['seniority']['seniority_id']!=sen1_id or Joe5['technologies']!=[] or Joe5['role']['role_id']!=team1_id:
            res = 'F'
        
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        if Joe6['seniority']['seniority_id']!=sen1_id or Joe6['technologies'][0]['technology_id']!=tech2_id or Joe6['role']:
            res = 'F'        
        
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        if Joe7['seniority']['seniority_id']!=sen1_id or Joe7['technologies'][0]['technology_id']!=tech2_id or Joe7['technologies'][1]['technology_id']!=tech1_id or Joe7['role']['role_id']!=team1_id:
            res = 'F'   
                
        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 

















# =============================================================================
# MAIN
# =============================================================================
Clean_up()

api_test_run = {}

# =============================================================================
# api_test_run['TC1_Login'] = TC1_Proper_login()
# api_test_run['TC2_Improper_login_password'] = TC2_Improper_login_password()
# api_test_run['TC3_Improper_login_email'] = TC3_Improper_login_email() 
# 
# api_test_run['TC4_Create_technologies_valid'] = TC4_Create_technologies_valid() 
# api_test_run['TC5_Create_technologies_invalid'] = TC5_Create_technologies_invalid() 
# api_test_run['TC6_Upadete_technologies'] = TC6_Upadete_technologies() 
# api_test_run['TC7_Create_existing_technologies'] = TC7_Create_existing_technologies() 
# =============================================================================

# =============================================================================
# api_test_run['TC8_Create_seniorities_valid'] = TC8_Create_seniorities_valid() 
# api_test_run['TC9_Create_seniorities_invalid'] = TC9_Create_seniorities_invalid() 
# api_test_run['TC10_Upadete_seniorities'] = TC10_Upadete_seniorities() 
# api_test_run['TC11_Create_existing_seniorities'] = TC11_Create_existing_seniorities() 
# =============================================================================

api_test_run['TC12_Create_teams_valid'] = TC12_Create_teams_valid() 
api_test_run['TC13_Create_teams_invalid'] = TC13_Create_teams_invalid() 
api_test_run['TC14_Upadete_teams'] = TC14_Upadete_teams() 
api_test_run['TC15_Create_existing_teams'] = TC15_Create_existing_teams() 




