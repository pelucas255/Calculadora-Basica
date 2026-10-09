
# Calculadora básica en Python

print("===== CALCULADORA BÁSICA =====")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

while True:
    opcion = input("\nSelecciona una opción: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida. Intenta de nuevo.")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcion == "4":
            if num2 == 0:
                print("Error: no se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print("Resultado:", resultado)

    except ValueError:
        print("Error: debes ingresar números válidos.")