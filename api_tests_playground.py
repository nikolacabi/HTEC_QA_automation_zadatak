# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:04:14 2021

@author: Nikola
"""

import api_test_functions
import json
import random


def Clean_up():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_teams(token)
    api_test_functions.api_delete_all_projects(token)
    api_test_functions.api_delete_all_use_cases(token)


# =============================================================================
# LOGIN
# =============================================================================
def TC1_Proper_login():
    
    try:
        
        response = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)
    
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


def TC6_Update_technologies():
    
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


def TC10_Update_seniorities():
    
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


def TC14_Update_teams():
    
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
        api_test_functions.api_add_people(token, "vfbgeerbvebrerbgevsdfropbcdaserbyweiurberberbejh50")
        api_test_functions.api_add_people(token, "Славољуб")
        api_test_functions.api_add_people(token, r"!@#$%^&*()_+=-{}[]\\;:,.<>/?*")
        
        response = json.loads(api_test_functions.api_get_all_people(token).text)
        
        if (response[0]['people_name'] == "!@#$%^&*()_+=-{}[]\\;:,.<>/?*" and response[1]['people_name'] == "Славољуб" 
            and response[2]['people_name'] == "vfbgeerbvebrerbgevsdfropbcdaserbyweiurberberbejh50" and response[3]['people_name'] == "John"
            and response[4]['people_name'] == "1234567890" and response[5]['people_name'] == "Joe Doe" 
            and response[6]['people_name'] == "Jonathan"):
            return "PASSED" 
        else:
            return "FAILED"
    
    except:
        return "ERROR" 


# All possible combinations of volontery fields
def TC17_Create_people_other_fields():
    
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
        if Joe2['seniority'] or Joe2['technologies'][0]['technology_id']!=tech1_id or Joe2['role']:
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


def TC18_Create_people_invalid_name():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]     
    api_test_functions.api_delete_all_people(token)

    try:
        response1 = json.loads(api_test_functions.api_add_people(token, "Joe").text)
        response2 = json.loads(api_test_functions.api_add_people(token, "vfbgeerbvebrerbgevsdfropbcdaserbyweiurberberbeyjh51").text)        
        response3 = json.loads(api_test_functions.api_add_people(token, " ").text)  
        
        if response1=={'people_name': 'Full name needs to be between 4 and 50'} and response1==response2 and response3=={'people_name': 'Full name field is required'}:
            return "PASSED"
        else:
            return "FAILED"
    
    except:
        return "ERROR"  
    

def TC19_Create_people_invalid_fields():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_teams(token)
    
    res = "T"
       
    try:
        tech1_id = random.randint(1000, 9999)
        tech2_id = random.randint(1000, 9999)
        sen1_id = random.randint(1000, 9999)
        team1_id = random.randint(1000, 9999)
                                         
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)
        if Joe1['role_id'] != "Role id " + str(team1_id) + " doesn't exist":
            res = 'F'
                  
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        if Joe2['technology_id'][0].replace("'","") != 'Technology id ' + str(tech1_id) + " doesnt exist":
            res = 'F'
        
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)
        if Joe3['seniority_id'] != "Seniority id " + str(sen1_id) + " doesn't exist":
            res = 'F'
                    
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)
        if Joe4['technology_id'][0].replace("'","") != "Technology id " + str(tech1_id) + " doesnt exist" or Joe4['technology_id'][1].replace("'","") !=  "Technology id " + str(tech2_id) + " doesnt exist" or Joe4['role_id'] != "Role id " + str(team1_id) + " doesn't exist":
            res = 'F'                    
                    
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        if Joe5['seniority_id'] != "Seniority id " + str(sen1_id) + " doesn't exist" or Joe5['role_id'] != "Role id " + str(team1_id) + " doesn't exist":
            res = 'F'
        
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        if Joe6['seniority_id'] != "Seniority id " + str(sen1_id) + " doesn't exist" or Joe6['technology_id'][0].replace("'","") != "Technology id " + str(tech2_id) + " doesnt exist":
            res = 'F'        
        
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        if Joe7['seniority_id'] != "Seniority id " + str(sen1_id) + " doesn't exist" or Joe7['technology_id'][0].replace("'","") != "Technology id " + str(tech2_id) + " doesnt exist" or Joe7['technology_id'][1].replace("'","") !=  "Technology id " + str(tech1_id) + " doesnt exist" or Joe7['role_id'] != "Role id " + str(team1_id) + " doesn't exist":
            res = 'F'   
                
        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 


def TC20_Update_people_existing_fields():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_teams(token)
    
    res = "T"
       
    try:
        tech1_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech1").text))['technology_id']
        tech2_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech2").text))['technology_id']
        tech3_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech3").text))['technology_id']
        tech4_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech4").text))['technology_id']
        sen1_id = (json.loads(api_test_functions.api_add_seniorities(token, "L1").text))['seniority_id']
        sen2_id = (json.loads(api_test_functions.api_add_seniorities(token, "L2").text))['seniority_id']
        team1_id = (json.loads(api_test_functions.api_add_teams(token, "Team1").text))['role_id']
        team2_id = (json.loads(api_test_functions.api_add_teams(token, "Team2").text))['role_id']
                                         
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text) 
        Joe1 = json.loads(api_test_functions.api_change_people(token, Joe1['people_id'], "Joe11", sen='', technologies=[], role=team2_id).text)      
        if Joe1['people_name']!="Joe11" or Joe1['seniority'] or Joe1['technologies']!=[] or Joe1['role']['role_id']!=team2_id:
            res = 'F'
                  
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        Joe2 = json.loads(api_test_functions.api_change_people(token, Joe2['people_id'], "Joe22", sen='', technologies=[tech2_id], role='').text)   
        if Joe2['people_name']!="Joe22" or Joe2['seniority'] or Joe2['technologies'][0]['technology_id']!=tech2_id or Joe2['role']:
            res = 'F'

        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)
        Joe3 = json.loads(api_test_functions.api_change_people(token, Joe3['people_id'], "Joe33", sen=sen2_id, technologies=[], role='').text)
        if Joe3['people_name']!="Joe33" or Joe3['seniority']['seniority_id']!=sen2_id or Joe3['technologies']!=[] or Joe3['role']:
            res = 'F'
   
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)
        Joe4 = json.loads(api_test_functions.api_change_people(token, Joe4['people_id'], "Joe44", sen='', technologies=[tech3_id, tech4_id], role=team2_id).text)
        if Joe4['people_name']!="Joe44" or Joe4['seniority'] or Joe4['technologies'][0]['technology_id']!=tech3_id or Joe4['technologies'][1]['technology_id']!=tech4_id or Joe4['role']['role_id']!=team2_id:
            res = 'F'                    
    
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        Joe5 = json.loads(api_test_functions.api_change_people(token, Joe5['people_id'], "Joe55", sen=sen2_id, technologies=[], role=team2_id).text)
        if Joe5['people_name']!="Joe55" or Joe5['seniority']['seniority_id']!=sen2_id or Joe5['technologies']!=[] or Joe5['role']['role_id']!=team2_id:
            res = 'F'

        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe6 = json.loads(api_test_functions.api_change_people(token, Joe6['people_id'], "Joe66", sen=sen2_id, technologies=[tech3_id], role='').text)
        if Joe6['people_name']!="Joe66" or Joe6['seniority']['seniority_id']!=sen2_id or Joe6['technologies'][0]['technology_id']!=tech3_id or Joe6['role']:
            res = 'F'        

        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe7 = json.loads(api_test_functions.api_change_people(token, Joe7['people_id'], "Joe77", sen=sen2_id, technologies=[tech3_id, tech4_id], role=team2_id).text)       
        if Joe7['people_name']!="Joe77" or Joe7['seniority']['seniority_id']!=sen2_id or Joe7['technologies'][0]['technology_id']!=tech3_id or Joe7['technologies'][1]['technology_id']!=tech4_id or Joe7['role']['role_id']!=team2_id:
            res = 'F'   

        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 


def TC21_Update_people_add_fields():
    
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
        
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0").text) 
        Joe0 = json.loads(api_test_functions.api_change_people(token, Joe0['people_id'], "Joe0", sen='', technologies=[], role='').text)      
        if Joe0['people_name']!="Joe0" or Joe0['seniority'] or Joe0['technologies']!=[] or Joe0['role']:
            res = 'F'
                                         
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1").text) 
        Joe1 = json.loads(api_test_functions.api_change_people(token, Joe1['people_id'], "Joe1", sen='', technologies=[], role=team1_id).text)      
        if Joe1['people_name']!="Joe1" or Joe1['seniority'] or Joe1['technologies']!=[] or Joe1['role']['role_id']!=team1_id:
            res = 'F'
                  
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2").text)
        Joe2 = json.loads(api_test_functions.api_change_people(token, Joe2['people_id'], "Joe2", sen='', technologies=[tech1_id], role='').text)   
        if Joe2['people_name']!="Joe2" or Joe2['seniority'] or Joe2['technologies'][0]['technology_id']!=tech1_id or Joe2['role']:
            res = 'F'

        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3").text)
        Joe3 = json.loads(api_test_functions.api_change_people(token, Joe3['people_id'], "Joe3", sen=sen1_id, technologies=[], role='').text)
        if Joe3['people_name']!="Joe3" or Joe3['seniority']['seniority_id']!=sen1_id or Joe3['technologies']!=[] or Joe3['role']:
            res = 'F'
   
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4").text)
        Joe4 = json.loads(api_test_functions.api_change_people(token, Joe4['people_id'], "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)
        if Joe4['people_name']!="Joe4" or Joe4['seniority'] or Joe4['technologies'][0]['technology_id']!=tech1_id or Joe4['technologies'][1]['technology_id']!=tech2_id or Joe4['role']['role_id']!=team1_id:
            res = 'F'                    
    
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5").text)
        Joe5 = json.loads(api_test_functions.api_change_people(token, Joe5['people_id'], "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        if Joe5['people_name']!="Joe5" or Joe5['seniority']['seniority_id']!=sen1_id or Joe5['technologies']!=[] or Joe5['role']['role_id']!=team1_id:
            res = 'F'

        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6").text)
        Joe6 = json.loads(api_test_functions.api_change_people(token, Joe6['people_id'], "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        if Joe6['people_name']!="Joe6" or Joe6['seniority']['seniority_id']!=sen1_id or Joe6['technologies'][0]['technology_id']!=tech2_id or Joe6['role']:
            res = 'F'        

        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7").text)
        Joe7 = json.loads(api_test_functions.api_change_people(token, Joe7['people_id'], "Joe7", sen=sen1_id, technologies=[tech1_id, tech2_id], role=team1_id).text)       
        if Joe7['people_name']!="Joe7" or Joe7['seniority']['seniority_id']!=sen1_id or Joe7['technologies'][0]['technology_id']!=tech1_id or Joe7['technologies'][1]['technology_id']!=tech2_id or Joe7['role']['role_id']!=team1_id:
            res = 'F'   

        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 


def TC22_Update_people_remove_fields():
    
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
        
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe0 = json.loads(api_test_functions.api_change_people(token, Joe0['people_id'], "Joe0", sen='', technologies=[], role='').text)      
        if Joe0['people_name']!="Joe0" or Joe0['seniority'] or Joe0['technologies']!=[] or Joe0['role']:
            res = 'F'
                                         
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe1 = json.loads(api_test_functions.api_change_people(token, Joe1['people_id'], "Joe1", sen='', technologies=[], role=team1_id).text)      
        if Joe1['people_name']!="Joe1" or Joe1['seniority'] or Joe1['technologies']!=[] or Joe1['role']['role_id']!=team1_id:
            res = 'F'
                  
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe2 = json.loads(api_test_functions.api_change_people(token, Joe2['people_id'], "Joe2", sen='', technologies=[tech1_id], role='').text)   
        if Joe2['people_name']!="Joe2" or Joe2['seniority'] or Joe2['technologies'][0]['technology_id']!=tech1_id or Joe2['role']:
            res = 'F'

        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe3 = json.loads(api_test_functions.api_change_people(token, Joe3['people_id'], "Joe3", sen=sen1_id, technologies=[], role='').text)
        if Joe3['people_name']!="Joe3" or Joe3['seniority']['seniority_id']!=sen1_id or Joe3['technologies']!=[] or Joe3['role']:
            res = 'F'
   
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe4 = json.loads(api_test_functions.api_change_people(token, Joe4['people_id'], "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)
        if Joe4['people_name']!="Joe4" or Joe4['seniority'] or Joe4['technologies'][0]['technology_id']!=tech1_id or Joe4['technologies'][1]['technology_id']!=tech2_id or Joe4['role']['role_id']!=team1_id:
            res = 'F'                    
    
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe5 = json.loads(api_test_functions.api_change_people(token, Joe5['people_id'], "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        if Joe5['people_name']!="Joe5" or Joe5['seniority']['seniority_id']!=sen1_id or Joe5['technologies']!=[] or Joe5['role']['role_id']!=team1_id:
            res = 'F'

        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe6 = json.loads(api_test_functions.api_change_people(token, Joe6['people_id'], "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        if Joe6['people_name']!="Joe6" or Joe6['seniority']['seniority_id']!=sen1_id or Joe6['technologies'][0]['technology_id']!=tech2_id or Joe6['role']:
            res = 'F'        

        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe7 = json.loads(api_test_functions.api_change_people(token, Joe7['people_id'], "Joe7", sen=sen1_id, technologies=[tech1_id, tech2_id], role=team1_id).text)       
        if Joe7['people_name']!="Joe7" or Joe7['seniority']['seniority_id']!=sen1_id or Joe7['technologies'][0]['technology_id']!=tech1_id or Joe7['technologies'][1]['technology_id']!=tech2_id or Joe7['role']['role_id']!=team1_id:
            res = 'F'   

        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 


def TC23_Create_existing_people():
    
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
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)
        if Joe1 != {'people_name': 'Joe1 already exists'}:
            res = 'F'
                  
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        if Joe2 != {'people_name': 'Joe2 already exists'}:
            res = 'F'
            
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)
        if Joe3 != {'people_name': 'Joe3 already exists'}:
            res = 'F'
                    
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)
        if Joe4 != {'people_name': 'Joe4 already exists'}:
            res = 'F'                
                    
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        if Joe5 != {'people_name': 'Joe5 already exists'}:
            res = 'F'
        
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        if Joe6 != {'people_name': 'Joe6 already exists'}:
            res = 'F'      
        
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        if Joe7 != {'people_name': 'Joe7 already exists'}:
            res = 'F'   
                
        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 


def TC24_Delete_team_from_people():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_projects(token)
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
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen='', technologies=[], role='').text)
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)                
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)                  
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)                 
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
               
        api_test_functions.api_delete_teams(token, team1_id)
        
        response_wo_team = json.loads(api_test_functions.api_get_all_people(token).text)
        
        for i in range (0,8):
            if response_wo_team[i]['role']:
                res = "F"
        
        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 
    
    
def TC25_Delete_seniorities_from_people():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_projects(token)
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
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen='', technologies=[], role='').text)
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)                
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)                  
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)                 
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
               
        api_test_functions.api_delete_seniorities(token, sen1_id)
        
        response_wo_sen = json.loads(api_test_functions.api_get_all_people(token).text)
        
        for i in range (0,8):
            if response_wo_sen[i]['seniority']:
                res = "F"
        
        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 
        
    
def TC26_Delete_1_technologies_from_people():
     
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_projects(token)
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
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen='', technologies=[], role='').text)
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)                
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)                  
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)                 
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
               
        api_test_functions.api_delete_technologies(token, tech1_id)
        
        response_wo_tech = json.loads(api_test_functions.api_get_all_people(token).text)
        
        if (len(response_wo_tech[0]['technologies']) != 1 or len(response_wo_tech[1]['technologies']) != 1
            or len(response_wo_tech[0]['technologies']) != 1 or response_wo_tech[5]['technologies'] != []):
                res = "F"
        
        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 
            

def TC27_Delete_seniorities_from_people():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_projects(token)
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
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen='', technologies=[], role='').text)
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)                
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)                  
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)                 
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
               
        api_test_functions.api_delete_all_technologies(token)
        
        response_wo_sen = json.loads(api_test_functions.api_get_all_people(token).text)
        
        for i in range (0,8):
            if response_wo_sen[i]['technologies'] != []:
                res = "F"
        
        if res == "F":
            return "FAILED" 
        else:
            return "PASSED"
    
    except:
        return "ERROR" 


# =============================================================================
# PROJECTS
# =============================================================================
def TC28_Create_Projects_valid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_projects(token)
       
    try:
        api_test_functions.api_add_projects(token, "New Project")
        api_test_functions.api_add_projects(token, "Project")
        api_test_functions.api_add_projects(token, "1234567890")
        api_test_functions.api_add_projects(token, "P")
        api_test_functions.api_add_projects(token, "vfbgeerbvebrerbgerberberbejh30")
        api_test_functions.api_add_projects(token, "Пројекат")
        api_test_functions.api_add_projects(token, r"!@#$%^&*()_+=-{}[]\\;:,.<>/?*")
        
        response = json.loads(api_test_functions.api_get_all_projects(token).text)
        
        if (response[0]['project_title'] == "!@#$%^&*()_+=-{}[]\\;:,.<>/?*" and response[1]['project_title'] == "Пројекат" 
            and response[2]['project_title'] == "vfbgeerbvebrerbgerberberbejh30" and response[3]['project_title'] == "P"
            and response[4]['project_title'] == "1234567890" and response[5]['project_title'] == "Project" 
            and response[6]['project_title'] == "New Project"):
            return "PASSED" 
        else:
            return "FAILED"
    
    except:
        return "ERROR" 


def TC29_Create_Projects_add_people():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    
    api_test_functions.api_delete_all_projects(token)
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_teams(token)
          
    try:
    
        tech1_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech1").text))['technology_id']
        tech2_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech2").text))['technology_id']
        sen1_id = (json.loads(api_test_functions.api_add_seniorities(token, "L1").text))['seniority_id']
        team1_id = (json.loads(api_test_functions.api_add_teams(token, "Team1").text))['role_id']
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen='', technologies=[], role='').text)
        Joe1 = json.loads(api_test_functions.api_add_people(token, "Joe1", sen='', technologies=[], role=team1_id).text)                
        Joe2 = json.loads(api_test_functions.api_add_people(token, "Joe2", sen='', technologies=[tech1_id], role='').text)
        Joe3 = json.loads(api_test_functions.api_add_people(token, "Joe3", sen=sen1_id, technologies=[], role='').text)                  
        Joe4 = json.loads(api_test_functions.api_add_people(token, "Joe4", sen='', technologies=[tech1_id, tech2_id], role=team1_id).text)                 
        Joe5 = json.loads(api_test_functions.api_add_people(token, "Joe5", sen=sen1_id, technologies=[], role=team1_id).text)
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        
        Pro1 = json.loads(api_test_functions.api_add_projects(token, "Project1", people=[Joe0['people_id'], Joe1['people_id'], Joe2['people_id'], Joe3['people_id'], Joe4['people_id'], Joe5['people_id'], Joe6['people_id'] , Joe7['people_id']]).text)
        
        if (Pro1['roles'][0]['role_name'] or Pro1['roles'][0]['role_id'] or len(Pro1['roles'][0]['people']) != 4 or 
            Pro1['roles'][1]['role_name'] != 'Team1' or Pro1['roles'][1]['role_id'] != 3296 or len(Pro1['roles'][1]['people']) != 4):
            return "FAILED" 
        else:
            return "PASSED"        

    except:
        return "ERROR" 


def TC30_Create_Projects_invalid():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_projects(token)  

    try:
        response1 = json.loads(api_test_functions.api_add_projects(token, " ").text)
        response2 = json.loads(api_test_functions.api_add_projects(token, "vfbgeerbvebrerbgerberberberjw31").text)        

        if response1=={'project_title': 'Title is required'} and response2=={'project_title': 'Title needs to be between 1 and 30'}:
            return "PASSED"
        else:
            return "FAILED"
    
    except:
        return "ERROR"  


def TC31_Create_Projects_add_ivalid_people():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    
    api_test_functions.api_delete_all_projects(token)
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_teams(token)
          
    try:
            
        Joe0 = random.randint(1000, 9999)
        Joe1 = random.randint(1000, 9999)               
        
        Pro1 = json.loads(api_test_functions.api_add_projects(token, "Project1", people=[Joe0, Joe1]).text)
        
        if Pro1['people_id'][0] != "Person id " + str(Joe0) + " doesn't exist" or Pro1['people_id'][1] != "Person id " + str(Joe1) + " doesn't exist":
            return "FAILED" 
        else:
            return "PASSED"        

    except:
        return "ERROR" 


def TC32_Update_Projects():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    
    api_test_functions.api_delete_all_projects(token)
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_teams(token)
          
    try:
                    
        tech1_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech1").text))['technology_id']
        tech2_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech2").text))['technology_id']
        sen1_id = (json.loads(api_test_functions.api_add_seniorities(token, "L1").text))['seniority_id']
        team1_id = (json.loads(api_test_functions.api_add_teams(token, "Team1").text))['role_id']
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen='', technologies=[], role='').text)              
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        
        Pro1 = json.loads(api_test_functions.api_add_projects(token, "Project1", people=[Joe0['people_id'], Joe7['people_id']]).text)
        Pro1 = json.loads(api_test_functions.api_change_projects(token, Pro1['project_id'],"Project2", people=[Joe6['people_id'], Joe7['people_id']]).text)   
        if Pro1['project_title'] != "Project2" or Pro1['roles'][0]['people'][0]['people_name'] != "Joe6" or Pro1['roles'][1]['people'][0]['people_name'] != "Joe7":
            return "FAILED" 
        else:
            return "PASSED"        

    except:
        return "ERROR" 


def TC33_Create_existing_Projects():
    
    token = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]
    api_test_functions.api_delete_all_projects(token)
    api_test_functions.api_delete_all_people(token)
    api_test_functions.api_delete_all_technologies(token)
    api_test_functions.api_delete_all_seniorities(token)
    api_test_functions.api_delete_all_teams(token)
       
    try:

        tech1_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech1").text))['technology_id']
        tech2_id = (json.loads(api_test_functions.api_add_technologies(token, "Tech2").text))['technology_id']
        sen1_id = (json.loads(api_test_functions.api_add_seniorities(token, "L1").text))['seniority_id']
        team1_id = (json.loads(api_test_functions.api_add_teams(token, "Team1").text))['role_id']
        Joe0 = json.loads(api_test_functions.api_add_people(token, "Joe0", sen='', technologies=[], role='').text)              
        Joe6 = json.loads(api_test_functions.api_add_people(token, "Joe6", sen=sen1_id, technologies=[tech2_id], role='').text)
        Joe7 = json.loads(api_test_functions.api_add_people(token, "Joe7", sen=sen1_id, technologies=[tech2_id, tech1_id], role=team1_id).text)
        
        
        Pro1 = json.loads(api_test_functions.api_add_projects(token, "Project1", people=[Joe0['people_id'], Joe6['people_id'], Joe7['people_id']]).text)
        Pro1 = json.loads(api_test_functions.api_add_projects(token, "Project1", people=[Joe0['people_id'], Joe6['people_id'], Joe7['people_id']]).text)
        if Pro1 != {'project_title': 'Project1 already exists'}:
            return "FAILED" 
        else:
            return "PASSED"        
    
    except:
        return "ERROR" 


def TC34_Multiple_Login_atempts():
        
    try:
        for i in range (0, 11):
            api_test_functions.api_login('nikolacabi@yahoo.com', str(random.randint(100000, 999999)))
             
        response = json.loads(api_test_functions.api_login('nikolacabi@yahoo.com', 'HTEC2021').text)  
        if response['success'] == True:
            return "FAILED"
        else:
            return "PASSED"
    except:
        return "ERROR"    
    


