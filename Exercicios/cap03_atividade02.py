"""
  Cap03 - Atividade 02
  Conversor de Medidas

  Objetivos:
  Nesta atividade você vai converter um número em centimetros para Polegada, Pé ou Jarda. Será necessário usar o comando if / elif / else.

  Comandos utilizados:
  If / elif / else, formatação de números com posição de substituição {:.4f}
"""
from os import system
system('cls') 
print('*** CONVERSOR DE MEDIDAS ***')
# utilize o \n para quebra de linha
medida = float(input('Informe a medida em centímetros: '))
print('\nEscolha para que unidade deseja converter')
print('1 - Polegada\n2 - Pé\n3 - Jarda')
menu = input('Opção: ')
if menu=="1":
  polegadas = medida / 2.54
  resultado = '{:.4f} centímetros correspondem a {:.4f} polegadas' . format(medida, polegadas)
elif menu=="2":
  pes = medida / 30.48
  resultado = '{:.4f} centímetros correspondem a {:.4f} pés' . format(medida, pes)
elif menu=="3":
  jardas = medida / 91.44
  resultado = '{:.4f} centímetros correspondem a {:.4f} jardas' . format(medida, jardas)
else:
  resultado = "Você não escolheu uma das opções..."
print(resultado)