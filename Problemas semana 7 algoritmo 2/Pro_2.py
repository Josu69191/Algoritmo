class TaskQueue:
    """
    Cola de tareas basada en un max-heap.
    Cada entrada en el heap es una tupla (priority, count, description).
    Usamos 'count' para romper empates FIFO cuando varias tareas tienen la misma prioridad.
    """

    def __init__(self):
        # Lista que mantiene el heap
        self.heap = []
        # Contador para mantener el orden de inserción en empates de prioridad
        self._count = 0

    def add_task(self, priority, description):
        """
        Inserta una nueva tarea en el heap.
        - Validamos que 'priority' sea número para evitar errores de comparación.
        - Adjuntamos 'count' para preservar el orden FIFO en prioridades iguales.
        - Llamamos a _up() para restaurar la propiedad de max-heap tras la inserción.
        """
        if not isinstance(priority, (int, float)):
            raise ValueError("priority debe ser numérico")

        # Agregamos la tupla al final de la lista
        self.heap.append((priority, self._count, description))
        # Incrementamos el contador para la siguiente tarea
        self._count += 1
        # Subimos el nuevo elemento hasta su posición correcta
        self._up(len(self.heap) - 1)

    def peek(self):
        """
        Devuelve la descripción de la tarea más urgente sin extraerla.
        Retorna None si la cola está vacía.
        """
        if not self.heap:
            return None
        # El elemento de mayor prioridad siempre está en el índice 0
        return self.heap[0][2]

    def process_task(self):
        """
        Extrae y devuelve la tarea más urgente (priority, description).
        - Intercambiamos la raíz con el último elemento y hacemos pop().
        - Llamamos a _down() para restaurar la propiedad del heap.
        - Retornamos prioridad y descripción de la tarea removida.
        """
        if not self.heap:
            return None

        # Swap raíz <-> último para extraer la máxima prioridad
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        priority, _, description = self.heap.pop()
        # Bajamos el nuevo root hasta su posición correcta
        self._down(0)
        return priority, description

    def _up(self, i):
        """
        Burbujea el elemento en posición i hacia arriba.
        Mientras el padre tenga menor prioridad, los intercambia.
        """
        while i > 0:
            parent = (i - 1) // 2
            # Comparamos (priority, count) para tener en cuenta empates
            if self.heap[i][:2] > self.heap[parent][:2]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _down(self, i):
        """
        Empuja el elemento en posición i hacia abajo.
        Compara con hijos izquierdo y derecho, y hace swap con el mayor si es necesario.
        Repite hasta que la propiedad de max-heap se cumpla.
        """
        size = len(self.heap)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # Verificamos hijo izquierdo
            if left < size and self.heap[left][:2] > self.heap[largest][:2]:
                largest = left

            # Verificamos hijo derecho
            if right < size and self.heap[right][:2] > self.heap[largest][:2]:
                largest = right

            # Si encontramos un hijo mayor, intercambiamos y seguimos bajando
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break


# Ejemplo de uso con 10 tareas para cumplir el enunciado
tasks = TaskQueue()
datos = [
    (3, "Revisar logs"), (8, "Actualizar firmware"), (5, "Reset router"),
    (10, "Restaurar base de datos"), (1, "Inventario equipos"),
    (7, "Configurar VLAN"), (2, "Responder ticket soporte"),
    (9, "Optimizar enrutamiento"), (4, "Auditar seguridad"),
    (6, "Pruebas de conectividad")
]
for p, d in datos:
    tasks.add_task(p, d)

print("Tarea más urgente (peek):", tasks.peek())
print("\nProcesamiento en orden de prioridad:")
while True:
    tarea = tasks.process_task()
    if tarea is None:
        break
    print(f"Procesando: {tarea[1]} (prioridad {tarea[0]})")
