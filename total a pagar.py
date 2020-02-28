#Autor: Mariana Ponce González
#Tarea 2 ejercicio 3

s = int(input("Dame el subtotal "))
p = s * .13
i = s * .16
t = i + p + s

print("Costo de su comida %.2f" % (s))
print("Propina %.2f" % (p))
print("IVA %.2f" % (i))
print("Total a pagar %.2f" % (t))