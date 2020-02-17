import requests
import json
from app_setting import zb_session_id, zb_username, zb_password, zb_api_url




def create(HOST_GROUPS):
    for host_group in HOST_GROUPS:
        data = {
            "jsonrpc": "2.0",
            "method": "hostgroup.create",
            "params": {
                "name": host_group
            },
            "auth": zb_session_id,
            "id": 1
        }
        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})        
        print response.json()

def getid(HOST_GROUPS):
    groupids = []
    data = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": "extend",
            "filter": {
                "name": HOST_GROUPS
            }
        },
        "auth": zb_session_id,
        "id": 1
    }
    response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})        
    result = response.json()
    for group in  result['result']:
        groupids.append(group['groupid'])
    
    print groupids

    return groupids

def delete(HOST_GROUPS):
    groupids = getid(HOST_GROUPS)

    data = {
        "jsonrpc": "2.0",
        "method": "hostgroup.delete",
        "params": groupids,
        "auth": zb_session_id,
        "id": 1
    }    

    response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})        
    print response.json()
