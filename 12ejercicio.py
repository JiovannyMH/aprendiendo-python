# jercicio de tiempo de video 
tiempo_minimo = 2.5
tiempo_maximo = 7
tiempo_promedio = 4
tiempo_este_curso = 1.5

#diferencia en porcentaje entre este curso y el tiempo minimo
porcentaje1 = 100-(tiempo_este_curso/ tiempo_minimo*100)
#diferencia en porcentaje entre este curso y el tiempo maximo
porcentaje2 = 100-(tiempo_este_curso/tiempo_maximo*100)
redondear1 = round(porcentaje2,2)
#promedio de cursos
porcentaje3 = (tiempo_este_curso + tiempo_maximo + tiempo_minimo +tiempo_promedio) / 4
print(f'el porcentaje entre estos dos videos es de : {porcentaje1} %')
print(f'el porcentaje entre estos dos videos es de : {redondear1} %')
print(f'el porcentaje entre estos dos videos es de : {porcentaje3} h')
