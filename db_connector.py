from datetime import datetime
import pymysql, requests, json


#init connection to DB
conn = pymysql.connect(host='db4free.net', port=3306, user='yaakovem', passwd='QAZWSXedc12!', db='yaakovem_db')
conn.autocommit(True)
cursor = conn.cursor()


def add_user(id,name):
    full_id=int(id)
    
    creation_time= str(datetime.now())
    #Inserting data into users table
    try:
        cursor.execute(f"INSERT into yaakovem_db.users (user_id, user_name,creation_date) VALUES ({full_id},'{name}','{creation_time}');")
        return True

    except:
        return False
    

def get_user(id):
    full_id=int(id)
    #get user name by id
    try:
        cursor.execute(f"SELECT user_name FROM yaakovem_db.users WHERE user_id = {full_id}")
        records = cursor.fetchall()
        for row in records:
            return row[0]
    except:
        print("return false")
        return False
  

def update_user(id,name):
    full_id=int(id)

    #updating data into users table
    try:
        sql=(f"UPDATE yaakovem_db.users SET user_name ='{name}' WHERE user_id = {full_id}")
        result= cursor.execute(sql)
        if result:
             return True
        else:
            return False

    except:
        return False
    

def delete_user(id):
    full_id=int(id)

    #DELETE data from users table
    try:
        print("before delete in sql")
        #delete user by user_id
        sql=(f"DELETE FROM yaakovem_db.users WHERE user_id = {full_id}")
        cursor.execute(sql)
        print("after delete")
        return True

    except:
        return False
  

