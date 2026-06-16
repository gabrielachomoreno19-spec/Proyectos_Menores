def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print ("No se puede dividir en 0")

try: 

    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
except ValueError:
    print("Ingrese un numero")

print (f"La suma es: {suma(num1, num2)}")
print (f"La resta es: {resta(num1, num2)}")
print (f"La multiplicacion es: {multiplicacion(num1, num2)}")
print (f"La division es: {division(num1, num2)}")