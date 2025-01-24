import requests

# endpoint="https://httpbin.org/status/200/"
# endpoint="https://httpbin.org/anything"
endpoint="http://localhost:8000/api/"

get_response=requests.post(endpoint, json={"title":"Abc123", "content":"Hello world!", "price":"abc123"})  #API 


print(get_response.json())

