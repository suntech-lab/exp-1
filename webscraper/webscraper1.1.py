import requests #requests library

URL = "https://www.youtube.com/" #the site that the get method will use
page = requests.get(URL) #the get method is used to get information from a specified URL, like HTML, images, or videos

print(page) #print response