import math


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: introduce un numero valido.")


def calculadora():
    while True:
        print("\n====== CALCULADORA EN PYTHON ======")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Potencia")
        print("6. Raiz cuadrada")
        print("7. Porcentaje")
        print("8. Salir")

        opcion = input("Elige una opcion (1-8): ").strip()

        if opcion == "8":
            print("Gracias por usar la calculadora.")
            break

        if opcion in ("1", "2", "3", "4", "5"):
            a = pedir_numero("Primer numero: ")
            b = pedir_numero("Segundo numero: ")

            if opcion == "1":
                resultado = a + b
            elif opcion == "2":
                resultado = a - b
            elif opcion == "3":
                resultado = a * b
            elif opcion == "4":
                if b == 0:
                    print("Error: no se puede dividir entre cero.")
                    continue
                resultado = a / b
            else:
                resultado = a ** b

            print(f"Resultado: {resultado}")

        elif opcion == "6":
            a = pedir_numero("Numero: ")
            if a < 0:
                print("Error: no existe una raiz real para un numero negativo.")
            else:
                print(f"Resultado: {math.sqrt(a)}")

        elif opcion == "7":
            cantidad = pedir_numero("Cantidad: ")
            porcentaje = pedir_numero("Porcentaje: ")
            print(f"Resultado: {cantidad * porcentaje / 100}")

        else:
            print("Opcion no valida. Elige del 1 al 8.")


if __name__ == "__main__":
    calculadora()