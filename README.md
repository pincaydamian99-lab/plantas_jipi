# 🌳 Sistema de Fichas Informativas y Generador de Códigos QR Permanentes
### GAD Municipal del Cantón Jipijapa - Patrimonio Natural y Arbóreo

Este repositorio contiene la plataforma digital y el generador de **códigos QR permanentes (sin fecha de caducidad)** para las especies arbóreas del Parque Central del Cantón Jipijapa, Manabí, Ecuador.

---

## 📌 ¿Por qué estos códigos QR NO caducan?
Muchos generadores web comerciales (como QR Code Generator, Flowcode, Bitly, etc.) crean enlaces de redirección dinámicos sujetos a periodos de prueba de 14 días para forzar suscripciones mensuales.

**En esta solución:**
1. **Códigos QR Estáticos Directos:** El código QR almacena la dirección URL directa sin ningún intermediario.
2. **Alojamiento Gratuito Permanente en GitHub Pages:** Al estar alojado en GitHub Pages (`https://pincaydamian99-lab.github.io/plantas_jipi/`), el servicio es gratuito, tiene disponibilidad 24/7 y no tiene fecha de vencimiento ni límite de escaneos.

---

## 🎯 Características Principales

1. **Placas y Stickers QR con Nombre Común:**
   - Cada árbol cuenta con una placa gráfica lista para imprimir en alta resolución (300 DPI).
   - Incluye el encabezado institucional del GAD Municipal de Jipijapa.
   - Contiene el código QR en alta calidad.
   - **Muestra claramente en la parte inferior:**
     - `NOMBRE COMÚN: NIN` (o la especie correspondiente en tipografía grande y legible).
     - `Árbol N° 003` | Nombre Científico (*Azadirachta indica*) | Familia botánica.
     - Indicaciones para el visitante: `[ Escanea con la cámara de tu celular ]`.

2. **Ficha Digital Interactiva para Celulares (`ficha.html`):**
   - Se abre al instante al escanear el QR desde cualquier teléfono (Android / iPhone).
   - Visualización de la fotografía del árbol y acceso a la ficha técnica oficial escaneada en alta resolución.
   - Datos botánicos: Nombre común, científico, familia, origen (Nativa / Introducida), altura y estado fitosanitario.
   - **Audioguía interactiva:** Botón con voz en español que narra la ficha del árbol para turistas y personas con discapacidad visual.
   - **Ubicación GPS / Google Maps:** Enlace directo con coordenadas UTM para ubicar el árbol en el mapa del parque.

3. **Panel Web de Control (`index.html`):**
   - Catálogo interactivo de las 20 especies con buscador en tiempo real y filtros.
   - Generación dinámica de QR en el navegador.
   - Descarga directa de placas individuales en formato PNG de alta definición.
   - Descarga de todas las placas comprimidas en un archivo `.ZIP`.
   - Impresión directa desde el navegador o mediante el archivo PDF consolidado.

---

## 📂 Estructura del Proyecto

```text
qr_fotos/
├── index.html                 # Panel principal y generador de placas QR
├── ficha.html                 # Visor web de la ficha interactiva móvil
├── generar_qrs.py             # Script en Python para generar placas y PDF
├── extraer_fotos.py           # Script para recortar y optimizar fotos de árboles
├── README.md                  # Documentación del proyecto
├── data/
│   └── arboles.json           # Base de datos digitalizada de los 20 árboles
├── fotos_arboles/             # Fotografías individuales de los árboles
├── qrs_generados/             # Placas QR en alta resolución (PNG)
│   ├── placas_imprimibles_jipijapa.pdf # PDF listo para imprimir y plastificar
│   ├── placa_001_arbol_de_la_salchichas.png
│   ├── placa_003_nin.png
│   └── ...
└── b497...jpg                 # Fichas técnicas oficiales originales escaneadas
```

---

## 🚀 Cómo activar GitHub Pages para que esté disponible en línea

Una vez subido el código a GitHub:
1. Entra a tu repositorio: `https://github.com/pincaydamian99-lab/plantas_jipi`
2. Ve a la pestaña **Settings** (Configuración) en la parte superior.
3. En el menú izquierdo, haz clic en **Pages**.
4. En **Build and deployment > Branch**:
   - Selecciona la rama `main`.
   - Selecciona la carpeta `/ (root)`.
   - Haz clic en **Save** (Guardar).
5. En 1 minuto tu sitio estará en vivo en:
   👉 **`https://pincaydamian99-lab.github.io/plantas_jipi/`**
6. La ficha del árbol Nin estará directamente accesible en:
   👉 **`https://pincaydamian99-lab.github.io/plantas_jipi/ficha.html?id=003`**

---

## 🖨️ Instrucciones para Imprimir y Colocar en los Árboles

- **Opción 1 (Recomendada):** Abre el archivo `qrs_generados/placas_imprimibles_jipijapa.pdf` e imprímelo en papel adhesivo resistente a la intemperie (vinil adhesivo) o cartulina plastificada.
- **Opción 2:** Entra a `index.html` en tu navegador y presiona el botón **"Imprimir Placas (Navegador)"** para imprimir la selección deseada.
- **Opción 3:** Envía los archivos PNG individuales dentro de `qrs_generados/` para grabado láser en acrílico o metal.
