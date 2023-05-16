def imprimirValores(num1, num2):
    print("El valor de Num1 es "+str(num1))
    print("El valor de Num2 es "+str(num2))

def saludar():
    print("Hola Mundo! The Harry Code")

def sumar(num1, num2):
    return num1 + num2

saludar()
num1 = 10
num2 = 11
imprimirValores(num1, num2)
print("El resultado de la suma de los valores es: "+str(sumar(num1, num2))) 

num1 = int(input("Ingrese el valor para num1: "))
num2 = int(input("Ingrese el valor para num2: "))

imprimirValores(num1, num2)
print("El resultado de la suma de los valores es: "+str(sumar(num1, num2))) 