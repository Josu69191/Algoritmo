from collections import deque

# Crear la fila con 15 códigos
fila = deque(range(1, 16))  # Códigos del 1 al 15
print("Fila original:", list(fila))

# Convertir a lista para eliminar por posición
fila_lista = list(fila)

# Eliminar el tercer (índice 2) y séptimo (índice 6) elemento
# Importante: eliminar el mayor índice primero para no alterar posiciones
del fila_lista[6]  # Séptimo
del fila_lista[2]  # Tercero

# Convertir de nuevo a fila
fila = deque(fila_lista)

print("Fila después de eliminar el 3er y 7mo elemento:", list(fila))




