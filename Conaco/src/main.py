from flask import Flask, request, jsonify
from download import download_file
from reduccionDeMemoria import process, resolve_storage_path
from upload import upload_file
import os
import uuid

app = Flask(__name__)

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.get_json(force=True)

    signed_url = data.get("signed_url")
    file_type = data.get("file_type")

    if not signed_url or not file_type:
        return jsonify({"error": "signed_url y file_type son requeridos"}), 400

    tmp_input = f"/tmp/{uuid.uuid4()}.jpg"

    try:
        # 1. Descargar
        input_path = download_file(signed_url, tmp_input)

        # 2. Optimizar
        final_path = process(input_path)

        # 3. Resolver path
        storage_path = resolve_storage_path(file_type)

        # 4. Subir a Supabase
        public_url = upload_file(
            local_path=final_path,
            remote_path=f"{storage_path}{os.path.basename(final_path)}"
        )

        return jsonify({"public_url": public_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Cloud Run espera esto
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
