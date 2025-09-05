#Listas Doblemente Enlazadas

"""
Simulación de un historial de navegación con Lista Doblemente Enlazada (DLL).
Operaciones:
a) Agregar nueva página al final.
b) Retroceder en el historial.
c) Avanzar en el historial.
d) Eliminar una página por su URL.
e) Buscar una página por URL o título.
f) Mostrar el historial completo.
"""

from typing import Optional

# --------------------------
# Nodo de la lista
# --------------------------
class NodoPagina:
    def __init__(self, url: str, titulo: str, hora: str):
        self.url = url
        self.titulo = titulo
        self.hora = hora
        self.prev: Optional["NodoPagina"] = None
        self.next: Optional["NodoPagina"] = None

    def __repr__(self):
        return f"({self.url}, '{self.titulo}', {self.hora})"

# --------------------------
# Lista Doblemente Enlazada
# --------------------------
class HistorialNavegacion:
    def __init__(self):
        self.head: Optional[NodoPagina] = None
        self.tail: Optional[NodoPagina] = None
        self.current: Optional[NodoPagina] = None  # puntero a página actual

    # a) Agregar nueva página al final
    def agregar_pagina(self, url: str, titulo: str, hora: str) -> None:
        nuevo = NodoPagina(url, titulo, hora)
        if self.head is None:  # lista vacía
            self.head = self.tail = nuevo
        else:
            self.tail.next = nuevo
            nuevo.prev = self.tail
            self.tail = nuevo
        self.current = nuevo  # mover al final como "página actual"

    # b) Retroceder en el historial
    def retroceder(self) -> Optional[NodoPagina]:
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current
        return None

    # c) Avanzar en el historial
    def avanzar(self) -> Optional[NodoPagina]:
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current
        return None

    # d) Eliminar una página por su URL
    def eliminar_pagina(self, url: str) -> bool:
        actual = self.head
        while actual:
            if actual.url == url:
                # caso 1: es la cabeza
                if actual == self.head:
                    self.head = actual.next
                    if self.head:
                        self.head.prev = None
                # caso 2: es la cola
                elif actual == self.tail:
                    self.tail = actual.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    actual.prev.next = actual.next
                    actual.next.prev = actual.prev
                # si borramos la actual, mover current
                if self.current == actual:
                    self.current = actual.prev or actual.next
                return True
            actual = actual.next
        return False

    # e) Buscar página por URL o título
    def buscar(self, clave: str) -> Optional[NodoPagina]:
        actual = self.head
        while actual:
            if actual.url == clave or actual.titulo == clave:
                return actual
            actual = actual.next
        return None

    # f) Mostrar historial completo
    def mostrar_historial(self) -> None:
        actual = self.head
        historial = []
        while actual:
            marcador = " <= [Actual]" if actual == self.current else ""
            historial.append(f"{actual}{marcador}")
            actual = actual.next
        print(" ←→ ".join(historial))


# --------------------------
# Ejemplo de uso
# --------------------------
if __name__ == "__main__":
    historial = HistorialNavegacion()

    # Historial inicial
    historial.agregar_pagina("google.com", "Google", "10:00 AM")
    historial.agregar_pagina("wikipedia.org", "Wikipedia", "10:05 AM")
    historial.agregar_pagina("github.com", "GitHub", "10:10 AM")
    historial.agregar_pagina("stackoverflow.com", "Stack Overflow", "10:15 AM")

    print("=== Historial inicial ===")
    historial.mostrar_historial()

    # Retroceder
    print("\nRetroceder:")
    historial.retroceder()
    historial.mostrar_historial()

    # Avanzar
    print("\nAvanzar:")
    historial.avanzar()
    historial.mostrar_historial()

    # Eliminar
    print("\nEliminar github.com:")
    historial.eliminar_pagina("github.com")
    historial.mostrar_historial()

    # Buscar
    print("\nBuscar por título 'Wikipedia':")
    pagina = historial.buscar("Wikipedia")
    print("Encontrado:", pagina)

    # Agregar nueva
    print("\nAgregar nueva página: openai.com")
    historial.agregar_pagina("openai.com", "OpenAI", "10:20 AM")
    historial.mostrar_historial()

