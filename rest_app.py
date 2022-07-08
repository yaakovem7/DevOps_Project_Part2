from datetime import datetime
import requests
from flask import Flask, request
from db_connector import *

# varaialbe  declaratives
app = Flask(__name__)


# supported API methods for BE
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users(user_id):
    if request.method == 'POST':
        # getting the json data payload from request /users/<user_id>/{"user_name":"john"}
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')  # john
        # Inserting data into users table
        db_result=add_user(user_id,user_name)
        if db_result == True:
            return {"status": "ok", "user_added": user_name}, 200
        else:
            return {"status": "error", "reason": "id already exists"}, 500
        

    elif request.method == 'GET':
        user_name = get_user(user_id)

        if (user_name != None): #meaning not null
            return {"status": "ok", "user_name": user_name}, 200
        else:
            return {"status": "error", "reason": "no such id"}, 500

    elif request.method == 'PUT':
        # getting the json data payload from request /users/<user_id>/{"user_name":"john"}
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')  # john
        # Inserting data into users table
        db_result= update_user(user_id,user_name)
        print(db_result)
        if db_result == True:
            return {"status": "ok", "user updated": user_name}, 200
        else:
            return {"status": "error", "reason": "no such id"}, 500

    elif request.method == 'DELETE':
        try:

            # deleting data from users table
            print("before deleter_user()")
            if delete_user(user_id) == True:
                return {"status": "ok", "user deleted": user_id}, 200
            else:
                return {"status": "error", "reason": "no such id"}, 500
            #
        except:
            return {"status": "error", "reason": "no such id"}, 500

app.run(host='127.0.0.1', debug=True, port=5000)
