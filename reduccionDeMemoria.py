from PIL import Image
import os
import sys

def size(p):
    try:
        return os.path.getsize(p)
    except OSError:
        return 0

def process(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No existe la ruta: {path}")

    ext = path.lower().split('.')[-1]
    if ext not in ['jpg', 'jpeg', 'pdf']:
        raise ValueError('Formato no permitido')

    img = Image.open(path)
    if ext == 'pdf':
        img = img.convert('RGB')

    original = size(path)
    log = []

    # Guardar salidas en la misma carpeta que la entrada
    carpeta = os.path.dirname(path) or os.getcwd()
    nombre_base = os.path.splitext(os.path.basename(path))[0]

    img_small = img.resize((max(1, img.width//2), max(1, img.height//2)))
    step1_path = os.path.join(carpeta, f"{nombre_base}_step1.jpg")
    img_small.save(step1_path, quality=85)
    s1 = size(step1_path)
    log.append(f'Resolucion reducida: {original - s1} bytes -> {step1_path}')

    img_bw = img_small.convert('L')
    step2_path = os.path.join(carpeta, f"{nombre_base}_step2.jpg")
    img_bw.save(step2_path, quality=85)
    s2 = size(step2_path)
    log.append(f'Blanco y negro: {s1 - s2} bytes -> {step2_path}')

    final_path = os.path.join(carpeta, f"{nombre_base}_final.webp")
    img_bw.save(final_path, format='WEBP', quality=80)
    s3 = size(final_path)
    log.append(f'WebP: {s2 - s3} bytes -> {final_path}')

    for l in log:
        print(l)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python reduccionDeMemoria.py <ruta_imagen>')
        sys.exit(1)

    try:
        process(sys.argv[1])
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(2)
