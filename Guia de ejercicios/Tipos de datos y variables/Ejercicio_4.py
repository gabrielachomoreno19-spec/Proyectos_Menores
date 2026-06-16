# 4.	Declara una variable precio_base (float), un descuento (int, porcentaje) y un producto (string).
#  Muestra el precio final aplicando el descuento.
precio_base = float(input("Ingrese el precio base del producto: "))
descuento = int(input("Ingrese el descuento en porcentaje: "))   
producto = input("Ingrese el nombre del producto: ")
precio_final = precio_base * (1 - descuento / 100)
print(f"el precio final es: {precio_final}")   