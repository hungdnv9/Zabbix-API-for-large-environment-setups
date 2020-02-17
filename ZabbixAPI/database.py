import mysql.connector
from mysql.connector import errorcode
from app_setting import zb_datbase_host, zb_database_port, zb_database_name, zb_database_user, zb_database_passwd


class MysqlDB():

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                    host=zb_datbase_host, 
                    port=zb_database_port, 
                    user=zb_database_user,
                    passwd=zb_database_passwd,
                    database=zb_database_name
                )

            self.cursor = self.cnx.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def execute(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.cnx.close()
        return result

        