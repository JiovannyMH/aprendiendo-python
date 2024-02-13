#dir = devuelve la lista de atributos validos del objeto pasado, o cosas que se puende hacer
# por ejemplo si es string o un numero nos dice que cosas se pueden hacer, como count etc
cadena1 = "Hola soy Jiovanny"
cadena2 = "Bienvenido maquinola"
cadena3 = "1324"
cadena4 = "hol4a33$$$$$$"
cadena5 = "hola, cómo, está, hoy?"
numero = 4

print("*********Funcion DIR*********")
print(dir(cadena1))
print("\n*********Metodo UPPER*********")
# NO es valido print(UPPER(cadena1)) ya que los metodos se muestran distinto
print(cadena1.upper())
print("\n*********Metodo LOWER*********")
print(cadena1.lower())
print("\n*********Metodo CAPITALIZE*********")
print(cadena1.capitalize())
print("\n*********Metodo FIND*********")
print(cadena2.find("Bienvenido"))
print("\n*********Metodo INDEX*********")
print(cadena1.index("soy"))
print("\n*********Metodo ISNUMERIC*********")
print(cadena3.isnumeric())
print("\n*********Metodo ISALPHA*********")
print(cadena4.isalpha())
print("\n*********Metodo COUNT*********")
print(cadena4.count("$"))
print("\n*********Metodo LEN*********")
print(cadena1.__len__())
print("\n*********Metodo STARTSWITH*********")
print(cadena1.startswith("Hola"))
print("\n*********Metodo ENDSWITH*********")
print(cadena1.endswith("Jiovanny"))
print("\n*********Metodo REPLACE*********")
print(cadena1.replace("Jiovanny","Francisco"))
print("\n*********Metodo SPLIT*********")
print(cadena5.split(","))