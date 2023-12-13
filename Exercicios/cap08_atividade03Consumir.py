"""
  Cap08 - Atividade 03 Consumir
  Criar um Relatório

  Objetivos:
  Nesta atividade você vai salvar um arquivo como um relatório em texto, com as informações das classes realizadas anteriormente.

  Comandos utilizados:
  Bibliotecas, Classe, Salvar um Arquivo, For
"""
import io
from cap08_atividade03Classe import tabCat
from cap08_atividade03Classe import tabProd

cat = tabCat()
prod = tabProd()

dicCategoria = cat.dicCat()
listaProduto = prod.listProd()

relatorio = open("relatorio.txt", mode="w", encoding="utf-8")
for e in dicCategoria:

  titulo = '{}\n{}\n\nProdutos\n' .format(dicCategoria[e][0].upper(), dicCategoria[e][1])
  prod = []
  for p in listaProduto:
    if str(p[2]) == e:
      valor = '{:.2f}' . format(p[8])
      produto = '{:<60} | R$ {:>8}' . format(str(p[1].capitalize() + ' ' + p[3])[0:60], valor)
      prod.append(produto)
  prod.sort()
  lista = ''
  i = 1
  for p in prod:
    lista += '{:>4}. {}\n' . format(i, p)
    i+=1
  divisor = ' Categoria '.center(80,"*")
  relatorio.write(divisor + '\n' + titulo + lista + '\n\n')


categorias = 'Total de Categorias: {:>4}' . format(len(dicCategoria))
produtos = 'Total de Produtos: {:>4}' . format(len(listaProduto))
resumo = ' Resumo '.center(80,"*")
final = "{}\n\n{:>80}\n{:>80}" . format(resumo, categorias, produtos)
relatorio.write(final)
relatorio.close()