"""
  Cap05 - Atividade 
  Lista de Cadastro

  Objetivos:
  Nesta atividade você vai cadastrar o nome de pessoas e seu celular utilizando listas e ao final irá imprimir uma lista estes dados.

  Comandos utilizados:
  Lista e metodo append
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
opcao = ''
listaNome = []
listaCelular = []
while opcao!='x':
  nome = input("Informe o nome: ")
  celular = input("Informe o celular: ")
  listaNome.append(nome)
  listaCelular.append(celular)
  opcao=input('\nAperte X para Finalizar o cadastro ou qualquer tecla para continuar ')
for i in range(len(listaNome)):
  print('Nome: ', listaNome[i], ' - Celular:' , listaCelular[i])