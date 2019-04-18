from bs4 import BeautifulSoup
import requests
import lxml 

base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"

#Sending a request to the web page.
page = requests.get(base_url)

print(type(page))

if page.status_code == requests.codes.ok:
    #get the whole web page in beautiful soup format 
    soup = BeautifulSoup(page.text, 'lxml')
    print(soup.prettify())


