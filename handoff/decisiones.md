# Decisiones · CLI-0001

> Las referencias `references/stack.md`, `seguridad.md` y `flujo.md` de la skill **no estaban disponibles** en esta sesión. Se han aplicado criterios por defecto: menor coste total, menos dependencias, edición asumible y nada publicado sin aprobación.

## D1 · Stack preliminar (pendiente de confirmar)

| Opción | Coste anual aproximado* | Edición por Laia | Límites gratuitos | Encaje |
|---|---|---|---|---|
| **A. HTML/CSS/JS estático (actual) + GitHub Pages o Cloudflare Pages + dominio** | Solo el dominio | Mediante el técnico (archivos y git) | Pages: sitios públicos, límites de ancho de banda holgados para un portfolio | ✅ **Recomendada** |
| B. A + generador estático (Eleventy) y CMS basado en git (Decap o Pages CMS) | Solo el dominio | Laia puede editar textos y casos desde un panel | Igual que A | Si Laia quiere editar sola |
| C. Constructor alojado (Framer, Squarespace, Wix) | Cuota mensual de pago | Visual y sencilla | Los planes gratuitos muestran la marca del constructor y no permiten dominio propio | Más coste y dependencia; no necesaria |
| D. WordPress con hosting | Hosting + mantenimiento | Panel conocido | — | Sobredimensionado; requiere más mantenimiento y seguridad |

*Importes orientativos; confirmar precios vigentes antes de presupuestar. Correo: reenvío gratuito (p. ej. Cloudflare Email Routing) o un buzón de pago si necesita enviar desde el dominio.

**Motivo:** la web es una sola página con poco cambio de contenido, el código ya existe y pesa muy poco (~67 KB), y no hay presupuesto conocido. Pasar a B solo si Laia necesita editar sin ayuda.

## D2 · Idiomas en URLs propias

La traducción actual por JS solo permite indexar el castellano. Se propone generar `/ca/` y `/en/` como HTML estático con `hreflang`, a partir del mismo `idiomas.js`.

## D3 · Riesgos y acciones antes de producción

| Riesgo | Acción |
|---|---|
| **La demo ya es pública e indexable** y muestra fotos y marcas de clientes sin permiso confirmado (lo indica el propio README) | Añadir `noindex` ya. Conseguir el permiso escrito de cada empresa o sustituir las fotos por material de Laia o ficticio marcado como tal. Decide la persona responsable del repositorio. |
| Uso de la marca “Cucine Lube” en el menú y en una sección propia | Confirmar con Cucine Lube España que acepta el uso del nombre y del logotipo. |
| Google Fonts cargadas desde los servidores de Google (envío de IP; precedente LG München 2022) | Alojar las tipografías en la propia web (ya figura como pendiente en el README). |
| `wa.link` es un acortador de terceros | Usar un enlace directo `https://wa.me/<número>` (el número no se guarda en este traspaso). |
| Textos legales con datos del titular pendientes | Completarlos y revisarlos con un profesional antes de usar un dominio real. |
| Cifras fechadas en “nov. 2026” | Definir quién las actualiza y cada cuánto. |

## D4 · Publicación de la demo

En esta fase **no se ha publicado ni modificado nada**. La demo de GitHub Pages ya existía. No se ha hecho commit ni push al repositorio: los archivos de `handoff/` y `templates/` solo existen en la copia local de la sesión.
