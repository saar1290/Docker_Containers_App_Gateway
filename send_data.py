import json
import os
import socket
import requests

def send_data():
    # Getting the local ip Address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com", 80))
    PX4_SIM_HOST_ADDR = s.getsockname()[0]
    instance_num = "0"
    
    # Create a dict and load data in
    data = {}
    for var in ('instance_num', 'PX4_SIM_HOST_ADDR'):
        data[var] = locals()[ var]
    data = json.dumps(data, indent=4)
    
    # Send the data to api
    # print(data)
    url = "http://127.0.0.1:8000/start"
    req =requests.post(url, json=json.loads(data), headers={"Content-Type": "application/json; charset=utf-8"},)
    res = requests.get(url, json=json.dumps(data))
    print(req.text)
    

# send_data()
# user = os.getenv('username')
# print(user)
PX4_SIM_HOST_ADDR = str("10.0.0.180")
ip = PX4_SIM_HOST_ADDR.split('.')[-1]
print(ip)