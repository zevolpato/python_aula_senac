"""
  Cap02 - Atividade Extra
  Calculando Raiz Quadrada

  Objetivos:
  Nesta atividade você vai calcular a raiz quadrada a partir do operador matemático ** (exponenciação). O valor será passado pelo usuário e verificaremos se este valor é numerico ou decimal.

  Comandos utilizados:
  Variáveis, operador Exponenciação (**) e métodos isnumeric e isdecimal.
"""
from os import system
system('cls')
print('Vamos calcular a raiz quadrada')
n = input('informe o número: ')
print('O valor é um número inteiro? ' , n.isnumeric())
print('O valor é um número com casas decimais? ' , n.isdecimal())
# ** =  Exponenciação - retorna um número elevado a potência de outro, para raiz quadrada use 1/2
resultado = int(n) ** (1/2)
print('A raiz quadrada de {} é {:.2f}'.format(n, resultado))
