import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

def get_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    if not url or not key:
        raise RuntimeError("Variables de entorno de Supabase no cargadas")

    return create_client(url, key)


def upload_file(local_path: str, remote_path: str) -> str:
    supabase = get_supabase_client()

    with open(local_path, "rb") as f:
        supabase.storage.from_("canaco").upload(
            path=remote_path,
            file=f,
            file_options={"content-type": "image/webp"}
        )

    public_url = supabase.storage.from_("canaco").get_public_url(remote_path)
    return public_url
