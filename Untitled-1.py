n = int(input("Dame el numero de veces: "))
v = []
for i in range(n):
    valv = int(input(f"Dame el valor {i+1}: "))
    v.append(valv)

pos = 0
ac = 0
while pos < n:
    ac = ac + v[pos]
    pos = pos + 1

print("La suma es: ", ac)