from flask import Flask, request
from db_connector import *
import os
import signal

# varaialbe  declaratives

app = Flask(__name__)


# supported API methods for FE
@app.route('/get_user_name/<user_id>', methods=['GET'])
def get_user_name(user_id):
    if request.method == 'GET':
        user_name = get_user(user_id)
        print("user_name")
        if user_name == None:
            print("<H1 id='error'>no such user: " + user_id + "</H1>")
            #return "<H1 id='error'>no such user: " + user_id + "</H1>", 200
            return "<H1 id='error'>no such user</H1>", 200
        else:
            #print("<H1 id='user'>" + user_name + "</H1>")
            return "<H1 id="+user_id+">" + user_name + "</H1>", 200
            #return "<H1 id=" + user_id + ">Works</H1>", 200


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5001)