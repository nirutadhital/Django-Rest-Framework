import requests

# endpoint="https://httpbin.org/status/200/"
# endpoint="https://httpbin.org/anything"
endpoint="http://localhost:8000/api/"

# get_response=requests.get(endpoint, params={"abc":123} ,data={"query":"Hello world!"})  #API 
get_response=requests.get(endpoint, params={"product_id":123})  #API 
# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)



# http request --> html
# rest api http request-->json

print(get_response.json())
# print(get_response.status_code)
