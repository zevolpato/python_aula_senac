"""
  Cap08 - Atividade 01
  Abrir um arquivo 

  Objetivos:
  Nesta atividade você vai ler um arquivo no formato CSV, verificar as opções de enconding (codificação de caracteres) e separar os arquivo em uma lista para ler as informações de cada coluna.

  Comandos utilizados:
  Biblioteca os, comando open, path, lista e for
"""
import os.path, datetime
from os import system, name
system('cls') if(name == 'nt') else system('clear')

arquivo = 'produtos.csv'
if (os.path.isfile(arquivo)):
  produtos = open(arquivo, 'r', encoding="utf-8")
  tamanho = os.path.getsize(arquivo)
  t = os.path.getmtime(arquivo)
  print('Data de Modificação:', datetime.datetime.fromtimestamp(t))
  print('Tamanho do arquivo (bytes):', tamanho)
  listaProdutos = []
  for line in produtos:
    colunas = line.strip().split(";")
    #convertendo os valores para os seus formatos
    #colunas do tipo int
    colunas[0]=int(colunas[0])
    colunas[2]=int(colunas[2])
    colunas[4]=int(colunas[4])
    colunas[5]=int(colunas[5])
    colunas[6]=int(colunas[6])
    colunas[7]=int(colunas[7])
    #colunas do tipo float
    colunas[8]=float(colunas[8])
    colunas[9]=float(colunas[9])
    listaProdutos.append(colunas)
  produtos.close()
  for prod in listaProdutos:
    print(prod)
