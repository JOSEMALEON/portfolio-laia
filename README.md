# Portfolio · Laia Orfila

Web portfolio de **Laia Orfila** (@una.laiacreativa), estrategia de contenido para marcas del sector hogar y cocinas de diseño.

Versión de prueba en desarrollo. Mantenimiento: José M. León.

## Estructura

```
index.html        Página completa: contenido, estilos y scripts
img/
  laia.jpg            Foto de portada (reconstruida sin texto a partir de su presentación en Instagram)
  laia-hola.jpg       Foto "Hola :)" de la sección Sobre mí
  caso-menorca-hd.jpg Imagen del caso Ambients Menorca (catálogo Cucine Lube, web de Ambients)
  caso-malaga-hd.jpg  Imagen del caso Lube Cocinas Málaga (showroom, web de Lube Málaga)
  vielha-reel.jpg     Portada de reel usada en el visual del caso Vielha
  og.jpg              Imagen de vista previa al compartir el enlace
```

## Cómo verla

Abrir `index.html` en el navegador. No necesita instalación ni compilación.

## Cómo editar

- **Textos en castellano**: directamente en el HTML.
- **Catalán e inglés**: en el objeto `const T={ca:{…},en:{…}}` al final de `index.html`. Cada texto tiene una clave igual a su atributo `data-i18n`.
- **Test "¿Tu Instagram vende?"**: preguntas, consejos y resultados en `const QZ` (tres idiomas).
- **Cifras con contador**: atributo `data-count` en el HTML y en las traducciones.
- **Colores**: variables al inicio del CSS (`--sea`, `--sand`, `--sun`).

## Pendiente

- [ ] Datos reales de resultados por cliente (Laia)
- [ ] Testimonios con nombre y cargo
- [ ] Fotos sin texto de Laia y fotos de proyectos reales, con permiso de cada cliente
- [ ] Paquetes de servicios y precios
- [ ] Revisión de textos en catalán e inglés por Laia
- [ ] Antes de publicar: aviso legal y privacidad, tipografías alojadas localmente, imágenes en WebP
- [ ] Al publicar: cambiar `og:image` por la URL absoluta

## Derechos de las imágenes

Las fotos de clientes proceden de sus webs y perfiles públicos. Antes de publicar la web hay que confirmar el permiso de cada empresa.
