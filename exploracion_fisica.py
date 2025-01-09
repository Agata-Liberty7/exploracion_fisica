from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido al algoritmo de Exploración Física. Usa la ruta /exploracion para comenzar."

@app.route('/exploracion', methods=['POST'])
def exploracion_fisica():
    # Получение данных из запроса
    data = request.json
    if not data:
        return jsonify({"error": "Por favor, envía los datos en formato JSON"}), 400

    resultados = {}

    # Обработка этапов
    resultados["Observación inicial"] = data.get("observacion", "No especificado")
    resultados["Palpación"] = data.get("palpacion", "No especificado")
    resultados["Movilización pasiva"] = data.get("movilizacion", "No especificado")
    resultados["Evaluación del tono muscular"] = data.get("tono_muscular", "No especificado")
    resultados["Pruebas específicas"] = data.get("pruebas", "No especificado")

    # Генерация диагноза и рекомендаций
    diagnostico, recomendaciones = generar_diagnostico_y_recomendaciones(resultados)

    # Ответ
    return jsonify({
        "resultados": resultados,
        "diagnostico": diagnostico,
        "recomendaciones": recomendaciones
    })


def generar_diagnostico_y_recomendaciones(resultados):
    """Генерация диагноза и рекомендаций на основе результатов."""
    diagnostico = []
    if "inclinada" in resultados["Observación inicial"].lower():
        diagnostico.append("Alteración en la postura con posible desequilibrio pélvico.")
    if "severo" in resultados["Palpación"].lower():
        diagnostico.append("Dolor severo en articulaciones con posible inflamación.")
    if "restricción severa" in resultados["Movilización pasiva"].lower():
        diagnostico.append("Limitación severa del rango de movimiento.")
    if "hipotonía" in resultados["Evaluación del tono muscular"].lower():
        diagnostico.append("Reducción del tono muscular en las extremidades posteriores.")
    if "ortolani positiva" in resultados["Pruebas específicas"].lower():
        diagnostico.append("Displasia de cadera severa confirmada.")

    diagnostico_final = " ".join(diagnostico) if diagnostico else "Sin hallazgos significativos."

    recomendaciones = []
    if "dolor severo" in resultados["Palpación"].lower() or "restricción severa" in resultados["Movilización pasiva"].lower():
        recomendaciones.append("Terapia láser: 3-4 veces por semana para aliviar el dolor.")
    if "hipotonía" in resultados["Evaluación del tono muscular"].lower():
        recomendaciones.append("Ejercicios de fortalecimiento: 2-3 veces por semana.")
    if "ortolani positiva" in resultados["Pruebas específicas"].lower():
        recomendaciones.append("Consulta con el veterinario para evaluar cirugía correctiva.")
    if not recomendaciones:
        recomendaciones.append("Monitoreo continuo sin intervención específica.")

    return diagnostico_final, recomendaciones


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
