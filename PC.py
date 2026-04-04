import random

# Declaramos el arreglo vacío con 10 espacios
enteros = [0] * 10

# Usamos un for para recorrer y rellenar con valores aleatorios cada posicion
# range(inicio, parada, incremento) 
for i in range(0, 10, 1):
    enteros[i] = random.randint(1, 100)

print ("------------ Arreglo de enteros ------------")
for numero in enteros:
    print(f"Valor encontrado: {numero}")
    
print ("---Multiplicamos todos los valores por su indice---")
for i in range (len(enteros)):
    enteros [i] *= i 
for i in range (len(enteros)):
    print (f"- {enteros[i]}")

print ("------- Cambiamos los impares por cero -------")

for i in range(0, 10, 1):
    if enteros [i] % 2 != 0:
        enteros [i] = 0
    print(f"Posición {i} llenada con: {enteros[i]}")

print ("---------------- Busqueda lineal ----------------")
while True: 
    try:
        numero = int(input("Dime el número que deseas encontrar: "))
        break # si todo sal bien rompemos el bucle
    except ValueError:
        print("Error ¡ERROOOR!: No es un número Inténtalo de nuevo.")

encontrado = False 
for i in range(len(enteros)):
    if enteros [i] == numero:
        print (f"Encontrado en la posicion: {i}")
        encontrado = True
if not encontrado:
    print (f"El valor {numero} no fue encontrado")
    

