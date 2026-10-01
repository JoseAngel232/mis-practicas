def mostrar_encabezado_escuela():
    print("=" * 45)
    print("UTXJ")
    print("Registro y evaluacion de calificaciones")
    print("=" * 45)

def obtener_nota_minima_aprobatoria():
    return 6.0    

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final < 9.5:
        return "Aprobado"
    else:
        return "Excelente" 


def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    return round(nota_examenes * 0.70 + nota_tareas * 0.30, 1)    

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)
    extraordinario = "Sí" if nota_final < nota_minima else "No"   


    print(f"Alumno:                 {nombre_alumno}")
    print(f"Nota de exámenes (70%): {nota_examenes}")
    print(f"Nota de tareas (30%):   {nota_tareas}")
    print(f"Nota final:             {nota_final}")
    print(f"Estado académico:       {estado}")
    print(f"Examen extraordinario:  {extraordinario}")
    print("-" * 45)    
    
    
mostrar_encabezado_escuela()
generar_boleta("Jose", 7.5, 7.0)
