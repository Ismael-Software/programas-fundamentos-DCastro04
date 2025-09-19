# Ordenar números de mayor a menor
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

print("Los números en orden de mayor a menor son:", a , b , c)
