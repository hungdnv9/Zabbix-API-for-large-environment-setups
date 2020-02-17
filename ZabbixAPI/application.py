import requests
import json
from app_setting import zb_session_id, zb_api_url
from database import MysqlDB

def exist(name, hostid):

    SQL = "SELECT applicationid  FROM  applications WHERE name LIKE '%{name}%' AND hostid={hostid}".format(name=name, hostid=hostid)
    result = MysqlDB().execute(SQL)
    if len(result) == 0:
        return False
    else: 
        return True

def create(applications, hostid):
    """
    :applications Type List 
    """
    for application in applications:
        data = {
            "jsonrpc": "2.0",
            "method": "application.create",
            "params": {
                "name": application,
                "hostid": hostid
            },
            "auth": zb_session_id,
            "id": 1
        }

        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})
        print response.json()

def getid(applications, hostid):
    """
    :applications Type List
    :return list application_ids
    """
    result = []
    for application in applications:
        SQL = "SELECT applicationid  FROM  applications WHERE name LIKE '%{name}%' AND hostid={hostid}".format(name=application, hostid=hostid)    
        """
        [(466,)]
        ->
        [466]    
        """
        result.append(MysqlDB().execute(SQL)[0][0]) 

    return result
    


