import requests
from raven.utils import json

# url="http://127.0.0.1:8080/api/slot_booking/user/login/"
# url="http://127.0.0.1:8080/api/slot_booking/add/new_washing_mechine/"
url = "http://127.0.0.1:8080/api/slot_booking/get/all_washing_mechine_detalis"

# data = {"username": "susmitha", "password": "satya"}
# data = {"washing_mechine_id": "2"}
# d = json.dumps(data)

# response = requests.post(url=url, data=d, headers={"Content-type" : "application/json"})
# response = requests.post(url=url, data=d, headers={"Content-type": "application/json", "Authorization": "Bearer vLPaLT92giigs7A7jIleTKMYLAfSqP"})
response = requests.get(url=url, headers={"Content-type": "application/json", "Authorization": "Bearer vLPaLT92giigs7A7jIleTKMYLAfSqP"})

print(response.content)