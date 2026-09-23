import os
import sys
import json
import argparse
import qrcode
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_names = []
    if bold:
        font_names = [
            "C:/Windows/Fonts/arialbd.ttf",
            "C:/Windows/Fonts/segoeuib.ttf",
            "C:/Windows/Fonts/calibrib.ttf",
        ]
    else:
        font_names = [
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/segoeui.ttf",
            "C:/Windows/Fonts/calibri.ttf",
        ]
    for fn in font_names:
        if os.path.exists(fn):
            try:
                return ImageFont.truetype(fn, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_centered_text(draw, text, y, font, fill, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x = (width - text_w) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return y + (bbox[3] - bbox[1])

def slugify(text):
    text = text.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n')
    chars = [c if c.isalnum() else '_' for c in text]
    slug = "".join(chars)
    while '__' in slug:
        slug = slug.replace('__', '_')
    return slug.strip('_')

def generar_placa(arbol, base_url, output_path, pure_qr_path=None):
    W, H = 1200, 1680
    card = Image.new('RGB', (W, H), color='#FFFFFF')
    draw = ImageDraw.Draw(card)

    # Bordes institucionales
    border_color = '#007A3D' # Verde municipal Jipijapa
    draw.rounded_rectangle([30, 30, W - 30, H - 30], radius=35, outline=border_color, width=8)
    draw.rounded_rectangle([44, 44, W - 44, H - 44], radius=26, outline='#E2E8F0', width=2)

    # Franja superior
    header_h = 240
    draw.rounded_rectangle([36, 36, W - 36, header_h], radius=26, fill='#007A3D')
    # Franja roja (colores bandera Jipijapa)
    draw.rectangle([36, header_h - 16, W - 36, header_h], fill='#E31837')

    # Textos de cabecera
    font_h1 = get_font(42, bold=True)
    font_h2 = get_font(28, bold=False)
    font_sub = get_font(24, bold=True)

    draw_centered_text(draw, "GAD MUNICIPAL DEL CANTÓN JIPIJAPA", 65, font_h1, '#FFFFFF', W)
    draw_centered_text(draw, "FICHA INFORMATIVA DE LA ESPECIE ARBÓREA", 125, font_h2, '#E2FBE8', W)
    draw_centered_text(draw, "PARQUE CENTRAL • PATRIMONIO NATURAL", 175, font_sub, '#FDE047', W)

    # Badge número de árbol
    badge_w, badge_h = 460, 68
    badge_x = (W - badge_w) // 2
    badge_y = 275
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=20, fill='#F0FDF4', outline='#16A34A', width=3)
    font_badge = get_font(34, bold=True)
    badge_text = f"ÁRBOL N° {arbol['codigo']}"
    draw_centered_text(draw, badge_text, badge_y + 14, font_badge, '#15803D', W)

    # Generación del QR permanente
    url = f"{base_url}{arbol['id']}"
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=18,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#0F172A", back_color="#FFFFFF").convert('RGB')
    
    if pure_qr_path:
        qr_img.save(pure_qr_path, quality=95, dpi=(300, 300))

    # Pegar QR en la placa
    qr_size = 580
    qr_img_resized = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    qr_x = (W - qr_size) // 2
    qr_y = 370
    draw.rounded_rectangle([qr_x - 16, qr_y - 16, qr_x + qr_size + 16, qr_y + qr_size + 16], radius=20, fill='#FFFFFF', outline='#CBD5E1', width=3)
    card.paste(qr_img_resized, (qr_x, qr_y))

    # --- TEXTO DEBAJO DEL QR (Requerimiento explícito: NOMBRE COMÚN ... NIN) ---
    cur_y = qr_y + qr_size + 36

    font_label = get_font(30, bold=True)
    cur_y = draw_centered_text(draw, "NOMBRE COMÚN", cur_y, font_label, '#007A3D', W) + 8

    # Nombre común en tamaño destacado
    nombre = arbol['nombreComun'].upper()
    font_size_name = 56 if len(nombre) <= 15 else (44 if len(nombre) <= 22 else 36)
    font_name = get_font(font_size_name, bold=True)
    cur_y = draw_centered_text(draw, nombre, cur_y, font_name, '#0F172A', W) + 14

    # Nombre científico
    font_sci = get_font(32, bold=False)
    cur_y = draw_centered_text(draw, f"Científico: {arbol['nombreCientifico']}", cur_y, font_sci, '#475569', W) + 10

    # Familia y altura
    font_extra = get_font(26, bold=False)
    extra_text = f"Familia: {arbol['familia']}   |   Altura: {arbol['altura']}"
    cur_y = draw_centered_text(draw, extra_text, cur_y, font_extra, '#64748B', W) + 24

    # Separador sutil
    draw.line([(140, cur_y), (W - 140, cur_y)], fill='#CBD5E1', width=2)
    cur_y += 24

    # Llamado a la acción para escanear
    font_inst = get_font(28, bold=True)
    cur_y = draw_centered_text(draw, "[ Escanea con la camara de tu celular ]", cur_y, font_inst, '#16A34A', W) + 8

    font_desc = get_font(22, bold=False)
    cur_y = draw_centered_text(draw, "Para consultar la ficha tecnica oficial e historia de este arbol", cur_y, font_desc, '#64748B', W) + 8

    font_perm = get_font(20, bold=False)
    draw_centered_text(draw, "Codigo QR permanente sin caducidad • GAD Jipijapa", cur_y, font_perm, '#94A3B8', W)

    card.save(output_path, quality=95, dpi=(300, 300))
    return card

def main():
    parser = argparse.ArgumentParser(description="Generador de Códigos QR para Árboles de Jipijapa")
    parser.add_argument(
        '--url',
        default="https://pincaydamian99-lab.github.io/plantas_jipi/ficha.html?id=",
        help="URL base para los códigos QR"
    )
    args = parser.parse_args()
    base_url = args.url

    output_dir = "qrs_generados"
    pure_dir = os.path.join(output_dir, "qr_puros")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(pure_dir, exist_ok=True)

    with open('data/arboles.json', 'r', encoding='utf-8') as f:
        arboles = json.load(f)

    print(f"Generando placas QR para {len(arboles)} árboles...")
    print(f"URL Base: {base_url}")

    placas_images = []

    for arbol in arboles:
        slug = slugify(arbol['nombreComun'])
        cod = arbol['codigo']
        placa_path = os.path.join(output_dir, f"placa_{cod}_{slug}.png")
        pure_path = os.path.join(pure_dir, f"qr_{cod}.png")
        
        card_img = generar_placa(arbol, base_url, placa_path, pure_path)
        placas_images.append(card_img)
        print(f" -> Generado Árbol #{cod}: {arbol['nombreComun']}")

    # Generar PDF imprimible completo con todas las placas
    pdf_path = os.path.join(output_dir, "placas_imprimibles_jipijapa.pdf")
    if placas_images:
        # Convert to RGB for PDF
        first = placas_images[0].convert('RGB')
        rest = [img.convert('RGB') for img in placas_images[1:]]
        first.save(pdf_path, save_all=True, append_images=rest, resolution=300)
        print(f"\nPDF imprimible completo generado en: {pdf_path}")

    print("\n¡Todas las placas QR han sido generadas exitosamente!")

if __name__ == '__main__':
    main()
