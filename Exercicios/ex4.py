"""
Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo 
e o total de vendas efetuadas por ele no mês (em dinheiro). 
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o
seu nome, o salário fixo e salário no final do mês.

"""
nome = input("Digite o nome do vendedor : ")
salarioFixo = float(input("Digite o salário fixo do vendedor: "))
totalVendasMes = float(input("Digite o total de vendas efetuadas no mês : "))
comissao = totalVendasMes * 0.15
salarioTotal =  salarioFixo + comissao 
salarioLiquido =  salarioTotal - ( salarioTotal * 0.11)
print("O nome do funcionário é : " , nome)
print("O salário fixo é : " , salarioFixo)
print("O salário total foi de : " , salarioFixo + comissao)
print("O salário Liquido foi de : ",  salarioLiquido)