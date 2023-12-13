"""
  Cap08 - Atividade 03 Classe
  Criando uma Classe

  Objetivos:
  Nesta atividade você vai abrir criar um classe com os dados de um arquivo CSV e retornar um Dicionário.

  Comandos utilizados:
  Classe, Abrir Arquivo, Dicionário
"""
class tabCat:

  def dicCat(self):
    arquivo = 'categorias.csv'
    categorias = open(arquivo, 'r', encoding="utf-8")
    dicCategoria = {}
    for line in categorias:
      colunas = line.strip().split(";")
      dados = [colunas[1], colunas[2]]
      dicCategoria[colunas[0]] = dados
    categorias.close()
    return dicCategoria


class tabProd:
  
  def listProd(self):
    arquivo = 'produtos.csv'
    produtos = open(arquivo, 'r', encoding="utf-8")
    listaProdutos = []
    for line in produtos:
      colunas = line.strip().split(";")
      colunas[0]=int(colunas[0])
      colunas[2]=int(colunas[2])
      colunas[4]=int(colunas[4])
      colunas[5]=int(colunas[5])
      colunas[6]=int(colunas[6])
      colunas[7]=int(colunas[7])
      colunas[8]=float(colunas[8])
      colunas[9]=float(colunas[9])
      listaProdutos.append(colunas)
    produtos.close()
    return listaProdutos