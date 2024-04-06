import requests #requests library
from bs4 import BeautifulSoup #BeautifulSoup from bs4

URL = "https://realpython.github.io/fake-jobs/" #the site that the get method will use
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='ResultsContainer')

'''
line 7: finds the FIRST element 
(this element is a div(division/section of an html document)) 
with an id attribute of 'ResultsContainer'
'''

job_elements = results.find_all("div", class_="card-content")

'''
line 14: within the results (see line seven), 
finds ALL of the elements (the target elements are div elements) with a CLASS attriute of 'card-content', 
which is pretty self-explanatory
'''

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title") 
    company_element = job_element.find("h3", class_="company") 
    location_element = job_element.find("p", class_="location")

    '''
    lines 23, 24, 25: this is kind of in the same format as lines 7 and 8
    these three lines find the h2, h3, and p's that respectively,
    contain the title, company, and location of each job
    '''

    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

    '''
    lines 33, 34, 35: prints what the lines above have found
    the .text removes all of the html structure and keeps the useful information and the whitespace
    finally, the .strip removes the whitespace, and cleans up the result
    '''

    print() #prints a gap between the job listings
