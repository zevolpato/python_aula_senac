"""
  Cap09 - Atividade 03
  Extrair dados do site Chromedriver
"""
from requests import get
from bs4 import BeautifulSoup
from os import system, name
system('cls') if(name == 'nt') else system('clear')

url = 'https://chromedriver.chromium.org/downloads'
response = get(url)
print(response.status_code)
html_soup = BeautifulSoup(response.content, 'html.parser')
tags = html_soup.find_all('ul')
for i in range(len(tags)):
  if (tags[i].text.find('you are using Chrome version')>0):
    listas = tags[i].find_all('li')
    if (len(listas)>=1):
      print(listas[1].text)
      print(listas[1].text[-12:])
      urldownload = 'https://chromedriver.storage.googleapis.com/' + listas[1].text[-12:] + '/chromedriver_win32.zip'
      print(urldownload)