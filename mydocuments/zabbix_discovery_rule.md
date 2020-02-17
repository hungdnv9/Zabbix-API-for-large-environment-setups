# 
./bin/zabbix_get -s 10.127.0.3 -k vfs.fs.discovery
./bin/zabbix_get -s 10.127.0.3 -k net.if.discovery
./bin/zabbix_get -s 10.127.0.3 -k linux.services.discovery

https://www.zabbix.com/documentation/3.2/manual/discovery/low_level_discovery (section 10.3.8 )

## Custom discovery owner service
services.csv
------------
service_name,service_ip,service_port
haproxy,10.127.0.3,80
nginx,10.127.0.3,8080
mysql,10.127.0.3,3306

## Custom Json Output
#! /bin/python
import csv
import json

services_file = './services.csv'

output_json_format = {
	"data": [
	]
}

with open(services_file) as f:
	csv_reader = csv.DictReader(f)
	for column in csv_reader:
		output_json_format['data'].append(
			{
				"{#SERVICE_NAME}":column["service_name"],
				"{#SERVICE_IP}":column["service_ip"],
				"{#SERVICE_PORT}":column["service_port"]
			},
		)
output = json.dumps(output_json_format, indent=4, sort_keys=True)
print output


## output 

./discover_services.py 
{
    "data": [
        {
            "{#SERVICE_IP}": "10.127.0.3", 
            "{#SERVICE_NAME}": "haproxy", 
            "{#SERVICE_PORT}": "80"
        }, 
        {
            "{#SERVICE_IP}": "10.127.0.3", 
            "{#SERVICE_NAME}": "nginx", 
            "{#SERVICE_PORT}": "8080"
        }, 
        {
            "{#SERVICE_IP}": "10.127.0.3", 
            "{#SERVICE_NAME}": "mysql", 
            "{#SERVICE_PORT}": "3306"
        }
    ]
}

# Add UserParameter to Zabbix_Agent conf file
UserParameter=linux.services.discovery, /opt/zabbix-server-3.2.11/discovery_services/discover_services.py

# Create item
name: Service {#SERVICE_NAME} bind on port {#SERVICE_PORT}
key: net.tcp.port[{#SERVICE_IP},{#SERVICE_PORT}]

# Create trigger
Last value:
1 -> Reach
0 -> Unreach

{Template Discovery Service:net.tcp.port[{#SERVICE_IP},{#SERVICE_PORT}].last(,3)}=0
-> Last 3 times, if can't reach wiht port -> trigger start








