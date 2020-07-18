import requests
from raven.utils import json

url="http://127.0.0.1:8080/api/slot_booking/user/login/"
data = {"username": "123", "password": "abc"}
d = json.dumps(data)

response = requests.post(url=url, data=d, headers={"Content-type" : "application/json"})
print(response.content)