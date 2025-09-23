#parImpar
numero=int(input("Ingrese un numero: "))
resultado=(numero//2)
residuo=numero-(resultado*2)
if residuo==0:
    print("El número es par.")
else:
    print("El número es impar.")