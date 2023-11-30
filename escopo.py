# escopo / variavel global
x = "Senac"  
# variavel global. Criada fora do escopo Mostrar
def Mostrar():
    print(x)
Mostrar()

x = "Jose"

def MostrarNome():
    x = "SENAC"
    print(x)

MostrarNome()
print(x)



 