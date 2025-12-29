import requests
import tempfile

def download_file(url, output_path):
    r = requests.get(url, timeout=30)
    r.raise_for_status()

    ext = url.split("?")[0].split(".")[-1]
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix="." + ext)

    tmp.write(r.content)
    tmp.close()

    return tmp.name

