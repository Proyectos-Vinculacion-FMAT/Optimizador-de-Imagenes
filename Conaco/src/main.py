from flask import Flask, request, jsonify
import uuid
import os

from download import download_file
from reduccionDeMemoria import process, resolve_storage_path
from storage import upload_file

app = Flask(__name__)

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        data = request.get_json(force=True)

        signed_url = data.get("signed_url")
        file_type = data.get("file_type")

        if not signed_url or not file_type:
            return jsonify({"error": "signed_url y file_type son requeridos"}), 400

        # 1. Descargar archivo
        input_path = download_file(signed_url)

        # 2. Procesar archivo (SIEMPRE devuelve lista)
        processed_files = process(input_path)

        # 3. Subir resultados
        uploaded_urls = []
        base_path = resolve_storage_path(file_type)

        for local_path in processed_files:
            remote_name = f"{base_path}{uuid.uuid4()}.webp"
            public_url = upload_file(local_path, remote_name)
            uploaded_urls.append(public_url)

        return jsonify({
            "files": uploaded_urls
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
