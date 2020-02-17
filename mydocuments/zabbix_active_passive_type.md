## ACTIVE MODE
AGENT ---> request list of check  --->  Zabbix Server 
AGENT <--- responses list to check (example: CPU, RAM, ...) <--- Zabbix Server
AGENT ---> send back list of value need to check ---> Zabbix Server

+ config:
	ServerActive=<zabbix_server_ip>
+ note: if use ACTIVE MODE, do not set any config on PASSIVE parameter


## PASSIVE MODE
 SERVER --> request value of cpu --> Agent
 SERVER  <-- respone value of cpu <-- Agent
 SERVER --> request value of memory --> Agent
SERVER  <-- respone value of memory <-- Agent

+ config:
	Server=<zabbix_server_ip>
	ListenPort=<zabbix_server_port>
	ListenIP=<zabbix_agent_ip>

	
