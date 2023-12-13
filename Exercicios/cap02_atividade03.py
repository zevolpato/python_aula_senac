"""
  Cap02 - Atividade 03
  Trabalhando como Textos

  Objetivos:
  Nesta atividade você vai trabalhar com dados de texto, usando vários metódos para verificar e modificar o valor de uma variável.

  Comandos utilizados:
  Função len e os métodos upper, lower, capitalize, find, replace, isalpha, isalnum, split, center
"""
from os import system
system('cls')
nomecompleto = input('Informe o seu nome completo: ')
# função len retorno a quantidade de caracteres de uma variável
print('1. Quantidade de caracteres:', len(nomecompleto))
# metodos utilizados:
# upper = transforma um texto em maiusculo
# lower = transforma um texto em minusculo
# capitalize = somente a primeira letra em maiusculo
print('2. Nome em maiusculo:', nomecompleto.upper())
print('3. Nome em minusculo:', nomecompleto.lower())
print('4. Primeira letra em maiusculo:', nomecompleto.capitalize())
# metodo find sendo usado para localizar o primeiro espaço em branco
espaco = nomecompleto.find(' ')
# usando a primeira posição de espaco para separar o texto usando a notação [x:x] 
print('5. Somente o primeiro nome:', nomecompleto[0:espaco])
# metodo replace para tirar todos os espacos em branco
print('6. Nome sem espaços:', nomecompleto.replace(' ', ''))
# metodo isaplha para verificar se tem somente letras na palavra
print('7. Tem somente letras? (temos que tirar os espaços para verificar:', nomecompleto.replace(' ', '').isalpha())
# metodo isaplha para verificar se tem somente letras ou numeros na palavra
print('8. É alfanumerico? tem letras ou numeros (temos que tirar os espaços para verificar:', nomecompleto.replace(' ', '').isalnum())
# metodo split para criar uma lista com os nomes usando o espaço em branco como quebra
print('9. Quebrar os texto a cada espaço em branco:', nomecompleto.split(" "))
# metodo center para centrarlizar o texto em 80 colunas usando o *
print('10. Centralizar o nome entre *')
print(nomecompleto.center(80,"*"))
