#very simple response getter
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

retry = Retry(total=3)
adapter = HTTPAdapter(max_retries=retry)
page = requests.Session()

URL = "https://cars.com"
page.mount("https://", adapter)
response = page.get(URL)
'''
line 6-8,11-12: will try three times to get the right response in case of three errors:

1. waiting for server to start answering for five seconds
2. there is no access to the server or there it dropped connection
3. 5XX responses by default

'''
print(response)

#authentication
from requests.auth import HTTPBasicAuth

log_in = HTTPBasicAuth('user', 'pass') #the username and password, trying to validate authentication
page = requests.get('https://httpbin.org/basic-auth/user/pass', auth=log_in)
print(page) #prints a 200 response code this time

page = requests.get('https://httpbin.org/basic-auth/user/pass') #trying to get a response with no authentication
page.raise_for_status() #raises a 401 unauthorized error