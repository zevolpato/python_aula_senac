"""
  Cap09 - Atividade 02
  Extrair dados de filmes do site IMDB
"""
from requests import get
from bs4 import BeautifulSoup
from os import system, name
system('cls') if(name == 'nt') else system('clear')

url = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=user_rating,desc'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
filmes = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(len(filmes))
for i in range(10):
  filme_dados = filmes[i]
  nome = filme_dados.h3.a.text
  lancamento = filme_dados.h3.find('span', class_ = 'lister-item-year text-muted unbold')
  votos = filme_dados.find('span', attrs = {'name':'nv'})
  episodio = filme_dados.h3.find('small', 'text-primary unbold')
  x=""
  if episodio is not None:
    ep = filme_dados.find_all('a')
    x = '- Episodio: ' + ep[2].text
    # print(episodio)
  print('{} - {} {}\nPontuação: {} - Votos: {}' . format(i + 1, nome , lancamento.text, filme_dados.strong.text, votos.text))