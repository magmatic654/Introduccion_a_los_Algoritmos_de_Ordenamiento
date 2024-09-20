# Desafio con selection sort.
# Ejercicio: Ordenar una lista de diccionarios
# Tienes una lista de estudiantes, cada uno representado por un diccionario que contiene su nombre y su edad:

# estudiantes = [
#     {'nombre': 'Ana', 'edad': 22},
#     {'nombre': 'Luis', 'edad': 19},
#     {'nombre': 'Carlos', 'edad': 21},
#     {'nombre': 'Marta', 'edad': 20},
#     {'nombre': 'Pedro', 'edad': 23}
# ]

# Instrucciones:
# Modifica el algoritmo selection_sort para que ordene esta lista de diccionarios en función de la edad de los estudiantes.
# Ordena la lista de estudiantes de acuerdo a su edad en orden ascendente.
# Imprime la lista ordenada al finalizar.

students = [
    {'nombre': 'Ana', 'edad': 22},
    {'nombre': 'Luis', 'edad': 19},
    {'nombre': 'Carlos', 'edad': 21},
    {'nombre': 'Marta', 'edad': 20},
    {'nombre': 'Pedro', 'edad': 23}
]

def selection_sort_students(students):
    for i in range(len(students)):
        min_index = i
        for j in range(i + 1, len(students)):
            if students[j]['edad'] < students[min_index]['edad']:
                min_index = j
        students[min_index], students[i] = students[i], students[min_index]
    return students

new_students = selection_sort_students(list(students))
print(new_students)