import requests
import json
from setting import ZABBIX_URL_API, ZABBIX_PASSWORD, ZABBIX_USERNAME


def login():

    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": ZABBIX_USERNAME,
            "password": ZABBIX_PASSWORD
        },
        "id": 1,
        "auth": None
    }
    response = requests.post(ZABBIX_URL_API, data=json.dumps(data), headers={'content-type': 'application/json'})
    respone_json_format = response.json()

    session_id = respone_json_format['result']
    

def logout(self):

    data = {
        "jsonrpc": "2.0",
        "method": "user.logout",
        "params": [],
        "id": 1,
        "auth": session_id
    }    

    response = requests.post(self.URL, data=json.dumps(data), headers={'content-type': 'application/json'})
    respone_json_format = response.json()

    return respone_json_format
