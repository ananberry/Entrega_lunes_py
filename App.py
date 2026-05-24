from flask import Flask, jsonify

import funciones as pp
import Visualizaciones as vz

app = Flask(__name__)


@app.route("/")
def home():
    return "API de gráficos funcionando 🚀 Ve a /graficos"


@app.route("/graficos")
def obtener_graficos():

    df = pp.cargar_prestamos()
    df = pp.limpiar_prestamos(df)

    grafico1 = vz.graficar_frecuencia(df)
    grafico2 = vz.graficar_estados(df)

    return jsonify({
        "frecuencia": grafico1,
        "estados": grafico2
    })


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
