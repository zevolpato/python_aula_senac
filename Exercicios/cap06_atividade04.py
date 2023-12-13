"""
  Cap06 - Atividade 04
  Função de Datas

  Objetivos:
  Nesta atividade você vai aprender a usar a biblioteca datetime do python, com ela é possível manipular datas e converter uma string em data. E irá implementar um return numa função.
  
  Comandos utilizados:
  Biblioteca datetime, metodos strptime, strftime e today. Função com return
"""
from datetime import datetime

def idade(nascimento):
  today = datetime.today()
  return today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))

def dias(nascimento):
  today = datetime.today()
  return abs((nascimento - today).days)

print(datetime.now())
atual = datetime.now()
print(type(atual))
montarData = datetime(2021, 10, 5)
print(type(montarData))
print(atual.strftime('%d/%m/%Y %H:%M'))
dataNascimento = input('Informe a sua data de nascimento dd/mm/aaaa: ')
dataNascimento = datetime.strptime(dataNascimento, '%d/%m/%Y')
print(f'Você tem: {idade(dataNascimento)} anos')
print(f'Você já viveu {dias(dataNascimento)} dias')