# 
# Modul for working with Mysql DB
# 

# libs
import mysql.connector

class Mod_db:

    # contructor
    def __init__(self, host, user_name, password, db_name) -> None:
        
        #  create connection connection
        self.connection = mysql.connector.connect(host = host, user = user_name, passwd = password, database = db_name)

        # io buffer cursor
        self.cursor = self.connection.cursor()


    # Input (not read server ansver)
    def IO(self, sql_command, accept_changes = False):

        # send sql
        self.cursor.execute(sql_command)

        # accept changes
        if accept_changes:
            self.connection.commit()

        # return db answer
        return self.cursor.fetchall()