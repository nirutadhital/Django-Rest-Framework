import requests

headers={'Authorization':'Bearer9076659c2876ac765e0f066461a90ac8652d6a62'}

endpoint="http://localhost:8000/api/products/"

data={
    "title":"This field is done",
    "price":32.99
}

get_response=requests.post(endpoint, json=data, headers=headers)  

print(get_response.json())