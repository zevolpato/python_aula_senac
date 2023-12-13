"""
  Cap03 - Atividade Extra
  Calcular IMC

  Objetivos:
  Nesta atividade você vai calcular o IMC a partir de um peso e uma altura, usará a comando if para mostrar o resultado do calculo do IMC.

  Comandos utilizados:
  Variáveis, if / elif / else
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
print('*** CALCULADORA DE IMC ***')
peso = int(input('Informe o seu peso em KG: '))
altura = float(input('Agora a sua altura em centimetros: '))/100
imc = peso / (altura * altura)
print("O seu IMC é de {:.2f}".format(imc))
if imc < 18.5:
  resultado = 'Abaixo do Peso'
elif imc < 25:
  resultado = 'Peso Normal'
elif imc < 30:
  resultado = 'Sobrepeso'
elif imc < 35:
  resultado = 'Obesidade Grau I'
elif imc < 40:
  resultado = 'Obesidade Grau II'
else:
  resultado = 'Obesidade Grau III'
print(resultado)
