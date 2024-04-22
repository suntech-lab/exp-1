#very simple response getter
import requests

response = requests.get('https://realpython.github.io/fake-jobs/')
print(response.content)