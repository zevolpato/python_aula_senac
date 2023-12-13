"""
  Cap04 - Atividade 01
  Tabuada

  Objetivos:
  Nesta atividade você vai montar uma Tabuada usando a estrutura de Loop do For e range.

  Comandos utilizados:
  Comandos for e range
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
print('*** Tabuada Simples ***')
multiplicador = int(input('Informe o multiplicador '))
# para criar o loop usaremos a função for e range
for i in range(10):
  print('{} * {} = {}' . format(multiplicador, i, i*multiplicador))
