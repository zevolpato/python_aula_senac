"""
  Cap08 - Atividade 01
  Criando um Dicionário

  Objetivos:
  Nesta atividade você vai abrir um arquivo e criar um dicionário, o dicionário no Python é muito utilizado quando queremos armazenar dados de forma organizada e que possuam identificação única como num banco de dados.

  Comandos utilizados:
  Dicionário {}, Biblioteca OS, Metodos de string strip() e split()
"""
from os import system, name
import os.path
system('cls') if(name == 'nt') else system('clear')

arquivo = 'categorias.csv'
categorias = open(arquivo, 'r', encoding="utf-8")

dicCategoria = {}

for line in categorias:
  colunas = line.strip().split(";")
  # criar uma lista para as informações do dicionário
  dados = [colunas[1], colunas[2]]
  dicCategoria[colunas[0]] = dados
categorias.close()

# imprimir todo o dicionário
print(dicCategoria)

# imprimir apenas o conteúdo da chave 3 do dicionário
print(dicCategoria['3'])

# imprimir a descrição da conteúdo da chave 3 do dicionário
print(dicCategoria['3'][1])