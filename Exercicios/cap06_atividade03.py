"""
  Cap06 - Atividade 03
  Biblioteca Math

  Objetivos:
  Nesta atividade você vai importar a biblioteca math, visualizar a ajuda da biblioteca e usar algumas das principais funções.

  Comandos utilizados:
  Biblioteca math, funções ceil, fabs, floor, fmod, trunc
"""
import math
# use o comando help(biblioteca) para visualizar a sua ajuda
help(math)
# inteiro para cima
print(math.ceil(4.2))
# inteiro para baixo
print(math.floor(3.9))
# número absoluto
print(math.fabs(-1))
# mod = restante de uma divisão
print(math.fmod(9, 4))
# raiz quadrada
print(math.sqrt(36))
# não faz parte da bibilioteca math, é usado para arredondar um número.
print(round(3.988, 1))
