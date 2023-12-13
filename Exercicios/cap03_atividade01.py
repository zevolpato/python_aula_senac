"""
  Cap03 - Atividade 01
  Verificar Número Par e Impar

  Objetivos:
  Nesta atividade você vai usar uma estrutura de decisão (if / else) para verificar se um número é par ou ímpar.

  Comandos utilizados:
  If, operador % (retorna o resto da divisão entre operandos)
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
número = int(input('Informe um número: '))
# operador % restorna o restante de uma divisão
resultado = int(número % 2)
print('Se o resultado for 0 é par e se for 1 é impar, o resultado é:', resultado)
input('Ops, assim ficou ruim... assim fica melhor')
# if é usado para tomada de decisão
# comparação de igualdade no if sempre com ==
if resultado == 0:
  resultado = 'O número é par'
else: 
  resultado = 'O número é impar'
print(resultado)
