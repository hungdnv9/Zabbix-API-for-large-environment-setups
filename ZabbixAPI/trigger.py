import requests
import json
from app_setting import zb_session_id, zb_api_url
from validate import Validate
from database import MysqlDB
import template

class Triggers:

    def __init__(self, trigger_json_file):

        self.trigger_json_file = trigger_json_file
        
        with open(trigger_json_file) as f:
            params = json.load(f)
            self.template_name = params["expression"]["host"]
            self.trigger_description = params["description"]

        self.templateid = template.getid(self.template_name)[0]        
        self.trigger_params = Validate().trigger(self.trigger_json_file)


    def getid(self):


        sql = "SELECT t.triggerid  FROM triggers t,items i,functions f WHERE i.itemid=f.itemid \
               AND f.triggerid=t.triggerid \
               AND i.hostid={templateid} \
               AND t.templateid IS NULL \
               AND t.description='{trigger_description}'".format(templateid=self.templateid, trigger_description=self.trigger_description)

        result = MysqlDB().execute(sql)[0][0]
        print result
        return result

    def create(self):

        data = {
            "jsonrpc": "2.0",
            "method": "trigger.create",
            "params": self.trigger_params,
            "auth": zb_session_id,
            "id": 1
        }

        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})            
        result = response.json()    

        print result

    def update(self):
        self.trigger_params[0].update({"triggerid": self.getid()})
        
        data = {
            "jsonrpc": "2.0",
            "method": "trigger.update",
            "params": self.trigger_params,
            "auth": zb_session_id,
            "id": 1
        }
        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})            
        result = response.json()    

        print result

    def delete(self):
        
        data = {
            "jsonrpc": "2.0",
            "method": "trigger.delete",
            "params": [
                self.getid()
            ],
            "auth": zb_session_id,
            "id": 1
        }

        response = requests.post(zb_api_url, data=json.dumps(data), headers={'content-type': 'application/json'})            
        result = response.json()    

        print result 