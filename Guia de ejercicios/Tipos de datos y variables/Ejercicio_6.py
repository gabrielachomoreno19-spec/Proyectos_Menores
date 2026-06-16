#6.	Declara una variable string que almacene una frase y calcula cuántas palabras contiene. 
# Usa otra variable bool para indicar si la frase tiene más de 10 palabras.

frase = input("Ingrese la frase: ")
total_palabras = len(frase.split())
larga = total_palabras > 10

print (f"El total de palabras es: {total_palabras}")
print (larga)