import math

while True:

print("====== Bienvenido ====")

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. potencia")
print("6. raiz cuadrada")
print("7. porcentaje")
print("8. salir")

opcion = input("elige una opcion: ")

if opcion == "8":
print("hasta luego")

break

if opcion == "1":
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))

resultado = numero1 + numero2  
  
print("Resultado:", resultado)

elif opcion == "2":
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))

resultado = numero1 - numero2  
  
print("Resultado: ", resultado)

elif opcion == "3":
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))

resultado = numero1 * numero2  
  
print("Resultado: ", resultado)

elif opcion == "4":
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
if numero2 or numero1 == 0:
print("Error: no se puede dividir entre 0.")

else:  
    resultado = numero1 / numero2  
  
    print("Resultado: ", resultado)

elif opcion == "5":
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))

resultado = numero1 ** numero2  
  
 print("Resultado: ", resultado)

elif opcion == "6":
numero = float(input("ingrese el numero: "))

if numero < 0:  
    print("Error: no existe raiz cuadrada natural de un numero negativo.")  
     
 else:  
     resultado = math.sqrt(numero)  
      
     print("Resultado: ", resultado)

elif opcion == "7":
numero = float(input("ingrese el numero:, "))
porcentaje = float(input("ingresa el porcentaje: "))

resultado = numero * porcentaje / 100  
  
 print("Resultado: ", resultado)

else:
print("Opcion no valida")

