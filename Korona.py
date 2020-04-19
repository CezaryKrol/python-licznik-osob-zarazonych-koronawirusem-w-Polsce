import requests
from bs4 import BeautifulSoup

URL = 'https://www.worldometers.info/coronavirus/country/poland/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

klasa = soup.find(class_='maincounter-number')
print("Ilosc osob zarazonych koronawirusem w Polsce: ")
print(klasa.text)
