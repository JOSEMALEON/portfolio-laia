# Investigación · CLI-0001

Fecha de consulta: 2026-11-19. Fuente del brief: repositorio `josemaleon/portfolio-laia` (commit `23c5200`, 2026-11-09). La URL publicada no se pudo abrir desde esta sesión, así que se analizó el código del repositorio.

## 1. Brief del proyecto

| Campo | Dato | Origen |
|---|---|---|
| Nombre comercial | Laia Orfila · Estrategia de contenido (@una.laiacreativa) | README / index |
| Actividad | Estrategia de contenido, guiones y reels, gestión de Instagram, campañas, captación y consultoría | index |
| Nicho | Estudios de cocina, distribuidores (sobre todo la red Cucine Lube) y marcas del hogar | index |
| Zona / idiomas | Menorca, en remoto para toda España · ES / CA / EN | index |
| Conversión | WhatsApp, mensaje directo de Instagram, test de 5 preguntas, recurso “ECO” | index |
| Dominio / hosting | Solo GitHub Pages; no hay dominio propio | README |
| Correo | No figura (marcado como pendiente en el HTML) | index |
| Presupuesto, plazo, aprobación | **Desconocidos** | — |
| Redes | Instagram @una.laiacreativa | index |

## 2. Referentes del sector

**Limitación importante:** la red de esta sesión solo permitía usar el buscador. Las webs de los referentes no se pudieron abrir, así que **no se observaron directamente su UX, navegación, versión móvil ni velocidad**. Lo que sigue procede de los fragmentos que devuelve el buscador y se separa en lo observado y lo inferido. Para completar la comparación hay que permitir esos dominios en la red de la sesión o revisarlos a mano con PageSpeed Insights.

| # | Referente | Tipo | Observado (fragmento del buscador) | Inferencia (no verificada) |
|---|---|---|---|---|
| 1 | [Adtrak · Kitchens & Bathrooms](https://www.adtrak.co.uk/sectors/digital-marketing-kitchens-bathrooms) | Agencia del Reino Unido con página por sector | Página dedicada al sector cocinas y baños; muestra una cifra de caso muy llamativa (+20.236 % de interacción en Facebook) | La página por sector capta búsquedas del tipo “marketing para cocinas”. Una cifra tan extrema sin contexto resta credibilidad. |
| 2 | [Profitworks · Kitchen cabinet stores](https://www.profitworks.ca/industries/kitchen-cabinets-marketing.html) | Agencia canadiense con página por sector | Promete “leads” de calidad y visitas al showroom con Google Ads y redes sociales; se dirige a propietarios que buscan cocinas | El mensaje se centra en visitas al showroom, como el de Laia: confirma que es el beneficio que importa en el sector. |
| 3 | [kbbreview · “KBB social media marketing isn’t dead”](https://www.kbbreview.com/?p=79228) | Columna de opinión en una revista del sector | Defiende combinar publicidad pagada y contenido orgánico para los showrooms | Escribir como experta en medios del sector refuerza la autoridad; aplicable con revistas españolas del sector. |
| 4 | [KBB Focus · PR para tiendas de cocinas](https://kbbfocus.com/news/6240-why-hiring-a-professional-pr-can-help-grow-your-kitchen-retail-business) | Artículo del sector | Señala que muchas tiendas publican en redes de forma esporádica y que las redes sirven para enseñar proyectos, trastienda y lanzamientos | El dolor “publico poco y sin estrategia” es común: es un buen gancho para el test. |
| 5 | Perfiles en marketplaces ([Malt](https://www.malt.es/profile/carolinacalvo), [Behance](https://www.behance.net/creativeen/resume)) | Freelances de redes e interiorismo | Portfolios genéricos; ninguno especializado en cocinas en España | En la búsqueda no aparece ningún competidor directo especializado en cocinas en España. |

### Conclusiones

- **Nicho poco ocupado en España.** Las búsquedas en español no devolvieron agencias ni freelances especializados en estudios de cocina; los referentes especializados son anglosajones (el sector KBB). *Es una inferencia a partir de pocas búsquedas, no un estudio de mercado.*
- Los referentes especializados usan **páginas por sector o por caso** y **cifras de resultado**. La demo de Laia ya muestra cifras, pero en una sola página.
- Ningún referente analizado ofrece un **autodiagnóstico interactivo**: es un elemento diferencial de la demo.

## 3. Auditoría de la demo actual (prueba local con Playwright y Chromium, 2026-11-19)

| Comprobación | Resultado |
|---|---|
| Desbordamiento horizontal a 360 / 390 / 768 / 1280 / 1920 px | Ninguno |
| Errores de JS y recursos locales que no cargan | Ninguno |
| Teclado: enlace “Saltar al contenido” y foco visible en la navegación, los idiomas y las llamadas a la acción | Correcto |
| Anclas internas que no existen | 0 |
| Imágenes sin `alt` | 0 |
| Peso propio | HTML+CSS+JS ≈ 67 KB; imágenes ≈ 220 KB en WebP (más `og.jpg` de 72 KB) |
| Dependencias externas | Google Fonts (privacidad: ver `decisiones.md`), wa.link, Instagram |
| Detección del idioma | Elige el idioma según el navegador (un navegador en inglés la muestra en EN) |
| `robots` / `noindex` | **No hay**: la demo es indexable |
| `hreflang` / URLs por idioma | **No hay**: CA y EN existen solo en JS |
| Lighthouse / PageSpeed | **No se ejecutó** (no hay acceso a la API desde esta sesión). Pendiente. |

## 4. Recorridos de usuario

1. **Distribuidor de Lube que llega desde Instagram.** Inicio → “Red Lube” → caso de su zona → WhatsApp “Hablemos”.
2. **Estudio independiente que busca en Google.** Inicio → Método → Casos → Test → resultado con recomendación → WhatsApp.
3. **Marca curiosa sin urgencia.** Aprende → reel / recurso ECO → seguir en Instagram (conversión blanda).
4. **Cliente internacional de la Costa del Sol (EN).** Inicio en EN → caso de Málaga (bilingüe) → WhatsApp.

## 5. Inventario de contenido

| Contenido | Estado |
|---|---|
| Textos ES | Listos (demo) |
| Textos CA / EN | Traducidos; falta la revisión de Laia |
| Fotos de Laia | Hay 2; el README pide versiones sin texto |
| Fotos de proyectos de clientes | Sacadas de webs y perfiles públicos: **sin permiso confirmado** |
| Cifras por caso | Hay seguidores y me gusta; faltan resultados de negocio (consultas, visitas) |
| Testimonios | Faltan |
| Paquetes y precios | Faltan |
| Correo de contacto | Falta |
| Aviso legal / privacidad | Borradores; faltan los datos del titular y la revisión profesional |
