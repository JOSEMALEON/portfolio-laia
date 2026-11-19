# SEO · CLI-0001

No se prometen posiciones. **Sin herramienta de palabras clave en esta sesión**: la intención de búsqueda y los clústeres se basan en criterio, no en volúmenes medidos. Hay que validarlos con Search Console (cuando haya dominio) o con un planificador de palabras clave.

## 1. Intenciones y clústeres

| Clúster | Intención | Ejemplos de consulta (ES / CA / EN) | Página destino |
|---|---|---|---|
| Servicio en el nicho | Comercial | estrategia de contenido para tiendas de cocinas · marketing en redes para showroom de cocinas · gestión de Instagram para estudio de cocinas | `/` |
| Red Lube | Comercial / marca | marketing para distribuidores Cucine Lube · redes sociales Lube cocinas | `/#red` → futura `/red-lube/` |
| Local | Comercial local | community manager Menorca · estratègia de contingut Menorca · social media manager Menorca | `/` + `/ca/` |
| Prueba / casos | Investigación | caso de éxito Instagram cocinas · reels para tienda de cocinas ejemplos | `/casos/*` |
| Educativo | Informacional | ideas de reels para tienda de cocinas · jobs to be done marketing · errores al reformar la cocina | `/aprende/*` (fase 2) |
| Internacional | Comercial | social media for kitchen showrooms Spain | `/en/` |

## 2. Estructura de URL propuesta

Fase 1 (lanzamiento, mínima):
```
/                     ES (portfolio de una página)
/ca/                  CA (HTML estático, no traducido por JS)
/en/                  EN
/aviso-legal/
/privacidad/
```
Fase 2 (cuando haya permisos y datos):
```
/casos/ambients-menorca/
/casos/cucine-lube-vielha/
/casos/lube-cocinas-malaga/
/test/                (autodiagnóstico con URL propia, compartible)
/aprende/<articulo>/
```
Cada página por idioma enlaza a sus equivalentes con `hreflang` (es, ca, en, x-default → es).

## 3. Títulos, descripciones y H1

| URL | `<title>` (≤ 60 caracteres) | Meta description (≤ 155) | H1 |
|---|---|---|---|
| `/` | Estrategia de contenido para marcas de cocina · Laia Orfila | Contenido en redes que lleva clientes al showroom. Estrategia, reels y gestión de Instagram para estudios y distribuidores de cocina. | Contenido que convierte seguidores en clientes para marcas de cocina. *(actual, se mantiene)* |
| `/ca/` | Estratègia de contingut per a marques de cuina · Laia Orfila | Contingut a les xarxes que porta clients al showroom. Estratègia, reels i Instagram per a estudis i distribuïdors de cuina. | (traducción revisada por Laia) |
| `/en/` | Content strategy for kitchen brands · Laia Orfila | Social content that brings buyers into the showroom. Strategy, reels and Instagram for kitchen studios and retailers in Spain. | (traducción revisada) |
| `/casos/ambients-menorca/` | Caso Ambients Menorca: Instagram para cocinas de diseño | Cómo convertimos seguidores curiosos en clientes de cocina de diseño en Menorca: estrategia, formatos y resultados. | Ambients Menorca: de seguidores curiosos a clientes |

**Cambio respecto a la demo:** el título actual empieza por el nombre propio. Se propone poner primero el servicio, porque el nombre todavía no se busca.

## 4. Jerarquía H2 (portada, ya correcta en la demo)

H1 propuesta → H2 Método → H2 Casos (H3 por distribuidor) → H2 Red Lube → H2 Servicios (H3 ×6) → H2 Aprende → H2 Sobre mí → H2 Test → H2 Contacto. Hay un solo H1 por idioma ✔.

## 5. Enlaces internos

- Cada servicio enlaza al caso que lo demuestra (Campañas → Málaga; Serie educativa → Vielha; Captación → Menorca).
- Cada caso termina con su llamada a la acción y un enlace a “otros casos”.
- El resultado del test enlaza al servicio recomendado.
- El pie enlaza a los idiomas y a las páginas legales.

## 6. Texto alternativo

Ya existe en todas las imágenes ✔. Regla: describir la escena y el proyecto (“Cocina Lube con isla en blanco mate, proyecto de Ambients Menorca”), no repetir palabras clave.

## 7. SEO local

- Perfil de empresa en Google: **solo si Laia acepta mostrar la zona sin dirección exacta** (negocio de servicio a domicilio o en remoto, ocultando la dirección).
- Nombre y zona coherentes entre la web, Instagram y el perfil de Google.

## 8. Datos estructurados

- Se mantiene `ProfessionalService`, con `founder` de tipo `Person`, `areaServed`, `knowsLanguage` y `sameAs`. **Hay que actualizar `url` e `image` al dominio definitivo.**
- Se añade `Person` (`jobTitle`, `sameAs`) en `/` y `/ca/` y `/en/` con `inLanguage`.
- En los casos: `CreativeWork` o `Article` con `about` y `dateModified`.
- **No usar** `Review` ni `AggregateRating` hasta tener reseñas reales y verificables.
- Validar con Rich Results Test y validator.schema.org antes de publicar.

## 9. Buscadores con IA

- Escribir cada caso con hechos comprobables (fecha, cuenta y métrica, “Instagram · nov. 2026”), como ya hace la demo ✔.
- Publicar el método en texto HTML, no solo en imágenes o en reels.
- Usar contenido propio (las preguntas reales de los comentarios son material original y valioso).
- Hacer el contenido accesible sin JS: por eso se separan los idiomas en HTML estático.

## 10. Técnico antes del lanzamiento

- Demo: `<meta name="robots" content="noindex">` hasta la aprobación.
- Producción: `canonical`, `og:url`, `sitemap.xml` y JSON-LD con el dominio definitivo; `robots.txt` con referencia al sitemap.
- Alta en Google Search Console y Bing Webmaster Tools.
