"""
Sistema de gestión de cursos con MergeSort y Búsqueda Binaria.

Problema:
- Ordenar cursos por hora de inicio.
- Permitir búsqueda eficiente de un curso por hora de inicio.

Decisiones:
- Usamos MergeSort porque es O(n log n), estable y se enseña en cursos de Algoritmos II.
- Usamos Búsqueda Binaria porque después de ordenar la lista, la búsqueda en O(log n) es posible.
"""

from typing import List, Dict, Optional

# --------------------------
# Algoritmo MergeSort
# --------------------------
def merge_sort(cursos: List[Dict]) -> List[Dict]:
    """Ordena la lista de cursos por 'hora_inicio' usando MergeSort."""
    if len(cursos) <= 1:
        return cursos

    mid = len(cursos) // 2
    left = merge_sort(cursos[:mid])
    right = merge_sort(cursos[mid:])

    return merge(left, right)

def merge(left: List[Dict], right: List[Dict]) -> List[Dict]:
    """Fusiona dos listas ordenadas por 'hora_inicio' en una sola lista ordenada."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["hora_inicio"] <= right[j]["hora_inicio"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Añadir los elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --------------------------
# Búsqueda Binaria
# --------------------------
def binary_search(cursos: List[Dict], hora: str) -> Optional[Dict]:
    """
    Busca un curso que comience a la hora especificada.
    Devuelve el curso si lo encuentra, None si no existe.
    """
    low, high = 0, len(cursos) - 1

    while low <= high:
        mid = (low + high) // 2
        if cursos[mid]["hora_inicio"] == hora:
            return cursos[mid]
        elif cursos[mid]["hora_inicio"] < hora:
            low = mid + 1
        else:
            high = mid - 1
    return None

# --------------------------
# Programa principal
# --------------------------
if __name__ == "__main__":
    cursos = [
        {"codigo": "MAT101", "nombre": "Matemáticas I", "hora_inicio": "08:00"},
        {"codigo": "FIS202", "nombre": "Física II", "hora_inicio": "10:30"},
        {"codigo": "PROG305", "nombre": "Programación Avanzada", "hora_inicio": "09:15"},
        {"codigo": "HIST110", "nombre": "Historia Universal", "hora_inicio": "07:45"},
        {"codigo": "QUIM150", "nombre": "Química General", "hora_inicio": "14:00"}
    ]

    print("=== Lista de cursos (desordenada) ===")
    for c in cursos:
        print(c)

    # Ordenar con MergeSort
    cursos_ordenados = merge_sort(cursos)

    print("\n=== Lista de cursos (ordenada por hora de inicio) ===")
    for c in cursos_ordenados:
        print(c)

    # Búsqueda de curso
    hora_buscar = input("\nIngrese la hora del curso a buscar (ejemplo 09:15): ")
    curso_encontrado = binary_search(cursos_ordenados, hora_buscar)

    if curso_encontrado:
        print("\nCurso encontrado:")
        print(curso_encontrado)
    else:
        print("\nNo existe un curso a esa hora.")
