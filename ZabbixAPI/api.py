import requests
import json

class ZabbixAPI:

    def __init__(self):
        self.headers = {
            'content-type': 'application/json',
        }

        self.session_id = ''
        self.url = ''

    def loggin(self, url, zabbix_username, zabbix_passowrd):
        self.url = url
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": zabbix_username,
                "password": zabbix_passowrd
            },
            "id": 1,
            "auth": None
        }
        response = requests.post(self.url, data=json.dumps(data), headers=self.headers)
        response.encoding = "utf-8"
        """
        Output JSON format example
        {u'jsonrpc': u'2.0', u'result': u'b8a72b310f612b728dfe3ee157856e63', u'id': 1}
        """
        self.session_id = response.json()['result']
        

        print self.session_id

    def logout(self):

        data = {
            "jsonrpc": "2.0",
            "method": "user.logout",
            "params": [],
            "id": 1,
            "auth": self.session_id
        }
        response = requests.post(self.url, data=json.dumps(data), headers=self.headers)
        response.encoding = "utf-8"
        print response.json()


    def create_template(self, template_name, group_id):

        data = {
            "jsonrpc": "2.0",
            "method": "template.create",
            "params": {
                "host": template_name,
                "groups": {
                    "groupid": int(group_id)
                }
            },
            "auth": self.session_id,
            "id": 1
        }
        response = requests.post(self.url, data=json.dumps(data), headers=self.headers)
        response.encoding = "utf-8"
        print response.json()

z = ZabbixAPI()
z.loggin('http://zabbix.psaux.vn/api_jsonrpc.php', 'Admin', 'zabbix')
#z.create_template("Template Zabbix API", 1)
#z.logout()

