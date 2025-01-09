import json

def exploracion_fisica():
    print("Bienvenido al algoritmo de Exploración Física")
    print("===========================================\n")
    resultados = {}

    # Observación inicial
    print("1. Observación inicial:")
    print("Opciones:")
    print("1. Postura normal, sin tensiones visibles.")
    print("2. Postura inclinada hacia un lado.")
    print("3. Asimetría visible en las extremidades.")
    print("4. Otros (describir manualmente).")
    seleccion = input("Selecciona el número correspondiente: ")
    resultados["Observación inicial"] = interpretar_opcion(seleccion, {
        "1": "Postura normal, sin tensiones visibles.",
        "2": "Postura inclinada hacia un lado.",
        "3": "Asimetría visible en las extremidades.",
        "4": "Otros (describir manualmente): " + input("Describe: ")
    })
    print("\n")
    
    # Palpación
    print("2. Palpación:")
    print("Opciones:")
    print("1. Sin dolor ni anomalías.")
    print("2. Dolor leve en articulaciones.")
    print("3. Dolor severo con inflamación.")
    print("4. Espasmos musculares detectados.")
    print("5. Otros (describir manualmente).")
    seleccion = input("Selecciona el número correspondiente: ")
    resultados["Palpación"] = interpretar_opcion(seleccion, {
        "1": "Sin dolor ni anomalías.",
        "2": "Dolor leve en articulaciones.",
        "3": "Dolor severo con inflamación.",
        "4": "Espasmos musculares detectados.",
        "5": "Otros (describir manualmente): " + input("Describe: ")
    })
    print("\n")
    
    # Movilización pasiva
    print("3. Movilización pasiva:")
    print("Opciones:")
    print("1. Rango de movimiento normal.")
    print("2. Restricción leve en el movimiento.")
    print("3. Restricción severa en el movimiento.")
    print("4. Otros (describir manualmente).")
    seleccion = input("Selecciona el número correspondiente: ")
    resultados["Movilización pasiva"] = interpretar_opcion(seleccion, {
        "1": "Rango de movimiento normal.",
        "2": "Restricción leve en el movimiento.",
        "3": "Restricción severa en el movimiento.",
        "4": "Otros (describir manualmente): " + input("Describe: ")
    })
    print("\n")
    
    # Evaluación del tono muscular
    print("4. Evaluación del tono muscular:")
    print("Opciones:")
    print("1. Tono muscular normal.")
    print("2. Hipotonía (tono reducido).")
    print("3. Hipertonía (tono aumentado).")
    print("4. Otros (describir manualmente).")
    seleccion = input("Selecciona el número correspondiente: ")
    resultados["Evaluación del tono muscular"] = interpretar_opcion(seleccion, {
        "1": "Tono muscular normal.",
        "2": "Hipotonía (tono reducido).",
        "3": "Hipertonía (tono aumentado).",
        "4": "Otros (describir manualmente): " + input("Describe: ")
    })
    print("\n")
    
    # Pruebas específicas
    print("5. Pruebas específicas:")
    print("Opciones:")
    print("1. Pruebas normales sin anomalías.")
    print("2. Prueba de Ortolani positiva.")
    print("3. Restricción en ángulo de Norberg.")
    print("4. Otros (describir manualmente).")
    seleccion = input("Selecciona el número correspondiente: ")
    resultados["Pruebas específicas"] = interpretar_opcion(seleccion, {
        "1": "Pruebas normales sin anomalías.",
        "2": "Prueba de Ortolani positiva.",
        "3": "Restricción en ángulo de Norberg.",
        "4": "Otros (describir manualmente): " + input("Describe: ")
    })
    print("\n")
    
    # Generar diagnóstico preliminar y recomendaciones
    generar_diagnostico_y_recomendaciones(resultados)

    # Guardar resultados
    guardar_resultados(resultados)


def interpretar_opcion(seleccion, opciones):
    """Interpreta la opción seleccionada y devuelve el resultado correspondiente."""
    return opciones.get(seleccion, "Opción no válida.")


def generar_diagnostico_y_recomendaciones(resultados):
    """Genera un diagnóstico preliminar y las recomendaciones de fisioterapia."""
    print("===========================================")
    print("Generando diagnóstico preliminar...\n")

    # Formar diagnóstico
    diagnostico = []
    if "Postura inclinada" in resultados["Observación inicial"]:
        diagnostico.append("Alteración en la postura con posible desequilibrio pélvico.")
    if "Dolor severo" in resultados["Palpación"]:
        diagnostico.append("Dolor severo en articulaciones con posible inflamación.")
    if "Restricción severa" in resultados["Movilización pasiva"]:
        diagnostico.append("Limitación severa del rango de movimiento.")
    if "Hipotonía" in resultados["Evaluación del tono muscular"]:
        diagnostico.append("Reducción del tono muscular en las extremidades posteriores.")
    if "Prueba de Ortolani positiva" in resultados["Pruebas específicas"]:
        diagnostico.append("Displasia de cadera severa confirmada.")
    diagnostico_final = " ".join(diagnostico) if diagnostico else "Sin hallazgos significativos."

    # Crear recomendaciones
    recomendaciones = []
    if "Dolor severo" in resultados["Palpación"] or "Restricción severa" in resultados["Movilización pasiva"]:
        recomendaciones.append("Terapia láser: 3-4 veces por semana para aliviar el dolor.")
    if "Hipotonía" in resultados["Evaluación del tono muscular"]:
        recomendaciones.append("Ejercicios de fortalecimiento: 2-3 veces por semana.")
    if "Prueba de Ortolani positiva" in resultados["Pruebas específicas"]:
        recomendaciones.append("Consulta con el veterinario para evaluar cirugía correctiva.")
    if not recomendaciones:
        recomendaciones.append("Monitoreo continuo sin intervención específica.")

    # Mostrar resultados
    print(f"Diagnóstico preliminar: {diagnostico_final}\n")
    print("Recomendaciones de fisioterapia:")
    for rec in recomendaciones:
        print(f"- {rec}")
    print("===========================================\n")


def guardar_resultados(resultados):
    # Guardar resultados en archivo JSON
    archivo = "resultados_exploracion.json"
    with open(archivo, "w") as f:
        json.dump(resultados, f, indent=4)
    print(f"Resultados guardados en el archivo: {archivo}")


if __name__ == "__main__":
    exploracion_fisica()
