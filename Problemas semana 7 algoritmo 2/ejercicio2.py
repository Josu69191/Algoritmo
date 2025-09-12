class PatientQueue:
    def __init__(self):
        # Inicializa la cola de prioridad como una lista vacía (heap máximo)
        self.heap = []

    def insert(self, priority, name):
        # Inserta un nuevo paciente con su prioridad
        self.heap.append((priority, name))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        # Reorganiza el heap desde el índice i hacia arriba
        while i > 0 and self.heap[i][0] > self.heap[(i - 1) // 2][0]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def _heapify_down(self, i):
        # Reorganiza el heap desde el índice i hacia abajo
        size = len(self.heap)
        while 2 * i + 1 < size:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def extract_max(self):
        # Extrae y devuelve al paciente con mayor prioridad (la raíz del heap)
        if not self.heap:
            raise IndexError("La cola está vacía")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek_max(self):
        # Devuelve al paciente más urgente sin extraerlo
        if not self.heap:
            raise IndexError("La cola está vacía")
        return self.heap[0]

    def update_priority(self, name, new_priority):
        # Actualiza la prioridad de un paciente si empeora
        for i, (priority, pname) in enumerate(self.heap):
            if pname == name:
                self.heap[i] = (new_priority, name)
                self._heapify_up(i)
                self._heapify_down(i)
                return
        raise ValueError("Paciente no encontrado")


# Crear la cola de prioridad
pq = PatientQueue()

# Insertar pacientes con diferentes niveles de urgencia
pq.insert(5, "Lucía")    # Prioridad media
pq.insert(3, "Pedro")    # Prioridad baja
pq.insert(10, "Jorge")   # Prioridad alta
pq.insert(7, "María")    # Prioridad media-alta

# Mostrar al paciente más urgente sin atenderlo
print("Paciente más urgente (sin atender):", pq.peek_max())  # Jorge

# Extraer al paciente más urgente (atenderlo)
print("Paciente atendido:", pq.extract_max())  # Jorge

# Mostrar el siguiente paciente más urgente
print("Siguiente paciente urgente:", pq.peek_max())  # María

# Simular que Pedro empeora y su prioridad aumenta
pq.update_priority("Pedro", 9)

# Mostrar el nuevo paciente más urgente después del cambio
print("Paciente más urgente tras actualización:", pq.peek_max())  # Pedro

# Atender al siguiente paciente
print("Paciente atendido:", pq.extract_max())  # Pedro

# Mostrar el estado final de la cola
print("Pacientes restantes en la cola:", pq.heap)
