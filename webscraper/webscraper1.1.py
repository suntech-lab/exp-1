#very simple response getter
import requests

URL = "https://google.com"
page = requests.get(URL)

print(page)

#authentication
from requests.auth import HTTPBasicAuth

page = requests.get('https://httpbin.org/basic-auth/user/pass') #trying to get a response with no authentication
print(page) #this will print the 401 response code instead of the 200 response code because it lacks valid authentication

log_in = HTTPBasicAuth('user', 'pass') #the username and password, trying to validate authentication
page = requests.get('https://httpbin.org/basic-auth/user/pass', auth=log_in)
print(page) #prints a 200 response code this time