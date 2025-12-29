import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_ROLE_KEY")
)

BUCKET = "canaco"

def upload_file(local_path, remote_path):
    with open(local_path, "rb") as f:
        supabase.storage.from_(BUCKET).upload(
            remote_path,
            f,
            {"content-type": "image/webp"}
        )

    return supabase.storage.from_(BUCKET).get_public_url(remote_path)
