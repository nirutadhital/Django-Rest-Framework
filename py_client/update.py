import requests

endpoint="http://localhost:8000/api/products/10/update/"

data={
    "title":"Hello world my old friends! How are you",
    "price":1200.99
}

get_response=requests.put(endpoint, json=data)  #API 


print(get_response.json())
