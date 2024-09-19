#1. - Comenzar a hacer comparaciones de elementos adyacentes
#2. - Repetir hasta tener una pasada completa sin ningun swap

def bubbleSort(data):
    n = len(data)

    # Recorre todos los elementos de la lista
    for i in range(n):
        # Para comparar cada elemento de la lista
        swap = False
        print(data)
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True
        if not swap:
            break
    return data

data_set = [3, 65, 3, 2, 1, 5, 16, 1, 4, 6]
bubbleSort(data_set)

# RETO 1
# Imprimir cada uno de los bucles

# RETO 2
# Detener el programa cuando ya esta ordenado todo