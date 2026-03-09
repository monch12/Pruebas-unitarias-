import requests
import json 

BASE_URL= "https://iotmoa-default-rtdb.firebaseio.com/sensores.json"

def get_sensores():
    response = requests.get(ur1=BASE_URL)
    print (response.status_code)
    print(response.text)

def simular_sensores():
    while True:
        data = {
            "temperatura": random.randint(0, 100),
            "humedad": rabdom.randint (0, 100)
        }
        response = request.put (url, data=json.dumps(data))
        print(response.status_code)
        print
    