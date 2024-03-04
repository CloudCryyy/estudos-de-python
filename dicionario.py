dicio = {"nome": "Gabriel", "ano": 1993, "valor lógico": True}
print(dicio)

dicio["nome"] = "João Vitor"
print(dicio)

for x in dicio.values():
  print(x)

dicio.update({"nome": "Ana"})
print(dicio)

#Se o mesmo for feito com um atributo que não existe, então será criado um novo atributo
dicio.update({"estado": "Rio de Janeiro"})
print(dicio)
#popitem elimina o último item
dicio.popitem()
print(dicio)

dicio.pop("valor lógico")
print(dicio)

del dicio["ano"]
print(dicio)

dicio.clear()
print(dicio)

#Fromkeys função
tupla = ("item1", "item2", "item3")
tupla2 = ("1", "2", "3")
dicio = dict.fromkeys(tupla, tupla2)
print(dicio)