# --------------Datos compuestos-----------------

lista = ["Jiovanny", "Francisco","Morales","Hernandez"]
print(lista[2])
print(lista)

#la tupla no se puede modificar y la lista si
tupla=("Jiovanny", "Francisco","Morales","Hernandez")

lista[3] = "Apellido"
print(lista)

# esto no es valido
#tupla[3] = "Apellido"

# creando conjunto set       en los conjuntos no puedo acceder a los indices print(conjunto[1])
# no deja repetir elementos
conjunto={"Jiovanny", "Francisco","Morales","Hernandez"}
print(conjunto)

# creando un diccionario
diccionario = {
    'nombre' : "jerson",
    'nombre2' : "javier",
    'apellido': "Morales",
    'apellido2' : "Hernandez"
}
print(diccionario)
print(diccionario['nombre2'])