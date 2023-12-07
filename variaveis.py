"""
str = "textos"
int = 10
float = 10.5
boolean = true
# nomes para variavel
nome = "jose afranio volpato junior"
print(nome)
#mostrando o tipo
print(type(nome))
#função length (espaços tb conta)
print(len(nome))
#função Uper case
print(nome.upper())
#for x in nome:
#    print(x)
print(nome[5::])
"""
#a = 10
#b = 3
#c = 5
#print(a)
#print(b)
#print(c)
"""
a,b,c = 10,3,5
print(type(a))
print(a,b,c)
a="jose"
print(type(a))
print(a,b,c)
a=100
print(type(a))
print(a,b,c)
"""

nomeCompleto = "Jose Afranio Volpato Junior"

print(nomeCompleto[0:10]) # primeiros dez caracteres
print(nomeCompleto[-1]) # ultimo caractere
print(nomeCompleto[3:10])
print(nomeCompleto[5::])
print(nomeCompleto[-6:-1])
print(nomeCompleto[-6::])

cpf= "0123456789ab"
print(cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[-2::])

    


