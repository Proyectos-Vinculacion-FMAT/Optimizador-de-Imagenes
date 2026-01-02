from PIL import Image, UnidentifiedImageError
from pdf2image import convert_from_path
import os


def resolve_storage_path(file_type: str) -> str:
    paths = {
        "CSF": "store/",
        "ComprobanteDomiciliario": "branch/",
        "Ticket": "ticket/",
    }

    if file_type not in paths:
        raise ValueError(f"Tipo de archivo no valido: {file_type}")

    return paths[file_type]


def _is_pdf(path: str) -> bool:
    with open(path, "rb") as f:
        return f.read(4) == b"%PDF"


def process(path: str) -> list[str]:
    if not os.path.exists(path):
        raise FileNotFoundError("Archivo no encontrado")

    carpeta = os.path.dirname(path) or os.getcwd()
    nombre_base = os.path.splitext(os.path.basename(path))[0]

    final_paths = []

    if _is_pdf(path):
        pages = convert_from_path(path)

        for i, page in enumerate(pages):
            final_paths.append(
                _process_image(
                    page,
                    carpeta,
                    f"{nombre_base}_page{i+1}"
                )
            )

    else:
        try:
            img = Image.open(path)
        except UnidentifiedImageError:
            raise ValueError("El archivo no es una imagen valida ni PDF")

        final_paths.append(
            _process_image(img, carpeta, nombre_base)
        )

    return final_paths


def _process_image(img: Image.Image, carpeta: str, nombre_base: str) -> str:
    img_small = img.resize(
        (max(1, img.width // 2), max(1, img.height // 2))
    )

    img_bw = img_small.convert("L")

    final_path = os.path.join(carpeta, f"{nombre_base}_final.webp")
    img_bw.save(final_path, format="WEBP", quality=80)

    return final_path
