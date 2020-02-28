#Autor: Mariana Ponce González
#Tarea 2 ejercicio extra

x1 = int(input("Dame x1: "))
x2 = int(input("Dame x2: "))
y1 = int(input("Dame y1: "))
y2 = int(input("Dame y2: "))

d = (((x2-x1)**2)+((y2-y1)**2))**.5

print("Distancia: %.3f" % (d))