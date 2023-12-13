"""
  Cap07 - Atividade 01
  Criar um Classe 

  Objetivos:
  Nesta atividade você vai criar uma objeto de classe, aprendendo sobre os metodos e propriedades e usar metodos especiais. Irá também aprender a consumir esta classe.

  Comandos utilizados:
  Classe, __init__, __str__, Propriedades e Metodos de uma classe
"""
from cap07_atividade01Classe import recibo
dados = recibo('Laercio Azevedo de Sa')
dados.valor = 51.13
dados.descricao('desenvolvimento de sistemas em Python')
print(dados._descricao)
print(dados)

