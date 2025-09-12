import heapq

class ElevatorSimulator:
    """
    Simula un ascensor que siempre atiende primero el piso más cercano
    al piso actual. Reconstruye un min-heap tras cada parada para
    recalcular distancias y preservar orden FIFO en empates.
    """

    def __init__(self, current_floor):
        """
        Inicializa el simulador.
        current_floor -- piso donde arranca el ascensor.
        requests      -- almacena solicitudes como (count, floor).
        _count        -- contador interno para romper empates FIFO.
        heap          -- heap dinámico de (priority, count, floor).
        """
        self.current = current_floor
        self.requests = []
        self._count = 0
        self.heap = []

    def request_floor(self, floor):
        """
        Inserta una nueva solicitud de piso sin calcular aún prioridad fija.
        floor -- entero con el piso que solicita un pasajero.
        """
        self.requests.append((self._count, floor))
        self._count += 1

    def _rebuild_heap(self):
        """
        Reconstruye el heap con prioridades actualizadas:
        priority = distancia absoluta entre floor y self.current.
        El heap almacena (priority, count, floor) para que en caso
        de empate de distancia atienda primero la solicitud más vieja.
        """
        # Generamos la lista de tuplas con distancias actualizadas
        self.heap = [
            (abs(floor - self.current), count, floor)
            for count, floor in self.requests
        ]
        heapq.heapify(self.heap)

    def peek_next(self):
        """
        Devuelve el próximo piso a visitar sin extraerlo.
        Reconstruye el heap para recalcular prioridades.
        Retorna None si no hay solicitudes.
        """
        if not self.requests:
            return None
        self._rebuild_heap()
        _, _, floor = self.heap[0]
        return floor

    def next_stop(self):
        """
        Extrae y devuelve el piso más cercano pendiente.
        1. Reconstruye el heap con distancias actualizadas.
        2. Pop del heap (O(log n)).
        3. Elimina esa solicitud de self.requests.
        4. Actualiza self.current al nuevo piso.
        Retorna None si no hay solicitudes.
        """
        if not self.requests:
            return None

        self._rebuild_heap()
        _, count, floor = heapq.heappop(self.heap)

        # Filtramos la solicitud servida para que no vuelva a aparecer
        self.requests = [
            (cnt, fl) for cnt, fl in self.requests
            if cnt != count
        ]

        # Movemos el ascensor al piso atendido
        self.current = floor
        return floor


if __name__ == "__main__":
    # Ejemplo de uso
    elevator = ElevatorSimulator(current_floor=5)

    # Insertamos varias solicitudes
    for f in [2, 8, 3, 10, 4]:
        elevator.request_floor(f)
        print(f"Solicitud piso {f} registrada. Próximo sin extraer: {elevator.peek_next()}")

    print("\nSimulación de paradas:")
    while True:
        next_floor = elevator.next_stop()
        if next_floor is None:
            print("No quedan solicitudes.")
            break
        print(f"Siguiente piso a visitar: {next_floor} (Ascensor en piso {elevator.current})")