"""
  Cap06 - Atividade Extra
  Acertando o Símbolo

  Objetivos:
  Nesta atividade você vai criar um jogo onde irá acertar um símbolo através de um calculo matemático. 

  Comandos utilizados:
  Variáveis, while
"""
import random
from os import system
system('cls')

def tabuleiro(x):
  print('VOU ACERTAR O SIMBOLO QUE VC PENSAR'.center(79 , '*'))
  for i in range(0, 10):
    linha=''
    for ii in (range(1, 11)):
      numero = ii+(10*i)
      if not (numero%9):
        caracter = x
      else:
        caracter = random.randrange(16,25)
        while (caracter == x):
          caracter = random.randrange(16,25)
      linha+='{: >3} {} | ' . format(numero, chr(caracter))
    print(linha)
  print('*'*79)

opcao=1

while opcao:

  x = random.randint(16, 25)
  tabuleiro(x)
  input('Pense em um numero de 11 a 99 e aperte Enter ')
  input('Faça a soma dos digitos, exemplo o numero foi 22 = 2+2 e aperte Enter ')
  input('Agora faça o numero menos a soma deles (exemplo 22 - 4 = 18) e aperte Enter ')
  print('O simbolo é {}' . format(chr(x)))
  input('Opa o meu exemplo também deu certo!!!')
  system('cls')
  try:
    opcao = int(input("[1]. Aperte 1 para continuar: "))
    if opcao!=1:
      opcao = 0
  except:
    opcao = 0
  system('cls')