import json
import os
from PIL import Image

os.makedirs('fotos_arboles', exist_ok=True)

with open('data/arboles.json', 'r', encoding='utf-8') as f:
    arboles = json.load(f)

crop_box = (1231, 172, 2225, 890)

for a in arboles:
    img_path = a['imagenFicha']
    if os.path.exists(img_path):
        im = Image.open(img_path)
        cropped = im.crop(crop_box)
        foto_name = f"arbol_{a['codigo']}.jpg"
        save_path = os.path.join('fotos_arboles', foto_name)
        cropped.save(save_path, quality=92, optimize=True)
        a['fotoArbol'] = f"fotos_arboles/{foto_name}"
        print(f"Extraída foto de: {a['codigo']} - {a['nombreComun']}")

with open('data/arboles.json', 'w', encoding='utf-8') as f:
    json.dump(arboles, f, indent=2, ensure_ascii=False)

print("Proceso completado exitosamente.")
