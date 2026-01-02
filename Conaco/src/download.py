import requests
import tempfile

def download_file(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()

    # valida Content-Type
    content_type = r.headers.get("Content-Type", "")
    if "pdf" not in content_type and "image" not in content_type:
        raise ValueError(f"Respuesta no valida: {content_type}")

    ext = "pdf" if "pdf" in content_type else "jpg"

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix="." + ext)
    tmp.write(r.content)
    tmp.close()

    #  valida magic bytes
    with open(tmp.name, "rb") as f:
        header = f.read(4)
        if ext == "pdf" and header != b"%PDF":
            raise ValueError("El archivo descargado no es un PDF valido")

    return tmp.name
