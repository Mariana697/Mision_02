#Autor: Mariana Ponce González A01746107
# ejercicio 2 tarea 2

d = int(input("Dame la distancia "))
t = int(input("Dame el tiempo "))
v = d/t
d1 = v * 6
d2 = v * 3.5
t1 = 485 / v

print("Velocidad del auto en km/h: %d" % (v))
print("Distancia recorrida en 6 hrs: %.1f" % (d1))
print("Distancia recorrida en 3.5 hrs: %.1f" % (d2))
print("Tiempo para recorrer 485 km: %.1f" % (t1))
