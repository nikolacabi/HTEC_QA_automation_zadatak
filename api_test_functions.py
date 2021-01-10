# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:14:32 2021

@author: Nikola
"""

import requests
import json


# =============================================================================
# LOGIN 
# =============================================================================
def api_login(un, pw):
    
    url = "https://qa-sandbox.apps.htec.rs/api/users/login"
    
    payload = "{\"email\":\"" + un + "\",\"password\":\"" + pw + "\"}"
    headers = {
        'host': "qa-sandbox.apps.htec.rs",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
        'accept': "application/json, text/plain, */*",
        'accept-language': "en-US,en;q=0.5",
        'accept-encoding': "gzip, deflate, br",
        'content-type': "application/json;charset=utf-8",
        'content-length': "54",
        'origin': "https://qa-sandbox.apps.htec.rs",
        'connection': "keep-alive",
        'cookie': "io=U5LAwe72mQOo7tAzATxo",
        'te': "Trailers",
        'cache-control': "no-cache",
        'postman-token': "8d2859b5-d293-a0a2-9860-40078137956a"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    #print(response.text)
    return response


# =============================================================================
# TECHNOLOGIES
# =============================================================================
def api_get_all_technologies(token):

    url = "https://qa-sandbox.apps.htec.rs/api/technologies/all"
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "42cda08a-89bd-f7b7-6eb1-f197be8d510f"
        }
    
    response = requests.request("GET", url, headers=headers)
    
    #print(response.text)
    return response    


def api_add_technologies(token, tech_title):
    
    url = "https://qa-sandbox.apps.htec.rs/api/technologies/technology"
    
    payload = "{\"technology_title\":\"" + tech_title + "\"}"
    headers = {
        'accept': "application/json, text/plain, */*",
        'authorization': "Bearer " + token,
        'content-type': "application/json;charset=utf-8",
        'content-length': str(23 + len(tech_title)),
        'cache-control': "no-cache",
        'postman-token': "6315b652-7f29-4370-9179-75d3f91c2d18"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    #print(response.text)
    return response    


def api_delete_all_technologies(token):
    
    all_tech = json.loads(api_get_all_technologies(token).text)
    
    for i in range(0, len(all_tech)):
        
        tech_id = all_tech[i]['technology_id']
        
        url = "https://qa-sandbox.apps.htec.rs/api/technologies/technology/" + str(tech_id)
        
        headers = {
            'authorization': "Bearer " + token,
            'cache-control': "no-cache",
            'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
            }
        
        response = requests.request("DELETE", url, headers=headers)
        

def api_delete_technologies(token, tech_id):
    
    url = "https://qa-sandbox.apps.htec.rs/api/technologies/technology/" + str(tech_id)
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
        }
    
    response = requests.request("DELETE", url, headers=headers)
    
    #print(response.text)
    return response


# =============================================================================
# SENIORITIES
# =============================================================================
def api_get_all_seniorities(token):

    url = "https://qa-sandbox.apps.htec.rs/api/seniorities/all"
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "42cda08a-89bd-f7b7-6eb1-f197be8d510f"
        }
    
    response = requests.request("GET", url, headers=headers)
    
    #print(response.text)
    return response    


def api_add_seniorities(token, sen_title):
    
    url = "https://qa-sandbox.apps.htec.rs/api/seniorities/seniority"
    
    payload = "{\"seniority_title\":\"" + sen_title + "\"}"
    headers = {
        'accept': "application/json, text/plain, */*",
        'authorization': "Bearer " + token,
        'content-type': "application/json;charset=utf-8",
        'content-length': str(22 + len(sen_title)),
        'cache-control': "no-cache",
        'postman-token': "6315b652-7f29-4370-9179-75d3f91c2d18"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    #print(response.text)
    return response    


def api_delete_all_seniorities(token):
    
    all_sen = json.loads(api_get_all_seniorities(token).text)
    
    for i in range(0, len(all_sen)):
        
        sen_id = all_sen[i]['seniority_id']
        
        url = "https://qa-sandbox.apps.htec.rs/api/seniorities/seniority/" + str(sen_id)
        
        headers = {
            'authorization': "Bearer " + token,
            'cache-control': "no-cache",
            'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
            }
        
        response = requests.request("DELETE", url, headers=headers)


def api_delete_seniorities(token, sen_id):
    
    url = "https://qa-sandbox.apps.htec.rs/api/seniorities/seniority/" + str(sen_id)
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
        }
    
    response = requests.request("DELETE", url, headers=headers)
    
    #print(response.text)
    return response


# =============================================================================
# TEAMS
# =============================================================================
def api_get_all_teams(token):

    url = "https://qa-sandbox.apps.htec.rs/api/roles/all"
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "42cda08a-89bd-f7b7-6eb1-f197be8d510f"
        }
    
    response = requests.request("GET", url, headers=headers)
    
    #print(response.text)
    return response    


def api_add_teams(token, team_title):
    
    url = "https://qa-sandbox.apps.htec.rs/api/roles/role"
    
    payload = "{\"role_name\":\"" + team_title + "\"}"
    headers = {
        'accept': "application/json, text/plain, */*",
        'authorization': "Bearer " + token,
        'content-type': "application/json;charset=utf-8",
        'content-length': str(16 + len(team_title)),
        'cache-control': "no-cache",
        'postman-token': "6315b652-7f29-4370-9179-75d3f91c2d18"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    #print(response.text)
    return response    


def api_delete_all_teams(token):
    
    all_teams = json.loads(api_get_all_teams(token).text)
    
    for i in range(0, len(all_teams)):
        
        team_id = all_teams[i]["role_id"]
        
        url = "https://qa-sandbox.apps.htec.rs/api/roles/role/" + str(team_id)
        
        headers = {
            'authorization': "Bearer " + token,
            'cache-control': "no-cache",
            'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
            }
        
        response = requests.request("DELETE", url, headers=headers)


def api_delete_teams(token, team_id):
    
    url = "https://qa-sandbox.apps.htec.rs/api/roles/role/" + str(team_id)
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
        }
    
    response = requests.request("DELETE", url, headers=headers)
    
    #print(response.text)
    return response


# =============================================================================
# PEOPLE - word "people" is pluralia tantum
# =============================================================================
def api_get_all_people(token):

    url = "https://qa-sandbox.apps.htec.rs/api/people/all"
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "42cda08a-89bd-f7b7-6eb1-f197be8d510f"
        }
    
    response = requests.request("GET", url, headers=headers)
    
    #print(response.text)
    return response    


def api_add_people(token, name, sen='', technologies=[], role=''):
    
    url = "https://qa-sandbox.apps.htec.rs/api/people/person"
    
    if sen=='' and role=='':
        payload = "{\"people_name\":\"" + name + "\",\"technologies\":" + str(technologies) + "}"
        req_len = len(name) + len(str(technologies)) + 39
        
    elif sen=='' and role!='':
        
        payload = "{\"people_name\":\"" + name + "\",\"technologies\":" + str(technologies) + ",\"role_id\":" + str(role) + "}" 
        req_len = len(name) + len(str(technologies)) + 53
    
    elif sen!='' and role=='':
        
        payload = "{\"people_name\":\"" + name + "\",\"seniority_id\":" + str(sen) + ",\"technologies\":" + str(technologies) + "}"      
        req_len = len(name) + len(str(technologies)) + 58
                
    else:
        
        payload = "{\"people_name\":\"" + str(name) + "\",\"seniority_id\":" + str(sen) + ",\"technologies\":" + str(technologies) + ",\"role_id\":" + str(role) + "}"
        req_len = len(name) + len(str(technologies)) + 73
                
    headers = {
        'accept': "application/json, text/plain, */*",
        'authorization': "Bearer " + token,
        'content-type': "application/json;charset=utf-8",
        'content-length': str(16 + req_len),
        'cache-control': "no-cache",
        'postman-token': "6315b652-7f29-4370-9179-75d3f91c2d18"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    #print(response.text)
    return response    


def api_delete_all_people(token):
    
    all_people = json.loads(api_get_all_people(token).text)
    
    for i in range(0, len(all_people)):
        
        people_id = all_people[i]["people_id"]
        
        url = "https://qa-sandbox.apps.htec.rs/api/people/person/" + str(people_id)
        
        headers = {
            'authorization': "Bearer " + token,
            'cache-control': "no-cache",
            'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
            }
        
        response = requests.request("DELETE", url, headers=headers)


def api_delete_peolpe(token, people_id):
    
    url = "https://qa-sandbox.apps.htec.rs/api/people/person/" + str(people_id)
    
    headers = {
        'authorization': "Bearer " + token,
        'cache-control': "no-cache",
        'postman-token': "b7c9ef89-2743-6c02-45b4-284752b69ecc"
        }
    
    response = requests.request("DELETE", url, headers=headers)
    
    #print(response.text)
    return response














# =============================================================================
# MAIN
# =============================================================================
token = json.loads(api_login('nikolacabi@yahoo.com', 'HTEC2021').text)["token"]

api_add_technologies(token, "tech5652")
all_tech = json.loads(api_get_all_technologies(token).text)
#api_delete_all_technologies(token)

api_add_seniorities(token, "tech5652")
all_sen = json.loads(api_get_all_seniorities(token).text)
#api_delete_all_seniorities(token)

api_add_teams(token, "Team43")
all_teams = json.loads(api_get_all_teams(token).text)
#api_delete_all_teams(token)