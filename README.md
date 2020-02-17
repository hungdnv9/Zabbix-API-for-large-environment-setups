# Zabbix-API-for-large-environment-setups

This is my personal project, and it's still in progressing. It's written by Python 2 with very common library, i use request and json to handle process and generate data
It's will help you save your time to manager and setup zabbix environment automation.

## Simple plan example

Groups					| Function
------------------------|-------------------------------
ABC_PRODUCTION_SERVERS	| List servers for production
ABC_STAGGING_SERVERS	| List servers for stagging
ABC_DEVELOP_SERVERS		| List servers for dev
ABC_SERVERS 			| List all server of ABC company

I will create 3 groups for individual environment include producion, stagging, dev and 1 group for monitoring all server as they have the same metric (like memory, hdd, cpu, ..)

## Setup your app config

```bash
$cat ./ZabbixAPI/app_setting.py
zb_api_url = 'http://zabbix.psaux.vn/api_jsonrpc.php'
zb_username = 'Admin'
zb_password = 'zabbix'
zb_session_id = 'efe6fd5f27f5e68d1585f132b2d52337'

# MYSQL CONFIG
zb_datbase_host = '127.0.0.1'
zb_database_port = 3306
zb_database_user = 'zabbix'
zb_database_passwd = 'zabbix@password'
zb_database_name = 'zabbix
```

```python
from ZabbixAPI import group

hostgroups=["ABC_PRODUCTION_SERVERS", "ABC_STAGGING_SERVERS", "ABC_DEVELOP_SERVERS", "ABC_SERVERS"]
group.create(hostgroups)
```


## Create templates

Template 								| Link Groups
----------------------------------------|-------------------------------------------------------------------- 
ABC_TEMPLATE_DISCOVER_SERVICES			|  ABC_PRODUCTION_SERVERS, ABC_STAGGING_SERVERS, ABC_DEVELOP_SERVERS
ABC_TEMPLATE_INFRATRUCTURE_MONITORING 	|  ABC_SERVERS

Next, i will create a template and link them to Host Group

```python
from ZabbixAPI import template

TEMPLATES = [
	{
		"NAME": "ABC_TEMPLATE_DISCOVER_SERVICES",
		"LINK_GROUPS": [
			"ABC_PRODUCTION_SERVERS", 
			"ABC_STAGGING_SERVERS", 
			"ABC_DEVELOP_SERVERS"
		]
	},
	{
		"NAME": "ABC_TEMPLATE_INFRATRUCTURE_MONITORING",
		"LINK_GROUPS": [
			"ABC_SERVERS"
		]
	}
]

template.create(TEMPLATES)
```

##  Item

Example json file

```json
{
    "name": "haproxy_status",
    "key_": "trapper.haproxy",
    "hostid": "ABC_TEMPLATE_INFRATRUCTURE_MONITORING",
    "type": 2,
    "status": 0,
    "value_type": 3,
    "applications": [
        "haproxy",
        "web"
    ],
    "units": "",
    "trapper_hosts": "",
    "delay": 30,
    "description": "Somethings related the item"
}
```

Item action support: create, getid, update and delete item

```python
from ZabbixAPI.item import Items

i = Items("./conf.d/items/item_haproxy_status.json")

# create item
#i.create()
#i.getid()
#i.update()
#i.delete()
```

## Trigger

Example json file

```json
{
	"description": "Service Haproxy are Down",
	"expression": {
		"host": "ABC_TEMPLATE_INFRATRUCTURE_MONITORING",
		"key": "trapper.haproxy",
		"function": "last()",
		"operator": "=",
		"constant": 3
	},
	"comments": "Check Haproxy status",
	"priority": 5,
	"status": 1,
	"type": 0,
	"url": "https://github.com/hungdnv",
	"recovery_mode": 0,
	"manual_close": 0,
	"tags": [
		{
			"tag": "service",
			"value": "haproxy"
		},
		{
			"tag": "system",
			"value": "yes"
		}

	]
}
```
Trigger acction support: Create, getid, update, delete

```python
from ZabbixAPI.trigger import Triggers

t = Triggers("./conf.d/triggers/trigger_haproxy_status.json")
#t.create()
#t.getid()
#t.update()
#t.delete()
```


Thanks for your attention. If you need more further, please contact me by email hungdnv9@gmail.com. Nice to meet you :)))