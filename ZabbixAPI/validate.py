import json
import requests
import template
import application

class Validate:

    def __init__(self):
        pass

    def trigger(self, trigger_json_file):
        
        # DEFAULT TRIGGER OBJECT
        description = ""
        expression = ""
        comments = ""
        priority = 0
        status = 0
        _type = 0
        url = "https://github.com/hungdnv9"
        recovery_mode = 0
        recovery_expression = ""
        manual_close = 0
        tags = ""

        # GET TRIGGER OBJECTS
        with open(trigger_json_file) as f:
            params = json.load(f)
            trigger_objects =  params.keys()

            for obj in trigger_objects:
                if "description" == obj:
                    description = params["description"]

                if "expression" == obj:
                    expression = params["expression"]

                if "comments" == obj:
                    comments = params["comments"]

                if "priority" == obj:
                    priority = params["priority"]

                if "status" == obj:
                    status = params["status"]

                if "type" == obj:
                    _type = params["type"]
        
                if "url" == obj:
                    url = params["url"]

                if "recovery_mode" == obj:
                    recovery_mode = params["recovery_mode"]

                if "recovery_expression" == obj:
                    recovery_expression = params["recovery_expression"]

                if "manual_close" == obj:
                    manual_close = params["manual_close"]

                if "tags" == obj:
                    tags = params["tags"]


        # FORMAT TRIGGER EXPRESSION         
        expression_str = "{{{server}:{key}.{function}}}{operator}{constant}".format(
            server=expression["host"],
            key=expression["key"],
            function=expression["function"],
            operator=expression["operator"],
            constant=expression["constant"]
        )

        # FORMAT TRIGGER RECOVERY EXPRESSION
        if recovery_expression != "":
            recovery_expression_str = "{{{server}:{key}.{function}}}{operator}{constant}".format(
                server=recovery_expression["host"],
                key=recovery_expression["key"],
                function=recovery_expression["function"],
                operator=recovery_expression["operator"],
                constant=recovery_expression["constant"]
            )
        else:
              recovery_expression_str =  recovery_expression

        # FORMAT TRIGGER PARAMS
        trigger_params_construct = [
            {
                "description": description,
                "expression": expression_str,
                "comments": comments,
                "priority": priority,
                "status": status,
                "type": _type,
                "url": url,
                "recovery_mode": recovery_mode,
                "recovery_expression": recovery_expression_str,
                "manual_close": manual_close,
                "tags": tags
            }
        ]

        result = eval(json.dumps(trigger_params_construct))
        return result
                
#v = Validate()
#v.trigger("/home/hungdnv/ANTS/zabbix-server/conf.d/triggers/service_nginx.json")   

    def item(self, item_json_file):
        # DEFAULT ITEM OBJECTS      
        """
        :str item_name: Name of the item
        :str item_key: Key of the item
        :str hostid: Name of host / template
        :int item_type: Type of information of the item. Type of the item.
            Possible values:
            0 - Zabbix agent;
            1 - SNMPv1 agent;
            2 - Zabbix trapper;
            3 - simple check;
            4 - SNMPv2 agent;
            5 - Zabbix internal;
            6 - SNMPv3 agent;
            7 - Zabbix agent (active);
            8 - Zabbix aggregate;
            9 - web item;
            10 - external check;
            11 - database monitor;
            12 - IPMI agent;
            13 - SSH agent;
            14 - TELNET agent;
            15 - calculated;
            16 - JMX agent;
            17 - SNMP trap. 
    
        :int status: Status of Item. Value
            0 - Enable
            1 - Disable 

        :int value_type: Type of information of the item. 
            Possible values:
            0 - (default) decimal;
            1 - octal;
            2 - hexadecimal;
            3 - boolean. 


        :list applications: Name of the application
        :str unit: Value units
        :str trapper_hosts: Allowed hosts. Used only by trapper items. 
        :int delay: Update interval of the item in seconds (required).
        :str description: Description of the item
        :str history: A time unit of how long the history data should be stored. Also accepts user macro.
        :str trends: A time unit of how long the trends data should be stored. Also accepts user macro.
        """

        item_name = "" 
        item_key = ""   
        template_name = "" 
        item_type = ""
        status = 0
        value_type = 3
        applications = []
        units = ""
        trapper_hosts = ""
        delay = 30
        description = ""
        history = 90
        trends = 365

        # GET ITEM OBJECTS
        with open(item_json_file) as f:
            params = json.load(f)
            item_objects = params.keys()

            for obj in item_objects:
                if "name" == obj:
                    item_name = params["name"]

                if "key_" == obj:
                    item_key = params["key_"]

                if "hostid" == obj:
                    template_name = params["hostid"]

                if "type" == obj:
                    item_type = params["type"]

                if "status" == obj:
                    status = params["status"]

                if "value_type" == obj:
                    value_type = params["value_type"]

                if "applications" == obj:
                    applications = params["applications"]

                if "units" == obj:
                    units = params["units"]

                if "trapper_hosts" == obj:
                    trapper_hosts = params["trapper_hosts"]

                if "delay" == obj:
                    delay = params["delay"]

                if "description" == obj:
                    description = params["description"]

                if "history" == obj:
                    history = params["history"]

                if "trends" == obj:
                    trends =params["trends"]

        # GET TEMPLATE ID
        templateid = template.getid(template_name)[0]


        # CHECK APPLICATION IS EXIST
        for name in applications:
            if application.exist(name, templateid) is True:
                print "application name: ", name, "is existing, skip create application"
            else:
                # CREATE APPLICATION
                application.create(applications, templateid)

        # GET APPLICATION ID
        applicationsids = application.getid(applications, templateid)
        
        # FORMAT TRIGGER CONSTRUCT
        item_params_construct = {
            "name": item_name,
            "key_": item_key,
            "hostid": templateid,
            "type": item_type,
            "status": status,
            "value_type": value_type,
            "applications": applicationsids,
            "units": units,
            "trapper_hosts": trapper_hosts,
            "delay": delay,
            "description": description,
            "history": history,
            "trends": trends
        }


        result = eval(json.dumps(item_params_construct))
        return result

