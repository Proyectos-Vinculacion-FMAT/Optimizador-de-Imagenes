import os
from supabase import create_client


def get_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    if not url or not key:
        # Intentar cargar desde .env para desarrollo local
        try:
            from dotenv import load_dotenv
            load_dotenv()
            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        except ImportError:
            pass

    if not url or not key:
        raise RuntimeError("Variables de entorno de Supabase no configuradas")

    return create_client(url, key)


def upload_file(local_path: str, remote_path: str) -> str:
    supabase = get_supabase_client()

    with open(local_path, "rb") as f:
        supabase.storage.from_("canaco").upload(
            path=remote_path,
            file=f,
            file_options={"content-type": "image/webp"}
        )

    return supabase.storage.from_("canaco").get_public_url(remote_path)