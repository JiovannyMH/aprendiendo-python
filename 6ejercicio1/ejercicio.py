#*************** A jercicio de tiempo de video*************** 
tiempo_minimo = 2.5
tiempo_maximo = 7
tiempo_promedio = 4
tiempo_este_curso = 1.5

#diferencia en porcentaje entre este curso y el tiempo minimo
porcentaje1 = 100-(tiempo_este_curso/ tiempo_minimo*100)
#diferencia en porcentaje entre este curso y el tiempo maximo
porcentaje2 = 100-(tiempo_este_curso/tiempo_maximo*100)
redondear1 = round(porcentaje2,2)
#promedio en procentaje entre el tiempo de curso y el promedio
porcentaje3 = 100-tiempo_este_curso/tiempo_promedio*100
print(f'Ejercicio A')
print(f'el porcentaje entre estos dos videos es de : {porcentaje1} %')
print(f'el porcentaje entre estos dos videos es de : {redondear1} %')
print(f'el promedio entre los videos es de : {porcentaje3} %')

#**************B tiempo de crudos(videos sin editar)********************
otros_promedio_crudo = 5
promedio_dalto = 3.5

# calculando tiempo vacio removido
tiempo_vacio_removido = porcentaje2 = 100- tiempo_promedio * 1000 // otros_promedio_crudo / 10
tiempo_vacio_removido_dalto = porcentaje2 = 100- tiempo_este_curso * 1000 // promedio_dalto / 10
print(f'Ejercicio B')
print(f'Los cursos normales eliminan un promedio de tiempo de : {tiempo_vacio_removido} %')
print(f'en el curso de Dalto el tiempo reducido es de : {tiempo_vacio_removido_dalto} %')