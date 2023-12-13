"""
  Cap06 - Atividade 01
  Criação de Funções

  Objetivos:
  Nesta atividade você vai aprender a criar funções do python, as funções são muito uteis para que você reaproveite código.

  Comandos utilizados:
  Funções def, while
"""
# def = função
def soma(x, y):
  print("Soma: ", x+y)

def subtracao(x, y):
  print("Subtracao: ", x-y)

def multiplicacao(x, y):
  print("Multiplicacao: ", x*y)

def divisao(x, y):
  print("Divisao: ", x/y)

opcao=1
while opcao:
  x = float(input("Primeiro numero: "))
  y = float(input("Segundo numero: "))

  print("1. Somar")
  print("2. Subtrair")
  print("3. Multiplicação")
  print("4. Divisão ")

  operador = int(input("Opção: "))
  if(operador==1):
      soma(x, y)
  if(operador==2):
      subtracao(x, y)
  if(operador==3):
      multiplicacao(x, y)
  if(operador==4):
      divisao(x, y)

  opcao = input("\nAperte 0 para Sair ou Enter para continuar")
  if opcao=="0":
    opcao=int(opcao)