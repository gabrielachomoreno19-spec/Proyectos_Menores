#10.Declara tres precios de productos (float), súmalos y verifica si el total supera un presupuesto dado (int).
#  Muestra un mensaje distinto según el caso.

presupuesto = 100
producto1 = float(input("Ingrese el precio del producto: "))
producto2 = float(input("Ingrese el precio del producto: "))
producto3 = float(input("Ingrese el precio del producto: "))
total = producto1 + producto2 + producto3

if total > presupuesto: 
    print("No alcanza el presupuesto")
else: 
    print("compra existosa")