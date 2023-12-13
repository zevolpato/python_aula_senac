"""
  Cap02 - Atividade 01
  Somando Números

  Objetivos:
  Nesta atividade você vai somar dois numeros usando variáveis e irá verificar os tipo de dados de uma variável e como converter uma variável em um tipo diferente.

  Comandos utilizados:
  Variáveis, type, int, float
"""
# função de soma
print('Vamos fazer a soma de números inteiros')
num1 = input('Informe o primeiro número : ')
num2 = input('Informe o segundo número: ')
soma = num1 + num2
print('A soma entre {} e {} é igual {}' . format(num1, num2, soma))
print('Toda informação recebida pelo comando input é do tipo str')
# o comando type retorna o tipo da variável
print(type(num1))
print('É necessário converter os dados em número, agora a soma vai ficar correta')
# use int para numeros inteiros
soma = int(num1) + int(num2)
print('A soma correta é {}' . format(soma))
