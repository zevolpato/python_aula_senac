"""
  Cap04 - Atividade Extra
  Menu

  Objetivos:
  Nesta atividade você vai criar um menu usando o While, este menu poderá ser utilizado em conjunto com outros códigos para que a execução do programa seja realizado até que o usuário deseje sair.

  Comandos utilizados:
  Variáveis, while
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')

opcao = ''
while opcao!='x':
  print('execução do sistema...\n')
  opcao=input('Escolha uma das opções do menu\nx. Aperte X para Sair ou qualquer tecla para continuar ')
  system('cls') if(name == 'nt') else system('clear')