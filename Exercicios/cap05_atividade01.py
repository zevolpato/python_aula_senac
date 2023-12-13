"""
  Cap05 - Atividade 01
  Número por Extenso

  Objetivos:
  Nesta atividade você vai escrever um número por extenso, para isto usará uma tupla. A tupla é um array que contem dados que não pode ser alterados.

  Comandos utilizados:
  Tupla, operadores / e %
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
# tupla é criada com () e não pode ter seus dados alterados
# lista é criada com [] e pode ter seus dados alterados
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
print(dezenas[2])
pos = int(input('Digite um número entre 0 e 99: '))
if pos < 10:
  extenso = numeros[pos]
elif pos < 20:
  extenso = dez[pos-10]
elif pos <= 99:
  dezena = int(pos / 10) # outra forma de usar seria assim: int(str(pos)[0:1])
  numeral = (pos % 10) # outra forma de usar seria assim: int(str(pos)[1:2])
  numero = ''
  if (numeral!=0):
    numero = ' e ' + numeros[numeral]
  extenso = dezenas[dezena] + numero
else:
  extenso = 'Número maior que 100...'
print(extenso)

