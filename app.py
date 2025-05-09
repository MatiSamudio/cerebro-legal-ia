from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from procesador_archivos import extraer_texto_pdf, extraer_texto_imagen
from main import explicar_legal, red_flags, revision_de_permisos

app = Flask(__name__)
CORS(app)  # Habilita CORS para que pueda recibir solicitudes del frontend

@app.route("/analizar", methods=["POST"])
def analizar():
    archivo = request.files.get("archivo")
    modo = request.form.get("modo")
    texto_directo = request.form.get("texto", "")

    if archivo:
        filename = archivo.filename
        ruta_temp = os.path.join("uploads", filename)
        archivo.save(ruta_temp)

        if filename.lower().endswith(".pdf"):
            texto = extraer_texto_pdf(ruta_temp)
        else:
            texto = extraer_texto_imagen(ruta_temp)

        os.remove(ruta_temp)
    elif texto_directo:
        texto = texto_directo
    else:
        return jsonify({"error": "No se recibió archivo ni texto"}), 400

    if modo == "explicacion":
        resultado = explicar_legal(texto)
    elif modo == "redflags":
        resultado = red_flags(texto)
    elif modo == "permisos":
        resultado = revision_de_permisos(texto)
    else:
        resultado = "Modo de análisis no válido."

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
