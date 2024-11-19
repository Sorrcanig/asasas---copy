def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a/b

def calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        # Recibe la entrada del usuario
        eleccion = input("Introduce tu elección (1/2/3/4): ")
        # Verifica si la elección es una de las opciones válidas
        if eleccion in ['1', '2', '3', '4']:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if eleccion == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")

            elif eleccion == '2':
                print(f"{num1} - {num2} = {resta(num1, num2)}")

            elif eleccion == '3':
                print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")

            elif eleccion == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
            
            # Pregunta al usuario si quiere realizar otra operación
            siguiente_calculo = input("¿Quieres realizar otra operación? (sí/no): ")
            if siguiente_calculo.lower() != 'sí':
                break
        else:
            print("Entrada no válida, por favor elige una opción válida.")

if __name__ == "__main__":
    calculadora()