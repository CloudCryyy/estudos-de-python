lista = ["chicago", "queens", "salvador", "pernambuco"]

lista2 = [2, 3, 4, 5, 6]

lista3 = [2.0, 3.5, 7.9]
lista2 = lista2 + lista3
"""
print(sum(lista3))
print(max(lista3))
print(min(lista3))
"""
nome = "curso de python"
valor = range(10)

lista4 = list(nome)
#print(lista4)
lista4 = list(valor)
#print(lista4)

lista5 = ["cachorro", "gato", "cavalo", "girafa", "arraia"]
#print(lista5)
lista5[2] = "vaca"
#print(lista5)

lista5[1:4] = ["águia", "tubarão", "caracol"]

#print(lista5)

listadeAdd = ["carro", "barco", "avião"]

print(listadeAdd)

#sempre que for pedido um print da lista. Os elementos sempre terão a mesma ordem, pois os 
#mesmos estão indexados à lista nessa ordem

for x in listadeAdd:
  print(x)

print(len(listadeAdd))

for x in range(len(listadeAdd)):
  print(x + 1, listadeAdd[x])

texto = "água , peixe , yummi"
texto = texto.split(",")
listaDeTexto = list(texto)
print(listaDeTexto)
"""
o append adiciona 1 argumento
para adicionar mais de um elemento na lista seria necessário 
adionar uma lista dentro da lista com mais elementos

mas como adicionar mais de um elemento a lista de uma sem criar listas dentro de listas?
"""
listaDeTexto.append("gata gorda")
print(listaDeTexto)


"""
a função insert adiciona os elementos em lugares específicos
"""
listaDeTexto.insert(2, "Nautilus")
print(listaDeTexto)


"""
A dúvida era como adicionar muitos elementos de uma vez numa lista
A resposta é com .extend
"""

listaDeTexto.extend(["Mordekaiser", "Nasus", "Wow"])
print(listaDeTexto)

#excluindo elementos da lista
listaDeTexto.pop()
print(listaDeTexto)

listaDeTexto.pop(1)
print(listaDeTexto)

listaDeTexto.remove("Mordekaiser")
print(listaDeTexto)

#remover a lista em si
listaParaRemover = ["Miojo é bom"]
del listaParaRemover

listaParaLimpar = ["Miojo é Ruim"]
print(listaParaLimpar)
listaParaLimpar.clear()
print(listaParaLimpar)

""" 
sort é usado para ordenação
Fato curioso é que o sort ordena as letras minúsculas separadas das maíusculas
então se no meio da lista existirem algumas palavras com letras minúsculas
o sort vai ordenar primeiro as palavras com letras minúsculas e depois as com letras maiúsculas

Para ordenar todas juntas é necessário colocar .sort(key = str.lower) para agregar tanto as 
minúsculas quanto as maiúsculas na lista
"""

carrinhoDeCompras = ["Pão", "Carne", "Sabão"]
carrinhoDeCompras.sort()

print(carrinhoDeCompras)

carrinhoDeCompras.sort(reverse=True) #poderia também ter usado carrinhoDeCompras.reverse() somente
print(carrinhoDeCompras)


#Copiando listas:

listaA = ["a", "b", "c"]
listaB = listaA

listaB.append("d")

print(listaA)
print(listaB)

"""
esse método de cópia não é um bom jeito
o que aconteceu é que o python pegou o mesmo arquivo (listaA) e dividiu as informações dele com
outro (listaB), porém no fim continua sendo o mesmo arquivo com duas "entradas diferentes"
sendo assim quando se adiciona um elemento em 1 das listas, a outra também recebe a informação
"""
listaC = listaA.copy()
listaC.append("e")
print(listaC)

"""
Usando a extensão .copy() é possível criar uma cópia real dos elementos e não só uma troca de
informação entre dois arquivos, sendo assim quando for necessário copiar elementos e que no futuro
terão informações diferentes, é necessário usar lista.copy()
"""

