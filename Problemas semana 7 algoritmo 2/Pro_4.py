import threading

class AlertSystem:
    """
    Sistema de alertas basado en un max-heap.
    Cada tupla en el heap es (priority, -count, symbol):
    - priority: nivel de importancia (0–100)
    - -count: contador negativo para romper empates FIFO
    - symbol: identificador de la alerta
    """

    def __init__(self):
        # Lista interna que representa el heap
        self.heap = []
        # Contador para preservar orden FIFO en prioridades iguales
        self._count = 0
        # Lock para operaciones thread-safe
        self._lock = threading.Lock()

    def insert_alert(self, priority, symbol):
        """
        Inserta una nueva alerta en el heap.
        1. Valida que 'priority' sea numérico y esté en [0, 100].
        2. Añade una tupla (priority, -count, symbol).
        3. Llama a _up() para restaurar la propiedad de max-heap.
        """
        if not isinstance(priority, (int, float)):
            raise ValueError("priority debe ser numérico")
        if priority < 0 or priority > 100:
            raise ValueError("priority debe estar entre 0 y 100")

        with self._lock:
            self.heap.append((priority, -self._count, symbol))
            self._count += 1
            self._up(len(self.heap) - 1)

    def highest_alert(self):
        """
        Devuelve la alerta de mayor prioridad sin extraerla.
        Retorna (priority, symbol) o None si el heap está vacío.
        """
        with self._lock:
            if not self.heap:
                return None
            priority, _, symbol = self.heap[0]
            return priority, symbol

    def extract_alert(self):
        """
        Extrae y devuelve la alerta de mayor prioridad.
        1. Intercambia la raíz con el último elemento.
        2. Hace pop() del último (que era la raíz).
        3. Llama a _down() para restaurar la propiedad de max-heap.
        Retorna (priority, symbol) o None si está vacío.
        """
        with self._lock:
            if not self.heap:
                return None

            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            priority, _, symbol = self.heap.pop()
            if self.heap:
                self._down(0)
            return priority, symbol

    def _up(self, index):
        """
        Ajusta el elemento en 'index' hacia arriba.
        Mientras el padre tenga menor (priority, -count),
        intercambia posiciones.
        """
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index][:2] > self.heap[parent][:2]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def _down(self, index):
        """
        Ajusta el elemento en 'index' hacia abajo.
        Compara con hijos y hace swap con el mayor
        hasta restaurar la propiedad de max-heap.
        """
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left][:2] > self.heap[largest][:2]:
                largest = left
            if right < size and self.heap[right][:2] > self.heap[largest][:2]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index],
                )
                index = largest
            else:
                break


# Bloque de uso corregido para mostrar todas las funciones
if __name__ == "__main__":
    alerts = AlertSystem()

    # Insertamos y mostramos la alerta crítica tras cada inserción
    alerts.insert_alert(4, "ALFA")
    print("Tras insertar ALFA → alerta crítica:", alerts.highest_alert())

    alerts.insert_alert(2, "TUL")
    print("Tras insertar TUL  → alerta crítica:", alerts.highest_alert())

    alerts.insert_alert(5, "GOLF")
    print("Tras insertar GOLF → alerta crítica:", alerts.highest_alert())

    alerts.insert_alert(3, "OSCAR")
    print("Tras insertar OSCAR→ alerta crítica:", alerts.highest_alert())

    print("\nProcesamiento de alertas en orden de prioridad:")

    # Extraemos hasta vaciar y mostramos cada operación
    while True:
        next_alert = alerts.extract_alert()
        if next_alert is None:
            print("No quedan alertas.")
            break

        priority, symbol = next_alert
        print(f"Procesada alerta {symbol} (prioridad {priority})")

        following = alerts.highest_alert()
        if following:
            print("Siguiente alerta crítica:", following)
        else:
            print("Ya no hay alerta crítica.")
