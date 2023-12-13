"""
  Cap06 - Atividade 02
  Tratamento de erros

  Objetivos:
  Nesta atividade você vai criar a utilizar o tratamento de erro do python, irá reutilizar o código da atividade anterior para fazer o tratamento de erros dentro das funções.

  Comandos utilizados:
  Tratamento de erro Try / Except
"""
# def = função
def soma(x, y):
  try:
    print("Soma: ", float(x)+float(y))
  except:
    print("Ocorreu um erro")

def subtracao(x, y):
  try:
    print("Subtracao: ", float(x)-float(y))
  except:
    print("Ocorreu um erro")

def multiplicacao(x, y):
  try:
    print("Multiplicacao: ", float(x)*float(y))
  except:
    print("Ocorreu um erro")

def divisao(x, y):
  try:
    print("Divisao: ", float(x)/float(y))
  except ZeroDivisionError as erro:
    print(erro)
  except:
    print("Ocorreu um erro")

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
  else:
    opcao=1