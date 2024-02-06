import numpy as np
import pandas as pd
import heapq
import os

# Cargar los datos desde el archivo CSV
datos = pd.read_csv("golf.csv", header=0)

# Eliminar la columna "Unnamed: 7" si está presente
datos = datos.drop(columns=['Unnamed: 7'], errors='ignore')

# Mostrar los datos cargados
print("\n \n ")
print("\t\t\t  DATOS\n")
print(datos)
print("--------------------------------------------------------------")
print("\n \n \n")

# Convertir datos a formato numpy para facilitar su manipulación
datos = datos.to_numpy()

# Barajar los datos aleatoriamente para mezclar las instancias
np.random.shuffle(datos)

print("datos aleatorios")
print(datos)
print("---------------------------------------------------")
print("\n \n ")

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
entrenamiento1 = datos[0:10].copy()
entrenamiento2 = np.delete(entrenamiento1, 6, axis=1)
print("entrenamiento")
print(entrenamiento2)
print("-------------------")

prueba1 = datos[10:14].copy()
prueba2 = np.delete(prueba1, 6, axis=1)
print("prueba")
print(prueba2)
print("---------------------------------------------------")
print("\n \n \n")

# Solicitar al usuario el valor de k para el algoritmo k-NN
opc = input("\ningrese los k menores -- ")
opc = int(opc)

# Iterar sobre cada instancia en el conjunto de prueba
for j in prueba2:
    print("\n \t para P =", j, "\n")

    # Calcular las distancias entre la instancia de prueba y las instancias de entrenamiento
    k = []
    print('\tDistancias ')
    for i in range(len(entrenamiento2)):
        r = j - entrenamiento2[i]
        # Usar función numpy para calcular la norma euclidiana
        # dist = np.linalg.norm(r)
        # Calcular la distancia euclidiana utilizando la norma L2
        dist = np.sqrt(np.sum(np.square(r)))
        print(entrenamiento2[i], '-->', dist)
        k.append(dist)

    print('\n')
    print("\t", opc, "k menores \n")
    # Encontrar los k menores valores de distancia
    kmenores = heapq.nsmallest(opc, k)

    # Mostrar los k menores valores de distancia
    for i in kmenores:
        print(i)
    print('\n')

    # Obtener las posiciones correspondientes a los k menores valores de distancia
    pos1 = []
    print("\tresultado\n")
    for i in kmenores:
        pos = k.index(i)
        pos1.append(pos)

    # Mostrar los resultados correspondientes a las posiciones obtenidas
    for i in pos1:
        print(entrenamiento1[i])

    # Determinar la clase de la instancia de prueba utilizando el voto mayoritario de los vecinos más cercanos
    sol = np.delete(entrenamiento1, [0, 1, 2, 3, 4, 5], axis=1)
    sol1 = []  # guarda si y no
    for i in pos1:
        sol1.append(sol[i])

    sol1_flat = np.concatenate(sol1)  # Aplanar la lista de arrays

    yes_count = np.count_nonzero(sol1_flat == ' yes')
    no_count = np.count_nonzero(sol1_flat == ' no')

    # Mostrar el resultado final
    print("\n")

    if yes_count > no_count:
        print(j, "--> yes")
    elif yes_count < no_count:
        print(j, "--> no")
    else:
        print(j, "--> igual")

    print("\n---------------------------------------------------")
    os.system(" Pause \n")
