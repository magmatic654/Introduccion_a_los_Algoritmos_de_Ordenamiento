# 1. Buscar el numero menor en mi lista
# 2. Crear dos sublistas para llevar el control de mi algoritmo
# 3. Imprimir el resultado del ordenamiento
import sys
data1 = [10, 2, 4, 59, 34, 52, 7, 5]

def selectionSort(data):
    # Recorrer toda la lista
    for i in range(len(data)):

        # Encontrar el valor minimo restante dentro de nuestro array desordenado
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                idxDes = j
        # Ya que encontramos el minimo elemento, lo vamos a cambiar 
        # por el primer valor de nuesta lista desordenada
        data[i], data[min_index] = data[min_index], data[i]
# Ejecutar la funcion
selectionSort(data1)
print(data1)