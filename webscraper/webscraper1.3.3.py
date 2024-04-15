import requests
import json

def create_post(title, body, user_id):
    url = 'https://jsonplaceholder.typicode.com/posts'
    headers = {'Content-Type': 'application/json'}#tells the website with a header that this type of content is json data (payload header)
    data = {
        'title': title,
        'body': body,
        'userId': user_id
    }

    try:
        payload = json.dumps(data)#uses json library to transform the python dict into json data
        response = requests.post(url, data=payload, headers=headers)#posts the payload to the url with the header
        if response.status_code == 201:#'created' status
            print(f'post details: {response.json()}')#transform back into python dict
        else:
            print(f'failed: {response.status_code}')
            print(f'error: {response.text}')#print error details
    except Exception as e:
        print(f'error occurred: {str(e)}')

'''
function above will take in the details of the post and then transform them from a python dict to a json string
this json string is then, with the post method, posted onto a test website that simulates a real API
this test website does not show any visible change, but does respond
'''

title = 'test post'
body = 'this is a test post made by eric'
user_id = 1 

create_post(title, body, user_id)