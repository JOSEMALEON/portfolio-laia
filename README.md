# Portfolio · Laia Orfila

Web portfolio de **Laia Orfila** (@una.laiacreativa), estrategia de contenido para marcas del sector hogar y cocinas de diseño.

Versión de prueba en desarrollo. Mantenimiento: José M. León.

## Estructura

```
index.html          Contenido de la página (textos en castellano)
aviso-legal.html    Aviso legal (borrador, faltan datos de Laia)
privacidad.html     Política de privacidad (borrador, faltan datos de Laia)
css/estilos.css     Diseño: colores, tipografías, maquetación y animaciones
js/idiomas.js       Traducciones al catalán e inglés (T) y textos del test (QZ)
js/main.js          Funcionamiento: idiomas, contadores, test, menú móvil y WhatsApp
img/                Imágenes en WebP (og.jpg en JPG para redes sociales)
sitemap.xml         Mapa del sitio para Google
.nojekyll           Indica a GitHub Pages que sirva los archivos tal cual
```

## Publicación

GitHub Pages: `https://josemaleon.github.io/portfolio-laia/`
Si se usa un dominio propio, cambiar la URL en `index.html` (canonical, og:url, og:image y JSON-LD) y en `sitemap.xml`.

## Cómo verla

Abrir `index.html` en el navegador. No necesita instalación ni compilación.

## Pruebas

`pruebas/test_web.py` revisa la web en escritorio y móvil (10 anchuras, 3 idiomas). Conviene ejecutarlo después de cada cambio:

```
pip install playwright && playwright install chromium
python pruebas/test_web.py
```

## Cómo editar

- **Textos en castellano**: directamente en el HTML.
- **Catalán e inglés**: en `js/idiomas.js`, objeto `T`. Cada texto tiene una clave igual a su atributo `data-i18n` en el HTML.
- **Test "¿Tu Instagram vende?"**: preguntas, consejos y resultados en `js/idiomas.js`, objeto `QZ` (tres idiomas).
- **Cifras con contador**: atributo `data-count` en el HTML y en las traducciones.
- **Colores**: variables al inicio de `css/estilos.css` (`--sea`, `--sand`, `--sun`).
- **Rutas de imágenes en el CSS**: empiezan por `../img/` porque el CSS está dentro de la carpeta `css/`.

## Pendiente

- [ ] Datos reales de resultados por cliente (Laia)
- [ ] Testimonios con nombre y cargo
- [ ] Fotos sin texto de Laia y fotos de proyectos reales, con permiso de cada cliente
- [ ] Paquetes de servicios y precios
- [ ] Revisión de textos en catalán e inglés por Laia
- [x] Imágenes en WebP con carga diferida
- [x] Borradores de aviso legal y privacidad, enlazados en el pie
- [ ] Completar los datos de Laia en `aviso-legal.html` y `privacidad.html` (marcados en amarillo) y revisarlos con un profesional
- [ ] Alojar las tipografías en la propia web y quitar el apartado de Google Fonts de la privacidad
- [x] Repositorio público y GitHub Pages activado: https://josemaleon.github.io/portfolio-laia/

## Derechos de las imágenes

Las fotos de clientes proceden de sus webs y perfiles públicos. Antes de publicar la web hay que confirmar el permiso de cada empresa.
