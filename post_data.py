import requests

# res = requests.post('http://127.0.0.1:5000/users/105', json={"user_name": "Moshe"})
# print(res.json())

# res = requests.put('http://127.0.0.1:5000/users/108',json={"user_name": "david11"})
# print(res.json())


# res = requests.delete('http://127.0.0.1:5000/users/109')
# print(res.json())

res = requests.get('http://127.0.0.1:5000/users/105')
print(res.json())
# res = requests.get('http://127.0.0.1:5001/get_user_name/105')
# print(res)

x="yaakov"
print("my name is"+x)