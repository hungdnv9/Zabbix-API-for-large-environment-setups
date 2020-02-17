# Colect data by using Zabbix Server script
# Defind external script dir in zabbix-server conf file
ExternalScripts=/opt/zabbix-server-3.2.11/externalscripts

# Create somescript.sh in ExternalScripts dir
cat << EOF > /opt/zabbix-server-3.2.11/externalscripts/cpu_cores.sh
nproc
EOF

chmod +x /opt/zabbix-server-3.2.11/externalscripts/cpu_cores.sh

# Create item on Zabbix GUI, type external 
key: cpu_cores.sh

# Compine with variable in script
#! /bin/bash
echo $1

key: somescript.sh["ip"]

# Use macros
key: myscript.sh["{HOST.IP}","var1"]


