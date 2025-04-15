#1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

#Se muestra por pantalla la frase "Hola Mundo"

print("Hola Mundo!")

#2) Pedir nombre al usuario y mostrar un saludo usando el nombre ingresado.

#Se le pide al usuario que ingrese su nombre. 

nombre = input("Ingresá tu nombre: ")

#Se muestra por pantalla el nombre del usuario. 

print(f"Hola {nombre}!")

#3) Diseña un programa que pida al usuario un dato de temperatura en Celsius y que 
#luego muestre su equivalente en Kelvin. 

#Se le pide al usuario que ingrese la temperatura. 

temperaturaC = int (input("Ingresá un dato de temperatura en Celsius: "))

#Se realiza el calculo para pasar de celcius a kelvin. 

temperaturaK = temperaturaC + 273,15

#Se muestra el resultado de la equivalencia. 

print(f"Los {temperaturaC}°C que ingresaste equivalen a: {temperaturaK}°K")

#4) Diseña un programa que pida al usuario una distancia en millas náuticas y que luego 
#muestre su equivalente en metros. 

#Se le pide al usuario que ingrese la distancia.

distancia_millas = int (input("Ingresá una distancia en millas náuticas: "))

#Se realiza el calculo para pasar de metros a millas. 

distancia_metros = distancia_millas * 1852 

#Se muestra por pantalla la equivalencia. 

print(f"La distancia en millas nauticas equivale a: {distancia_metros} metros")

#5) Diseña un programa que calcule el precio final de un artículo. El usuario debe ingresar 
#el precio inicial y el porcentaje de descuento. 

#Se le pide al usuario que ingrese el precio inicial del articulo y el porcentaje de descuento. 

precio_inicial = int (input("Ingresá el precio inicial del articulo: "))
porcentaje_decuento = int (input("Ingrese el porcentaje de descuento: "))

#Se calcula el precio final del articulo con el porcentaje de descuento incluido. 

precio_final = precio_inicial * porcentaje_decuento / 100

#Se muestra por pantalla el precio final del articulo. 

print(f"El precio final del articulo es de: {precio_final}")

#6) Diseña un programa que pida al usuario dos números enteros. Posteriormente 
#muestra por pantalla el resultado de sumarlos, dividirlos, multiplicarlos, restarlos, la 
#potencia del primero elevado al segundo, y el resto de dividir el primero entre el 
#segundo. 

#Se le pide al usuario que ingrese los numeros enteros. 

numero1 = int (input("Ingrese el primer número entero: "))
numero2 = int (input("Ingrese el segundo número entero: "))

#Se realiza el calculo de cada operación.

suma = numero1 + numero2
resta = numero1 - numero2 
multiplicacion = numero1 * numero2
division = numero1 / numero2 
potencia = numero1 ** numero2 
resto = numero1 % numero2 

#Se muestra por pantalla los resultados de cada operación. 

print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
print(f"El resultado de la division es: {division}")
print(f"El resultado de la potencia es: {potencia}")
print(f"El resto de la division es: {resto}")

#7) Escribe un programa que calcule el área y el perímetro de un triángulo rectángulo. El 
#usuario debe proporcionar dos catetos. 

import math 

#Se le solicita al usuario que ingrese los catetos del triángulo rectángulo. 

base = int (input("Ingrese la base del triangulo: "))
altura = int (input("Ingrese la altura del triangulo: "))

#Se calculan los datos del triangulo rectangulo faltantes para luego calcular los parametros que se solicitan. 

area = (base * altura) / 2
hipotenusa = math.sqrt (base ** 2 + altura ** 2) 
perímetro = int (base + altura + hipotenusa) 

#Se imprime pot pantalla el area y el perímetro del triangulo rectángulo. 

print(f"El area del triangulo rectangulo es: {area}")
print(f"El perimetro del triangulo rectangulo es: {perímetro}")

#8) Diseña un programa que calcule las unidades de un número entero dado. 

#Se le pide al usuario que ingrese un número. 

numero = int (input("Ingrese un número: "))

#Se calculan las unidades del numero entero ingresado. 

unidades = numero % 10 

#Se muestra por pantalla las unidades del numero dado. 

print(f"Las unidades del numero que ingresaste son: {unidades}")

#9) Diseñar un programa que dado el precio final de un artículo, calcule cuál es el IVA que 
#tiene incluido. 

#Se le solicita al usuario que ingrese el precio final del artículo. 

precio_final = int (input("Ingrese el precio final del articulo: ")) 

#Se calcula el IVA que tiene incluido el artículo. 

iva = precio_final / (1 + (21 / 100)) * (0.21)

#Se muestra por pantalla cual es el IVA que tiene incluido el artículo. 

print(f"El IVA que tiene incluido el articulo es: {iva}") 

#10) Diseñar un programa que calcule la longitud de una circunferencia y el área. El usuario 
#debe ingresar el radio.

#Se le solicita al usuario que ingrese el radio de la circunferencia. 

radio = int (input("Ingrese el radio de la circunferencia: "))

#Se calcula la circunferencia y el area que se solicita. 

longitud = (2 * 3.14) * radio 
area = 3.14 * radio ** 2

#Se imprimen por pantalla los valores de la longitud y el area de la circunferencia. 

print(f"La longitud de la circunferencia es: {longitud} y el area de la circunferencia es: {area}") 