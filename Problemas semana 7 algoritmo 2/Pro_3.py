class EventScheduler:
    """
    Organizador de eventos basado en un min-heap.
    Cada entrada es una tupla (date, name).
    El heap siempre sitúa en la raíz el evento con fecha más próxima.
    """

    def __init__(self):
        # Lista interna que representa el heap
        self.heap = []

    def add_event(self, date, name):
        """
        Inserta un nuevo evento en el heap.
        date: entero que simula la fecha (por ejemplo YYYYMMDD)
        name: descripción del evento
        """
        self.heap.append((date, name))
        self._up(len(self.heap) - 1)

    def peek_event(self):
        """
        Devuelve el evento más próximo sin extraerlo.
        Retorna None si no hay eventos.
        """
        return self.heap[0] if self.heap else None

    def next_event(self):
        """
        Extrae y devuelve el evento más próximo.
        Corrige el error de asignar en heap[0] cuando queda vacío.
        """
        if not self.heap:
            return None

        # Intercambiamos raíz y último, luego pop
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        event = self.heap.pop()

        # Solo bajamos si aún quedan elementos
        if self.heap:
            self._down(0)

        return event

    def _up(self, i):
        """
        Ajusta hacia arriba el elemento en posición i
        para restaurar la propiedad de min-heap.
        """
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i][0] < self.heap[p][0]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def _down(self, i):
        """
        Ajusta hacia abajo el elemento en posición i
        comparándolo con sus hijos para mantener el min-heap.
        """
        size = len(self.heap)
        while True:
            left, right = 2*i + 1, 2*i + 2
            smallest = i

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


# Ejemplo de uso
if __name__ == "__main__":
    scheduler = EventScheduler()
    scheduler.add_event(20230515, "Reunión con Clientes")
    scheduler.add_event(20230420, "Conferencia")
    scheduler.add_event(20230610, "Entrega de Proyecto")
    scheduler.add_event(20230301, "Planificación anual")

    print("Próximo evento (sin extraer):", scheduler.peek_event())

    print("\nProcesando eventos en orden cronológico:")
    while True:
        evt = scheduler.next_event()
        if not evt:
            break
        print(f"→ {evt[1]} (fecha {evt[0]})")
