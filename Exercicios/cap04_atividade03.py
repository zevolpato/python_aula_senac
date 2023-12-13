"""
  Cap04 - Atividade 03
  Verificar Número Primo

  Objetivos:
  Nesta atividade você vai verificar se um número é primo ou não e ainda indicar quem é o menor divisor deste número, usando o While para o realizar o loop.

  Comandos utilizados:
  Comando f com variável de substituição, comando while e break e if ternário
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
numero = int(input("Digite um número inteiro: "))
i = 2
divisor = 0
tipo = 'O número deve ser maior que 2'
# usaremos o while para criar o loop
while i < numero:
  tipo = 'O número é PRIMO'
  x = numero % i
  if x == 0:
    divisor = i
    tipo = 'O número não é primo'
    # comando break finaliza um loop
    break
  i = i + 1
# observe que aqui usamos a função f e o nome da variável dentro das {} em vez do comando format
print(tipo)
print(f'O menor divisor é: {divisor}' if divisor > 0 else '')