from PIL import Image
from pdf2image import convert_from_path
import os

def size(p):
    try:
        return os.path.getsize(p)
    except OSError:
        return 0


def resolve_storage_path(file_type: str) -> str:
    paths = {
        "CSF": "store/",
        "ComprobanteDomiciliario": "branch/",
        "Ticket": "ticket/",
    }

    if file_type not in paths:
        raise ValueError(f"Tipo de archivo no valido: {file_type}")

    return paths[file_type]


def process(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No existe la ruta: {path}")

    ext = path.lower().split('.')[-1]
    carpeta = os.path.dirname(path) or os.getcwd()
    nombre_base = os.path.splitext(os.path.basename(path))[0]

    final_paths = []

    if ext == "pdf":
        pages = convert_from_path(path)

        for i, page in enumerate(pages):
            final_paths.append(
                _process_image(
                    page,
                    carpeta,
                    f"{nombre_base}_page{i+1}"
                )
            )
        return final_paths

    elif ext in ["jpg", "jpeg"]:
        img = Image.open(path)
        return [_process_image(img, carpeta, nombre_base)]

    else:
        raise ValueError("Formato no permitido")


def _process_image(img, carpeta, nombre_base):
    original_size = img.size

    img_small = img.resize(
        (max(1, img.width // 2), max(1, img.height // 2))
    )

    img_bw = img_small.convert("L")

    final_path = os.path.join(carpeta, f"{nombre_base}_final.webp")
    img_bw.save(final_path, format="WEBP", quality=80)

    return final_path
