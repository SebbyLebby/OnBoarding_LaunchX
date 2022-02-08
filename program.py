# program.py

#----Saludando----
print("Hola desde la consola")

#----Variables----
sum = 1 + 2
print("1 + 2 =", sum)

product = sum * 2
print("El producto es:", product)

#----Tipos de datos----
planetas_en_el_sistema_solar = 8 #int, plutón ahora es un planeta enano.
distancia_a_alfa_centauri = 4.367 #float, distancia en años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

print("Dato 1:", type(planetas_en_el_sistema_solar))
print("Dato 2:", type(distancia_a_alfa_centauri))
print("Dato 3:", type(puede_despegar))
print("Dato 4:", type(transbordador_que_aterrizo_en_la_luna))

#----Operadores aritméticos----
left_side = 10
right_side = 5

suma = left_side + right_side
resta = left_side - right_side
multiplicacion = left_side * right_side
division = left_side / right_side

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#----Operadores de asignación----
x = 2
x += 2 # x ha incrementado en 2.
x -= 2 # x ha decrementado en 2.
x /= 2 # x ha sido dividido entre 2.
x *= 2 # x ha sido multiplicado por 2.
print(x)

#----Fechas----
from datetime import date

fecha = date.today() # Otorga la fecha del día de hoy.
print("La fecha de hoy es:", fecha) # string, then datetime.date
print(type(fecha)) # Es otro tipo de dato:'datetime.date'
print("Today's date is: " + str(date.today())) # Para concatenar se debe transformar 'datetime.date' -> 'string'.

#----Recopilar información----
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre:")
print("Hello " + name + "!")

print("Calculadora")
first_number = input("Introduzca un número:")
second_number = input("Introduzca otro número:")
print("Resultado incorrecto:" + first_number + second_number) # Marca error porque concatena ambos números al ser datos de tipo 'string'.
print("Resultado correcto:", int(first_number) + int(second_number)) # Resultado correcto de la suma de ambos números.
