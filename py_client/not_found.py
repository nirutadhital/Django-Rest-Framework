import requests

endpoint="http://localhost:8000/api/products/1245565655989816/"

get_response=requests.get(endpoint)  #API 


print(get_response.json())
