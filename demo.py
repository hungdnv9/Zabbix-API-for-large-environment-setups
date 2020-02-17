from ZabbixAPI import template, group, application
from ZabbixAPI.trigger import Triggers
from ZabbixAPI.item import Items

## CREATE GROUPS
hostgroups_file = "/home/hungdnv/ANTS/zabbix-server/conf.d/hostgroups/create.txt"
hostgroups=["ABC_PRODUCTION_SERVERS", "ABC_STAGGING_SERVERS", "ABC_DEVELOP_SERVERS", "ABC_SERVERS"]
#group.create(hostgroups)
#group.getid(hostgroups)

## CREATE TEMPLATE AND LINK TO GROUP

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

# GET TEMPLATE ID
#TEMPLATES=["ABC_TEMPLATE_DISCOVER_SERVICES", "ABC_TEMPLATE_INFRATRUCTURE_MONITORING"]
#print template.getid(TEMPLATES)
#


## ITEMS

i = Items("/home/hungdnv/ANTS/zabbix-server/conf.d/items/item_haproxy_status.json")

# create item
#i.create()
#i.getid()
#i.update()
#i.delete()


## TRIGER
t = Triggers("/home/hungdnv/ANTS/zabbix-server/conf.d/triggers/trigger_haproxy_status.json")
#t.create()
#t.getid()
#t.update()
#t.delete()