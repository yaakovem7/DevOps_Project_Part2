import requests
from db_connector import *

user_id="109"
user_name="Yaakov"

post_test = requests.post('http://127.0.0.1:5000/users/'+user_id, json={"user_name": user_name})
print (post_test.json())

res = requests.get('http://127.0.0.1:5000/users/'+user_id)
if res.ok and (res.json()['user_name'] == user_name):
    print("return code is 200 and user name"+ user_name+ " as expected")

if (get_user(user_id) == user_name):
    print(user_name+" is stored in users db with user id"+user_id)



