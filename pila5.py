# Crear la pila vacía
pila_nombres = []
pila_aux = []

# Ingresar 20 nombres
for i in range(1, 21):
    nombre = input(f"Ingrese el nombre #{i}: ")
    pila_nombres.append(nombre)

print("\n📦 Pila original (LIFO):")
print(pila_nombres)

# Pedir el nombre a eliminar
nombre_eliminar = input("\n🔍 Ingresa el nombre que deseas eliminar (LIFO): ")

# Buscar y eliminar usando LIFO
encontrado = False
while pila_nombres:
    nombre_actual = pila_nombres.pop()
    if nombre_actual == nombre_eliminar:
        print(f"✅ Nombre '{nombre_eliminar}' eliminado.")
        encontrado = True
        break
    else:
        pila_aux.append(nombre_actual)

# Restaurar los nombres que estaban encima
while pila_aux:
    pila_nombres.append(pila_aux.pop())

# Mostrar la pila final
print("\n📦 Pila final (sin el nombre eliminado):")
print(pila_nombres)

if not encontrado:
    print(f"⚠️ El nombre '{nombre_eliminar}' no fue encontrado en la pila.")
