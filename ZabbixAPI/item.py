import requests
import json
from app_setting import zb_session_id, zb_username, zb_password, zb_api_url
import application
import template
from validate import Validate
from database import MysqlDB

class Items:

    def __init__(self, item_json_file):
        
        self.item_json_file = item_json_file
        self.item_params = Validate().item(self.item_json_file)

        self.item_name = self.item_params['name']
        self.templateid = self.item_params['hostid']
           

    def getid(self):
        sql = "SELECT itemid FROM items WHERE name='{item_name}' AND templateid IS NULL AND hostid='{hostid}'".format(item_name=self.item_name, hostid=self.templateid);
        result = MysqlDB().execute(sql)[0][0]
        print result
        return result

    def create(self): 
        
       
        data = {
            "jsonrpc": "2.0",
            "method": "item.create",
            "params": self.item_params,
            "auth": zb_session_id,
            "id": 1
        }

        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})            
        result = response.json()    

        print result

    def update(self):

        itemid = self.getid()

        self.item_params.update({"itemid": itemid})

        data = {
            "jsonrpc": "2.0",
            "method": "item.update",
            "params": self.item_params,
            "auth": zb_session_id,
            "id": 1
        }

        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})            
        result = response.json()    

        print result


    def delete(self):
        itemid = self.getid()
        data = {
            "jsonrpc": "2.0",
            "method": "item.delete",
            "params": [
                itemid
            ],
            "auth": zb_session_id,
            "id": 1
        }

        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})            
        result = response.json()    

        print result