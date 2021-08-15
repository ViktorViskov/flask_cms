# 
# Modul for working with Mysql DB
# 

# libs
import mysql.connector

class Mod_db:

    # contructor
    def __init__(self, host, user_name, password, db_name) -> None:
        self.host = host
        self.user_name = user_name
        self.password = password
        self.db_name = db_name
    
    # Function for open connection
    def Open(self):
        # open connection
        self.connection = mysql.connector.connect(host = self.host, user = self.user_name, passwd = self.password, database = self.db_name)

        # io buffer cursor
        self.cursor = self.connection.cursor()

    # Function for clouse connection
    def Close(self):
        # close connection
        self.connection.close()

    # Input (not read server ansver)
    def IO(self, sql_command, accept_changes = False):

        # send sql
        self.cursor.execute(sql_command)

        # accept changes
        if accept_changes:
            self.connection.commit()
        
        else:
            # return data
            return self.cursor.fetchall()