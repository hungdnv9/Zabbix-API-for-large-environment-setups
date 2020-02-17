# PROBLEM
MySQL [zabbix]> SELECT * FROM triggers  WHERE templateid IS NULL and description='Service Nginx Down';
+-----------+------------+--------------------+----------------------------+--------+-------+----------+------------+--------------------+-------+------------+------+-------+-------+---------------+---------------------+------------------+-----------------+--------------+
| triggerid | expression | description        | url                        | status | value | priority | lastchange | comments           | error | templateid | type | state | flags | recovery_mode | recovery_expression | correlation_mode | correlation_tag | manual_close |
+-----------+------------+--------------------+----------------------------+--------+-------+----------+------------+--------------------+-------+------------+------+-------+-------+---------------+---------------------+------------------+-----------------+--------------+
|     13573 | {13235}>5  | Service Nginx Down |                            |      0 |     0 |        5 |          0 |                    |       |       NULL |    0 |     0 |     0 |             0 |                     |                0 |                 |            0 |
|     13578 | {13249}=1  | Service Nginx Down | https://github.com/hungdnv |      0 |     0 |        5 |          0 | Check Nginx status |       |       NULL |    0 |     0 |     0 |             0 |                     |                0 |                 |            0 |
+-----------+------------+--------------------+----------------------------+--------+-------+----------+------------+--------------------+-------+------------+------+-------+-------+---------------+---------------------+------------------+-----------------+--------------+


--> we get 2 trigger as same name, but they come from different template. 
--> i did search google, and found it, https://www.zabbix.com/forum/zabbix-help/12434-link-between-triggers-table-and-hosts-table


# finaly result

SELECT t.triggerid 
FROM triggers t,items i,functions f 
WHERE i.itemid=f.itemid 
    AND f.triggerid=t.triggerid 
    AND i.hostid=10114 
    AND t.templateid IS NULL 
    AND t.description='Service Nginx Down';


    
select t.triggerid from triggers t,items i,functions f where i.itemid=f.itemid and f.triggerid=t.triggerid and i.hostid=10113 and t.templateid IS NULL and t.description='Service Nginx Down';


