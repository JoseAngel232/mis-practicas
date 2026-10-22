from collections import deque
cola = deque()
#AGREGAR ELEMENTOS
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
#SACAR EL PRIMER ELEMENTO ATENDIDO(DESENCOLAR)
atendido = cola.popleft()
#MOSTRAR RESULTADOS
print("Atendido", atendido)
print("Cola restante", cola)

#-----------------------------------------------------
from collections import deque
import time
cola_reproduccion = deque()
#AGREGAR ELEMENTO DE REPRODUCCION

cola_reproduccion.append("1.- Mochila azul")
cola_reproduccion.append("2.- Aereolina Carrillo ")
cola_reproduccion.append("3.- La calabaza")
#MOSTRAR LAS CANCIONES
print("Canciones en espera: ")
for cancion in cola_reproduccion:
    print(" _", cancion)
    print("INICIANDO REPRODUCCION")
#DESENCOLAR
while cola_reproduccion:
    cancion_actual = cola_reproduccion.popleft()
    print(f"Sonando ahora:{cancion_actual}")
    time.sleep(1) #SIMULA LA DURACION DEL TEMA
    print(f"Finalizo: {cancion_actual}")
#MUESTRA CUANTAS CANCIONES QUEDAN EN LA COLA
print(f"(Quedan{len(cola_reproduccion)}canciones en la cola)")
print("LA COLA DE REPRODUCCION HA FINALIZADO")    