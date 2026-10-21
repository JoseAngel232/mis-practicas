pila = []

for i in range(1, 11):
    pila.append(f"Plato {i}")

print("Pila despues de apilar 10 elementos: ")
print(pila)

print("\nElemento en la cima: ", pila[-1])

print("\nDesapilando 4 elementos: ")
for _ in range(4):
    print("Se retiro: ", pila.pop())

print("\nPila actual: ", pila)
print("Tamaño: ", len(pila))
print("¿Esta vacia?", len(pila) == 0)

print("\nVaciando la pila por completo: ")
while len(pila) > 0:
    print("Se retiro: ", pila.pop())

print("\nTamaño final: ", len(pila))
print("¿Esta vacia?", len(pila) == 0)    
    