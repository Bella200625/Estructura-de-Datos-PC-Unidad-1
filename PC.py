import random
# Declaramos el arreglo vacío con 10 espacios
""" 
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
    

"""


print ("\n --------Ahora se trabajara con matrices --------")

filas = 3
columnas = 3


# esta matriz esta vacia solo esa rellena de puros ceros
matriz = [[1 for j in range(columnas)] for i in range(filas)]

# doble for pa recorrer tanto filas como columnas 
for i in range(filas):
    for j in range(columnas):
        # random.randint(inicio, fin) genera un número entero aleatorio
        matriz[i][j] = random.randint(1, 9) 

for fila in matriz:
    print(fila)

print ("---------- SUMAA Forma larga (for) -----------")
suma = 0
for i in range (len(matriz)): 
    
    for j in range (len(matriz[0])):
        suma += matriz [i][j]
print (f"La suma de los elementos es {suma}")

print ("---------- SUMAA Forma Corta (sum) -----------")
sumaCorta = 0
for fila in matriz: 
    sumaCorta += sum (fila)
print (f"forma rapida: {sumaCorta}")

print ("-------- Matriz Transpuesta --------")

filas = len(matriz)
columnas = len(matriz[0])

# El primer FOR recorre las COLUMNAS 
for j in range(columnas):
    print(f"--- Columna {j} ---")
    # El segundo FOR recorre las FILAS 
    for i in range(filas):
        print(matriz[i][j])

transpuesta = [list(fila) for fila in zip(*matriz)] 
print(transpuesta)

print("--- RECORRIDO POR COLUMNAS (TABLA) ---")


for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(matriz[i][j], end="   ")
        
    print()

"""
Bueno ahora vamos a intercambiar las filas con las columnas 
"""
print ("----- Intercambiar primera fila por la ultima -----")

matriz [0], matriz [-1] = matriz [-1], matriz [0]
for fila in matriz: 
    print (fila)