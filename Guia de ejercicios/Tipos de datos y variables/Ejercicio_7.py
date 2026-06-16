#7.	Crea una calculadora de IMC (Índice de Masa Corporal) con variables peso (float en kg) y altura (float en metros).
#  Declara una variable booleana que indique si el resultado es saludable (IMC entre 18.5 y 24.9).

peso = float(input("ingrese el peso: "))
altura = float(input("Ingrese la altura"))
imc = peso / (altura*altura)
saludable = imc >= 18.5 and imc <25

print (saludable , imc)