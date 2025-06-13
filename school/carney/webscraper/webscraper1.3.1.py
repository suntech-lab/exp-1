'''
gets my user data from github
github doesnt allow git tokens to be pushed, but it works
'''
import requests
from requests.auth import HTTPBasicAuth

def read_password_from_file(file_name):
    with open(file_name, 'rb') as file:
        return file.read()

github_token = read_password_from_file('C:/Users/Eric/Desktop/FunnyPrograms/exp-1/gittoken.txt')
auth = HTTPBasicAuth(github_token, '')#uses the github authentication token to get the data
url = 'https://api.github.com/user'
response = requests.get(url, auth=auth)

user_data = response.json()#json is used so that it becomes a python dict

data = {'username': 'login',
        'company': 'company',
        'location': 'location',#its not literally taking my current position (my specified location is ACRSS)
        'email': 'email',
        'bio': 'bio',
        'amount of followers': 'followers',
        'amount following': 'following',
        'date of creation': 'created_at',
        'date of update': 'updated_at'}


print(f'Here are some aspects of Eric\'s github account:')
for key in data:
    print(f'{key}: {user_data[data.get(key)]}')#prints details