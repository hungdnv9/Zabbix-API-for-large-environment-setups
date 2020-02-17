import requests
import json
from app_setting import zb_session_id, zb_username, zb_password, zb_api_url




def exist(template_name):
    """
    Check Temple is existing or not
    If len of result is equal 0 -> Template is not created
    Return True if exist, False if is not exist
    """


    data = {
        "jsonrpc": "2.0",
        "method": "template.get",
        "params": {
            "output": "extend",
            "filter": {
                "host": template_name
            }
        },
        "auth": zb_session_id,
        "id": 1
    }
    response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})

    result = response.json()

    if len(result['result']) == 0:
        return False
    else:
        return True

def create(TEMPLATE_METRICS):

    params= []
    for template in TEMPLATES:
        link_groups = template['LINK_GROUPS']
        link_groups_id = group.getid(link_groups)
        template_name = template['NAME']
        #print template_name, link_groups_id
        groups = []
        for groupid in link_groups_id:
            groups.append(
                {
                    "groupid": int(groupid)
                }
            )
        params.append(
            {
                "host": template_name,
                "groups": groups
            }
        )

    for param in params:
        data = {
            "jsonrpc": "2.0",
            "method": "template.create",
            "params": param,
            "auth": zb_session_id,
            "id": 1
        }
    
        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})        
        print response.json()
    
def getid(TEMPLATES):
    """
    :TEMPLATES type List
    :return list templateIDs
    """

    data = {
        "jsonrpc": "2.0",
        "method": "template.get",
        "params": {
            "output": "extend",
            "filter": {
                "host": TEMPLATES
            }
        },
        "auth": zb_session_id,
        "id": 1
    }

    response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})        
    
    result = response.json()
    
    template_ids = []
    for template in  result['result']:
        template_ids.append(template['templateid'])

    return template_ids    





