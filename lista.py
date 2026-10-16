Historial_navegacion = []
Historial_navegacion.append("google.com")
Historial_navegacion.append("youtube.com")
Historial_navegacion.append("wikipedia.com")

print("historial_cargado", Historial_navegacion)
#OPERACION CIMA (TOP/PEEK)

pagina_actual = Historial_navegacion[-1]
print("pagina actual en pantalla;", pagina_actual)

#OPERACION DESAPILAR 
pagina_cerrada = Historial_navegacion.pop()
print("saliendo de", pagina_cerrada)
print("historial despues de cerrar ´Atras´: ", Historial_navegacion)

#TAMAÑO DE LA PILA
total_paginas = len(Historial_navegacion)
print("Paginas previas guardadas: ", total_paginas)

#OPERACION VACIA(EMPY)
sin_paginas = len(Historial_navegacion) ==0
print("¿El historial esta vacio?", sin_paginas)