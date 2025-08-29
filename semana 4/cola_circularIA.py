# Clase original ColaFia
class ColaFia:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)
    
  def enqueue_front(self, element):
    self.queue.insert(0, element)  # Inserta al inicio

  def dequeue(self):
    if self.isEmpty():
      return "La cola está vacía"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "La cola está vacía"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Clase extendida ColaCircular
class ColaCircular(ColaFia):
  def __init__(self, capacidad):
    super().__init__()
    self.capacidad = capacidad
    self.inicio = 0
    self.fin = 0
    self.count = 0
    self.queue = [None] * capacidad  # Sobrescribe con tamaño fijo

  def enqueue(self, element):
    if self.count == self.capacidad:
      return "La cola está llena"
    self.queue[self.fin] = element
    self.fin = (self.fin + 1) % self.capacidad
    self.count += 1

  def enqueue_front(self, element):
    if self.count == self.capacidad:
      return "La cola está llena"
    self.inicio = (self.inicio - 1 + self.capacidad) % self.capacidad
    self.queue[self.inicio] = element
    self.count += 1

  def dequeue(self):
    if self.isEmpty():
      return "La cola está vacía"
    elemento = self.queue[self.inicio]
    self.queue[self.inicio] = None
    self.inicio = (self.inicio + 1) % self.capacidad
    self.count -= 1
    return elemento

  def peek(self):
    if self.isEmpty():
      return "La cola está vacía"
    return self.queue[self.inicio]

  def isEmpty(self):
    return self.count == 0

  def size(self):
    return self.count

  def mostrarCola(self):
    resultado = []
    i = self.inicio
    for _ in range(self.count):
      resultado.append(self.queue[i])
      i = (i + 1) % self.capacidad
    return resultado

# Ejemplo de uso con ColaFia
print("=== ColaFia ===")
myColaMatrucula = ColaFia()
myColaMatrucula.enqueue('Aldo')
myColaMatrucula.enqueue('Bianca')
myColaMatrucula.enqueue('Carlos')

print("Cola: ", myColaMatrucula.queue)
print("Primer elemento: ", myColaMatrucula.peek())
print("Elimina: ", myColaMatrucula.dequeue())
print("Cola después de eliminar: ", myColaMatrucula.queue)
print("Está vacía: ", myColaMatrucula.isEmpty())
print("Tamaño: ", myColaMatrucula.size())

myColaMatrucula.enqueue('Diana')
print("Cola después de agregar un nuevo elemento: ", myColaMatrucula.queue)
print("Nuevo primer elemento: ", myColaMatrucula.peek())
print("Tamaño: ", myColaMatrucula.size())

myColaMatrucula.enqueue_front('Elena')
print("Cola después de agregar un nuevo elemento al inicio: ", myColaMatrucula.queue)
print("Nuevo primer elemento: ", myColaMatrucula.peek())

# Ejemplo de uso con ColaCircular
print("\n=== ColaCircular ===")
miColaCircular = ColaCircular(5)
print("Agregando elementos...")
print(miColaCircular.enqueue('Aldo'))
print(miColaCircular.enqueue('Bianca'))
print(miColaCircular.enqueue('Carlos'))
print("Cola circular: ", miColaCircular.mostrarCola())

print("Elimina: ", miColaCircular.dequeue())
print("Cola después de eliminar: ", miColaCircular.mostrarCola())

print("Agrega Diana: ", miColaCircular.enqueue('Diana'))
print("Agrega Elena al frente: ", miColaCircular.enqueue_front('Elena'))
print("Cola final: ", miColaCircular.mostrarCola())
print("Primer elemento: ", miColaCircular.peek())
print("Tamaño: ", miColaCircular.size())
