#dict
"""
usuario = {
    "nome" : "jose",
    "sobrenome": "Volpato",
    "fone" : 12982964018,
    "email" : "zevolpato@gmail.com"
}

print(usuario['nome'].upper(), usuario['fone'])

nome = "jose"
print(nome.upper())

produto = {
    "nome" : "camiseta",
    "cores" : ["branca", "preto", "cinza"],
    "tamanho" : ["P", "M", "G", "XG"]
}
#produto["nome"] = "blusa"
produto.update({"nome" : "shorts"})
produto.update({"marca" : ["HD", "OP"]})
produto["marca"][0]= "Oakley"
produto["tamanho"].append("XXG")
produto["cores"].pop(1)
print(produto["nome"])
print(produto["cores"])
print(produto["tamanho"])
print(produto["marca"])
print(produto)
"""

produtos = {
    "cocalata" : {
         "quantidade" : "250ml",
         "valor" : 5.00
    },
    "cocacolalata" : {
        "quantidade" : "350ml",
        "valor" : 6.00
    },
    "coxinha": {
        "tamanho" : "medio", 
        "valor" : 5.00
    }
}

produtos["cocalata"]["valor"] = 7.00
produtos.update({
    "café" : { 
        "tipo": "torrado" 
    }
})

print(produtos)