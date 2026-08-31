#Programa para inscripcion de cursos, validar edades de los participantes, hacer calculos de costos
#Y si la persona va a tener desceuntos
from validaciones.validaciones import validar_nombre, validar_edad
from matematicas.calculos import calcular_costo

print("===Matricula del curso===")

nombre=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad: "))

##Validar el nombre de la persona
if not validar_nombre(nombre):
    print("Error: el nombre NO puede estar vacio")
elif not validar_edad(edad):
    print("No puedes matricularte")
else:
    valor_hora=int(input("Introduce el valor por hora del curso: "))
    horas=int(input("Introduce la cantidad de horas"))
    costo=calcular_costo(horas,valor_hora)
    print(f"Bienvenido sujeto {nombre}")
    print(f"Costo del curso: {costo}")
