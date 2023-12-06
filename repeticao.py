listaCarros = ["Opala", "Chevelle", "Zafira ","Mustang", "Omega",  "Astra",  "Uno com escada", "Kadetão"]
"""
# Comandos de repetição

for x in range(5,11):
    print(x)
listaNomes = ["Maria", "Ana", "Pedro", "João"]
for x in listaNomes:
    print(x)

numeros = (3,6,4,9)
soma = 0
for x in numeros:
    soma += x
    print(soma)  # mostra a soma toda vez que passa pelo for
print("O resultado total é : ", soma)

i=0
while i<10:
    print(i)
    i+=1
lista = ["fanta", "coca", "sprite", "tai", "skol", "bohemia"]
i=0
while i < len(lista):
    #print(i ,"  - ", lista[i])
    print(i, " - ", lista[i])
    i+=1
# brake - continue
for x in listaCarros:
    print(x)
i = 0
while i <len(listaCarros):
    if listaCarros[i] == "Omega":
        print( i , " - " , listaCarros[i])
        break
    i+=1
i = 0
while i <len(listaCarros):
    #print( i , " - " , listaCarros[i])
    if listaCarros[i] == "Omega":
        break
    i+=1

#i = 0
#while i <len(listaCarros):
#    i+=1
#    if "Omega" == listaCarros[i]:
#        continue
#    print( i , " - " , listaCarros[i])
for x in listaCarros:
    if x == "Omega":
        continue
    print(x)

i = 0
while i <len(listaCarros):
    #print( i , " - " , listaCarros[i])
    if listaCarros[i] == "Omega":
        break
    i+=1
while i <len(listaCarros):
    print(listaCarros[i])
    i+=1

"""
# ordenar lista
#print(listaCarros)
#listaCarros.sort()
#print(listaCarros)
#for x in listaCarros:
#    print(x)
#listaCarros.sort(reverse = True)
#print(listaCarros)
#posicao = 0
#i=0
#while i < len(listaCarros):
#    if listaCarros[i] == "Mustang":
#        posicao = i
#    i+=1
#print(posicao)
#listaNova = []
#while posicao < len(listaCarros):
#    listaNova.append(listaCarros[posicao])
#    posicao+=1
#print(listaNova)
"""
print(listaCarros)
posicao = 0
i=0
listaNova = []
while i < len(listaCarros):
    if listaCarros[i] == "Mustang":
        posicao = i
    if posicao != 0:
        listaNova.append(listaCarros[posicao])
        posicao+=1
    i+=1

print(listaNova)

"""


# ensinar converter tupla em lista para adicionar e depois converter listsa em tupla para bloquear


tuplaFrutas = ("Maça", "Pera", "Banana", "Morango")
print(type(tuplaFrutas))
x = list(tuplaFrutas)
print(type(x))
x.append("Melancia")
print(x)
tuplaFrutas = tuple(x)
print(type(tuplaFrutas))
print(tuplaFrutas)



