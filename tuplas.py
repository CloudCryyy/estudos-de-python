lista = ["item1", "item2", "item3"]
print(lista)
print(len(lista))
print(type(lista))

#tupla x listas
print("------"*10)

tupla = ("item1", "item2", "item3", "item1", "item1")
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[1])
print(tupla.count("item1"))

"""
Uma tupla é imutável, por isso atributos como append, extend, pop or remove não funcionam
como então modificar as informações de uma tupla? transformando em lista
"""
tuplaParaLista = ("item1", "item2", "item3", "item4")
listaParaTupla = list(tuplaParaLista)
print(listaParaTupla)
listaParaTupla.append("item5")
print(listaParaTupla)
tuplaParaLista = tuple(listaParaTupla)
print(tuplaParaLista)

# loops com tupla
tupla1 = ("item1",)
tupla2 = ("item2",)
tupla3 = tupla1 + tupla2 * 3
print(tupla3)

(x, y, *z) = tupla3
print("x:", x)
print("y:", y)
print("z:", z)

tuplaFinal = ("a", "b", "c", "d", "e", "f")
#isso não funcionaria
(a, *b, *c, d) = tuplaFinal
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
