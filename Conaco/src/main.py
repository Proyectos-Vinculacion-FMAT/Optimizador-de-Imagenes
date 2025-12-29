from download import download_file
from reduccionDeMemoria import process, resolve_storage_path
from upload import upload_file
import os

SIGNED_URL = "https://gmyzmyiwpoeteoogleoq.supabase.co/storage/v1/object/sign/canaco/branch/1130cc7f-2479-4993-bec2-5276ab2967f3.jpg?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV85ODcyYTI3OC00MGJkLTQwMWItOTY1My04NzVhMzliYWMwZWQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJjYW5hY28vYnJhbmNoLzExMzBjYzdmLTI0NzktNDk5My1iZWMyLTUyNzZhYjI5NjdmMy5qcGciLCJpYXQiOjE3NjY5NTA0NDEsImV4cCI6MTc2NzAzNjg0MX0.Ik9CF_sXCSFQEq-VSJGhdPg5y0RCXHRp7JhKSNg4jZo&download="
FILE_TYPE = "ComprobanteDomiciliario"
#sa
TMP_PATH = "/tmp/imagen_original.jpg"
print("INICIO DEL SCRIPT")

def pipeline():
    print("Pipeline iniciado")

    # 1. Descargar desde signed URL
    input_path = download_file(SIGNED_URL, TMP_PATH)

    # 2. Reducir memoria (NO se toca la logica interna)
    final_path = process(input_path)

    # 3. Resolver path segun tipo
    storage_path = resolve_storage_path(FILE_TYPE)

    # 4. Subir a Supabase
    public_url = upload_file(
        local_path=final_path,
        remote_path=f"{storage_path}{os.path.basename(final_path)}"
    )

    return public_url


if __name__ == "__main__":
    print(pipeline())
