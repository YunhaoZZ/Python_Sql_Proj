import mysql.connector as connector

class DBManager:
    def __init__(self):
        self.connector = connector.connect(host='localhost',
                                     port='3308',
                                     user='root',
                                     password='20000819',
                                     database='pythonproj')

        sql_query = 'create table if not exists user(uID int primary key, userName varchar(200), phone varchar(12))'
        cursor = self.connector.cursor()
        cursor.execute(sql_query)
        print("Table 'user' Created")

    # Insert
    def insert_user(self, uId_in, userName_in, phone_in):
        sql_query = "insert into user(uID, userName, phone) \
            values({}, '{}', '{}')".format(uId_in, userName_in, phone_in)
        print("---Query-----------")
        print(sql_query)
        print("---Result----------")
        cur = self.connector.cursor()
        cur.execute(sql_query)
        self.connector.commit()
        print("new user data recorded")

    # Select
    def select_all(self):
        sql_query = "select * from user"
        cur = self.connector.cursor()
        cur.execute(sql_query)
        for record in cur:
            print("Name: ", record[1])
            print("ID: ", record[0])
            print("Phone: ", record[2])
            print("----------")
            print("----------")

    # Delete
    def delete_by_id(self, uID_dl):
        sql_query = "delete from user where uID = {}".format(uID_dl)
        print("---Query-----------")
        print(sql_query)
        print("---Result----------")
        cur = self.connector.cursor()
        cur.execute(sql_query)
        self.connector.commit()       # commit the change or the change is not permanent
        print("User deleted")

    # Update record
    def update_by_id(self, uID_up, userName_new, phone_new):
        sql_query = "update user set userName='{}', phone='{}' where uID={}".format(
            userName_new, phone_new, uID_up)
        print("---Query-----------")
        print(sql_query)
        print("---Result----------")
        cur = self.connector.cursor()
        cur.execute(sql_query)
        self.connector.commit()
        print("Record updated")
