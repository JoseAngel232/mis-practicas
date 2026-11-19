def limpiar_feed(publicaciones: list) -> list:
    if len(publicaciones) <= 1:
        return publicaciones
    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

print("Resultado 1:", limpiar_feed(["Post A", "Post B", "Post B", "Post C", "Post B"]))

#---------------------------------------------limpiador de publicaciones repetidas

def calcular_saldo_final(depositos: list, tasa_intereses: float) -> float:
    if not depositos:
        return 0.0
    return (calcular_saldo_final(depositos[:-1], tasa_intereses) + depositos[-1]) * (1 + tasa_intereses)

print("Resultado 2:", round(calcular_saldo_final([1000, 2000, 1500], 0.05) + 1e-9, 2))

#---------------------------------------------proyeccion de ahorro con interes compuesto

def maxima_profundidad(comentarios: list) -> int:
    if not comentarios:
        return 0
    elem = comentarios[0]
    if isinstance(elem, list):
        actual = 1 + maxima_profundidad(elem)
    else:
        actual = 1
    return max(actual, maxima_profundidad(comentarios[1:]))

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
print("Resultado 3:", maxima_profundidad(hilo))

#---------------------------------------------medir profundidad de un hilo de comentarios