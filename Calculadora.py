
# Calculadora básica en Python

# Funciones matemáticas
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


# Menú principal
def main():
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
                resultado = sumar(num1, num2)
            elif opcion == "2":
                resultado = restar(num1, num2)
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
            else:
                resultado = dividir(num1, num2)

            print("Resultado:", resultado)

        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
        except ValueError:
            print("Error: debes ingresar números válidos.")


# Ejecutar el menú solamente si se abre este archivo
if __name__ == "__main__":
    main()