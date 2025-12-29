from supabase import create_client
import os

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

def upload_to_supabase(local_path, remote_path):
    with open(local_path, "rb") as f:
        supabase.storage.from_("canaco").upload(remote_path, f)

def get_public_url(remote_path):
    res = supabase.storage.from_("canaco").get_public_url(remote_path)
    return res["publicUrl"]
