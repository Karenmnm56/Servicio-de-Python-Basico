# Calculadora en pythonnnnn
print("CALCULADORA EN PYTHON")
num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    if operacion == "-":
        return num_1 - num_2
    if operacion == "*":
        return num_1 * num_2
    if operacion == "/":
        return num_1 / num_2

if operacion == "+":
    resultado = calculadora(num_1, num_2, operacion)
    print("El resultado es: ", resultado)

if operacion == "-":
    resultado = calculadora(num_1, num_2, operacion)
    print("El resultado es: ", resultado)

if operacion == "*":
    resultado = calculadora(num_1, num_2, operacion)
    print("El resultado es: ", resultado)

if operacion == "/":
    resultado = calculadora(num_1, num_2, operacion)
    print("El resultado es: ", resultado)