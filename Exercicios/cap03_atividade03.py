"""
  Cap03 - Atividade 03
  Folha de Pagamento

  Objetivos:
  Nesta atividade você vai calcular uma folha de pagamento usando o comando if aninhado e mostrando o resultado dos valores de Imposto de Renda e INSS a serem pagos.

  Comandos utilizados:
  Variáveis, if, operadores matemáticos e formatação com posição de substituição.
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')
print('*** Folha de Pagamento ***')
salario = float(input('Informe o seu salario: '))
# Calcular INSS
if salario > 6433.58:
  inss = 900.70
else:
  if salario > 3305.23:
    inssP = 0.14
  elif salario > 2203.49:
    inssP = 0.12
  elif salario > 1100.01:
    inssP = 0.09
  else:
    inssP = 0.075
  inss = salario * inssP
base = salario - inss
# Calcular IR
if base > 4664.68:
  irP = 0.275
  deducao = 869.36
elif base > 3751.06:
  irP = 0.225
  deducao = 636.13
elif base > 2826.66:
  irP = 0.15
  deducao = 354.80
elif base > 1903.98:
  irP = 0.075
  deducao = 142.80
else:
  irP = 0
  deducao = 0
ir = (base * irP) - deducao
salarioLiquido = base - ir
print('Salário Bruto: {:.2f}\nSalário Base: {:.2f}\nINSS: {:.2f}\n%IR: {:.2f}%\nValor IR: {:.2f}\nSalário Liquido: {:.2f}' . format(salario, base, inss, irP*100, ir, salarioLiquido))