#Autor: Mariana Ponce González A01746107
# ejercicio 2 tarea 3

m = int(input("Dame el numero de mujeres: "))
h = int(input("Dame el numero de hombres: "))

t = m + h
pm = (m/t) * 100
ph = 100 - pm

print("Mujeres inscritas: %d" % (m))
print("Hombres inscritos: %d" % (h))
print("Total de inscritos:  %d" % (t))
print("Porcentaje de mujeres: %.1f" % (pm))
print("Porcentaje de hombres: %.1f" % (ph))