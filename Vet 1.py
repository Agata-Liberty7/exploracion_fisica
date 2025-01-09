{\rtf1\ansi\ansicpg1251\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import json\
\
def exploracion_fisica():\
    print("Bienvenido al algoritmo de Exploraci\'f3n F\'edsica")\
    print("===========================================\\n")\
    resultados = \{\}\
\
    # Observaci\'f3n inicial\
    print("1. Observaci\'f3n inicial:")\
    print("Opciones:")\
    print("1. Postura normal, sin tensiones visibles.")\
    print("2. Postura inclinada hacia un lado.")\
    print("3. Asimetr\'eda visible en las extremidades.")\
    print("4. Otros (describir manualmente).")\
    seleccion = input("Selecciona el n\'famero correspondiente: ")\
    resultados["Observaci\'f3n inicial"] = interpretar_opcion(seleccion, \{\
        "1": "Postura normal, sin tensiones visibles.",\
        "2": "Postura inclinada hacia un lado.",\
        "3": "Asimetr\'eda visible en las extremidades.",\
        "4": "Otros (describir manualmente): " + input("Describe: ")\
    \})\
    print("\\n")\
    \
    # Palpaci\'f3n\
    print("2. Palpaci\'f3n:")\
    print("Opciones:")\
    print("1. Sin dolor ni anomal\'edas.")\
    print("2. Dolor leve en articulaciones.")\
    print("3. Dolor severo con inflamaci\'f3n.")\
    print("4. Espasmos musculares detectados.")\
    print("5. Otros (describir manualmente).")\
    seleccion = input("Selecciona el n\'famero correspondiente: ")\
    resultados["Palpaci\'f3n"] = interpretar_opcion(seleccion, \{\
        "1": "Sin dolor ni anomal\'edas.",\
        "2": "Dolor leve en articulaciones.",\
        "3": "Dolor severo con inflamaci\'f3n.",\
        "4": "Espasmos musculares detectados.",\
        "5": "Otros (describir manualmente): " + input("Describe: ")\
    \})\
    print("\\n")\
    \
    # Movilizaci\'f3n pasiva\
    print("3. Movilizaci\'f3n pasiva:")\
    print("Opciones:")\
    print("1. Rango de movimiento normal.")\
    print("2. Restricci\'f3n leve en el movimiento.")\
    print("3. Restricci\'f3n severa en el movimiento.")\
    print("4. Otros (describir manualmente).")\
    seleccion = input("Selecciona el n\'famero correspondiente: ")\
    resultados["Movilizaci\'f3n pasiva"] = interpretar_opcion(seleccion, \{\
        "1": "Rango de movimiento normal.",\
        "2": "Restricci\'f3n leve en el movimiento.",\
        "3": "Restricci\'f3n severa en el movimiento.",\
        "4": "Otros (describir manualmente): " + input("Describe: ")\
    \})\
    print("\\n")\
    \
    # Evaluaci\'f3n del tono muscular\
    print("4. Evaluaci\'f3n del tono muscular:")\
    print("Opciones:")\
    print("1. Tono muscular normal.")\
    print("2. Hipoton\'eda (tono reducido).")\
    print("3. Hiperton\'eda (tono aumentado).")\
    print("4. Otros (describir manualmente).")\
    seleccion = input("Selecciona el n\'famero correspondiente: ")\
    resultados["Evaluaci\'f3n del tono muscular"] = interpretar_opcion(seleccion, \{\
        "1": "Tono muscular normal.",\
        "2": "Hipoton\'eda (tono reducido).",\
        "3": "Hiperton\'eda (tono aumentado).",\
        "4": "Otros (describir manualmente): " + input("Describe: ")\
    \})\
    print("\\n")\
    \
    # Pruebas espec\'edficas\
    print("5. Pruebas espec\'edficas:")\
    print("Opciones:")\
    print("1. Pruebas normales sin anomal\'edas.")\
    print("2. Prueba de Ortolani positiva.")\
    print("3. Restricci\'f3n en \'e1ngulo de Norberg.")\
    print("4. Otros (describir manualmente).")\
    seleccion = input("Selecciona el n\'famero correspondiente: ")\
    resultados["Pruebas espec\'edficas"] = interpretar_opcion(seleccion, \{\
        "1": "Pruebas normales sin anomal\'edas.",\
        "2": "Prueba de Ortolani positiva.",\
        "3": "Restricci\'f3n en \'e1ngulo de Norberg.",\
        "4": "Otros (describir manualmente): " + input("Describe: ")\
    \})\
    print("\\n")\
    \
    # Generar diagn\'f3stico preliminar y recomendaciones\
    generar_diagnostico_y_recomendaciones(resultados)\
\
    # Guardar resultados\
    guardar_resultados(resultados)\
\
\
def interpretar_opcion(seleccion, opciones):\
    """Interpreta la opci\'f3n seleccionada y devuelve el resultado correspondiente."""\
    return opciones.get(seleccion, "Opci\'f3n no v\'e1lida.")\
\
\
def generar_diagnostico_y_recomendaciones(resultados):\
    """Genera un diagn\'f3stico preliminar y las recomendaciones de fisioterapia."""\
    print("===========================================")\
    print("Generando diagn\'f3stico preliminar...\\n")\
\
    # Formar diagn\'f3stico\
    diagnostico = []\
    if "Postura inclinada" in resultados["Observaci\'f3n inicial"]:\
        diagnostico.append("Alteraci\'f3n en la postura con posible desequilibrio p\'e9lvico.")\
    if "Dolor severo" in resultados["Palpaci\'f3n"]:\
        diagnostico.append("Dolor severo en articulaciones con posible inflamaci\'f3n.")\
    if "Restricci\'f3n severa" in resultados["Movilizaci\'f3n pasiva"]:\
        diagnostico.append("Limitaci\'f3n severa del rango de movimiento.")\
    if "Hipoton\'eda" in resultados["Evaluaci\'f3n del tono muscular"]:\
        diagnostico.append("Reducci\'f3n del tono muscular en las extremidades posteriores.")\
    if "Prueba de Ortolani positiva" in resultados["Pruebas espec\'edficas"]:\
        diagnostico.append("Displasia de cadera severa confirmada.")\
    diagnostico_final = " ".join(diagnostico) if diagnostico else "Sin hallazgos significativos."\
\
    # Crear recomendaciones\
    recomendaciones = []\
    if "Dolor severo" in resultados["Palpaci\'f3n"] or "Restricci\'f3n severa" in resultados["Movilizaci\'f3n pasiva"]:\
        recomendaciones.append("Terapia l\'e1ser: 3-4 veces por semana para aliviar el dolor.")\
    if "Hipoton\'eda" in resultados["Evaluaci\'f3n del tono muscular"]:\
        recomendaciones.append("Ejercicios de fortalecimiento: 2-3 veces por semana.")\
    if "Prueba de Ortolani positiva" in resultados["Pruebas espec\'edficas"]:\
        recomendaciones.append("Consulta con el veterinario para evaluar cirug\'eda correctiva.")\
    if not recomendaciones:\
        recomendaciones.append("Monitoreo continuo sin intervenci\'f3n espec\'edfica.")\
\
    # Mostrar resultados\
    print(f"Diagn\'f3stico preliminar: \{diagnostico_final\}\\n")\
    print("Recomendaciones de fisioterapia:")\
    for rec in recomendaciones:\
        print(f"- \{rec\}")\
    print("===========================================\\n")\
\
\
def guardar_resultados(resultados):\
    # Guardar resultados en archivo JSON\
    archivo = "resultados_exploracion.json"\
    with open(archivo, "w") as f:\
        json.dump(resultados, f, indent=4)\
    print(f"Resultados guardados en el archivo: \{archivo\}")\
\
\
if __name__ == "__main__":\
    exploracion_fisica()\
\pard\pardeftab720\partightenfactor0

\f1\fs24 \cf0 \
}