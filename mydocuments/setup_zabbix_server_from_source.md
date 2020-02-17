# Download source
https://nchc.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/3.2.11/zabbix-3.2.11.tar.gz
# Compile
./configure \
--prefix=/opt/zabbix-server-3.2.11 \
--enable-server \
--enable-agent \
--with-mysql=/opt/mysql-5.7/bin/mysql_config \
--with-net-snmp \
--with-ssh2 \
--with-openssl \
--with-ldap \
--with-libcurl \
CPPFLAGS="-I/opt/mysql-5.7/include" \
LDFLAGS="-L/opt/mysql-5.7/lib"


make 
make install

# Create database
create database zabbix character set utf8 collate utf8_bin;
grant all privileges on zabbix.* to zabbix@10.127.0.3 identified by 'zabbix@password';
quit;


# Import DB source
/opt/mysql-5.7/bin/mysql -h 10.127.0.3 --socket=/opt/mysql-5.7/mysql.sock -u zabbix -pzabbix@password zabbix < /root/download/zabbix-3.2.11/database/mysql/schema.sql
/opt/mysql-5.7/bin/mysql -h 10.127.0.3 --socket=/opt/mysql-5.7/mysql.sock -u zabbix -pzabbix@password zabbix < /root/download/zabbix-3.2.11/database/mysql/images.sql
/opt/mysql-5.7/bin/mysql -h 10.127.0.3 --socket=/opt/mysql-5.7/mysql.sock -u zabbix -pzabbix@password zabbix < /root/download/zabbix-3.2.11/database/mysql/data.sql


## systemd file /etc/systemd/system/zabbix-server-3.2.11.service
[Unit]
Description=Zabbix Server version 3.2.11 LTS
After=syslog.target network.target mysqld.service

[Service]
Type=oneshot
ExecStart=/opt/zabbix-server-3.2.11/sbin/zabbix_server -c /opt/zabbix-server-3.2.11/etc/zabbix_server.conf
ExecReload=/opt/zabbix-server-3.2.11/sbin/zabbix_server -R config_cache_reload
RemainAfterExit=yes
PIDFile=/opt/zabbix-server-3.2.11/zabbix_server.pid

[Install]
WantedBy=multi-user.target

## fix zabix lib mysql

cat <<EOF > /etc/ld.so.conf.d/mysql-5.7.conf
/opt/mysql-5.7/lib
EOF

## Create zabbix user
## Change owner of zabbix dir

## Config frontend php + nginx

server {
    client_max_body_size 50m;
    client_header_timeout  5m;
    client_body_timeout    5m;
    send_timeout       5m;
    listen 10.127.0.3:8080;
    keepalive_timeout 5s;
    server_name zabbix.psaux.vn;

    
    access_log /data/logs/www/zabbix.psaux.vn_access.log;
    error_log /data//logs/www/zabbix.psaux.vn_error.log;

    index index.php;
    #auth_basic "Private Property";
    #auth_basic_user_file /data/www/zabbix.psaux.vn/.htpasswd;

    root /data/www/zabbix.psaux.vn;

    location / {
        try_files $uri $uri/ /index.php?$args;
        proxy_set_header Connection "";
        add_header Cache-Control no-cache;
    }

    location ~ \.php$ {
        try_files $uri =404;        
        fastcgi_split_path_info ^(.+\.php)(/.+)$;    
        fastcgi_intercept_errors on;
        fastcgi_read_timeout 60s;
        fastcgi_pass unix:/dev/shm/php-fpm-7.2.socket;
        fastcgi_index index.php;
        fastcgi_param APPLICATION_ENV production;
        fastcgi_param SCRIPT_FILENAME  /data/www/zabbix.psaux.vn$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\. {
        deny  all;
    }

}


## Config harproxy
backend backend_8080
    fullconn 100000
    balance roundrobin
    option redispatch
    option abortonclose
    #option httpclose
    option forwardfor
    compression algo gzip
    compression type text/cmd text/css text/csv text/html text/javascript text/plain text/vcard text/xml application/json application/x-www-form-urlencoded application/javascript application/x-javascript
    server localhost 10.127.0.3:8080 weight 5

    acl acl_backend_8080 hdr_beg(host) zabbix.psaux.vn
    use_backend backend_8080 if acl_backend_8080




