import requests
from raven.utils import json

# url="http://127.0.0.1:8080/api/slot_booking/user/login/"

# url="http://127.0.0.1:8080/api/slot_booking/add/new_washing_mechine/"

# url = "http://127.0.0.1:8080/api/slot_booking/get/all_washing_mechine_detalis"

# url = "http://127.0.0.1:8080/api/slot_booking/get/washing_machine_slot_details/1/MONDAY/"

# url = "http://127.0.0.1:8080/api/slot_booking/get/reported_issues/?offset=0&limit=9"

url = "http://127.0.0.1:8080/api/slot_booking/update/washing_machine_status/"

# url = "http://127.0.0.1:8080/api/slot_booking/update/issues/is_resolved/"

# data = {"username": "satya", "password": "sowrav"}
data = {"washing_machine_id": "2", "is_active": "False"}
# data = {"washing_mechine_id": "02", "washing_machine_image": "image.url"}

d = json.dumps(data)

# response = requests.post(url=url, data=d, headers={"Content-type": "application/json"})
# response = requests.post(url=url, data=d, headers={"Content-type": "application/json", "Authorization": "Bearer PTE0GOoBdvaFeCIiwpy7oBUdijki5h"})
# response = requests.get(url=url, headers={"Content-type": "application/json", "Authorization": "Bearer PTE0GOoBdvaFeCIiwpy7oBUdijki5h"})
response = requests.put(url=url, data=d, headers={"Content-type": "application/json", "Authorization": "Bearer PTE0GOoBdvaFeCIiwpy7oBUdijki5h"})

print(response.content)
