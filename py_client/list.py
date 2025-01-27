import requests

endpoint="http://localhost:8000/api/products/"


get_response=requests.get(endpoint)  #API f


print(get_response.json())