"""
  Cap04 - Atividade 02
  MultiTabuada

  Objetivos:
  Nesta atividade você vai construir uma multitabuada de duas maneiras, na primeira usando for e na segunda usando for aninhado

  Comandos utilizados:
   Comandos for range
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
print('\n*** MULTI TABUADA 1 ***')
for i in range(1, 11):
  print('{: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4}' . format(i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10))

print('\n*** MULTI TABUADA 2 ***')
# usando um for dentro de outro
for i in range(1, 11):
  linha = '{: >4} ' . format(i)
  for ii in (range(2, 11)):
    linha+='{: >4} ' . format(ii*i)
  print(linha)
