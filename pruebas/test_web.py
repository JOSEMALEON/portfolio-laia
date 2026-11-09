"""Batería de pruebas del portfolio (escritorio y móvil).

Uso:  pip install playwright && playwright install chromium
      python pruebas/test_web.py

Revisa: desbordamientos en 10 anchuras y 3 idiomas, errores de JavaScript, menú móvil,
anclas, traducciones, contadores, test (puntuación, teclado y botones en móvil),
efectos que se quedan fijos al tocar, páginas legales, imágenes y textos alternativos.

Incidencias conocidas y aceptadas:
- Textos pequeños dentro de la ilustración del móvil (caso Vielha): es una imagen con descripción propia.
- El botón de idioma cambia de aspecto al tocarlo: es el idioma seleccionado.
"""
import sys, json
from pathlib import Path
from playwright.sync_api import sync_playwright
BASE=Path(__file__).resolve().parent.parent.as_uri()+'/'
issues=[]
def bad(area,msg): issues.append(f'[{area}] {msg}')
NOANIM='*{transition:none!important;animation:none!important}.r{opacity:1!important;transform:none!important}'

with sync_playwright() as p:
    b=p.chromium.launch()
    def page(w,h=800,mobile=False):
        ctx=b.new_context(viewport={'width':w,'height':h},is_mobile=mobile,has_touch=mobile,device_scale_factor=2 if mobile else 1)
        pg=ctx.new_page(); pg._errs=[]
        pg.on('pageerror',lambda e:pg._errs.append('JS: '+str(e)))
        pg.on('console',lambda m:pg._errs.append('console: '+m.text) if m.type=='error' and 'fonts.g' not in m.text else None)
        pg.on('requestfailed',lambda r:pg._errs.append('fallo carga: '+r.url) if r.url.startswith('file:') else None)
        return pg

    # 1. Desbordamiento horizontal y errores, todas las anchuras e idiomas
    for w in [320,360,390,414,768,900,1024,1280,1440,1920]:
        for lang in ['es','ca','en']:
            pg=page(w,mobile=w<820); pg.goto(BASE+'index.html'); pg.click(f'button[data-lang="{lang}"]'); pg.add_style_tag(content=NOANIM)
            o=pg.evaluate("""()=>{const W=document.documentElement.clientWidth;const r=[];document.querySelectorAll('body *').forEach(e=>{const b=e.getBoundingClientRect();if(b.width&&b.right>W+1&&getComputedStyle(e).position!=='fixed'&&!e.closest('.mnav'))r.push((e.className||e.tagName)+':'+Math.round(b.right))});return [document.documentElement.scrollWidth>W,r.slice(0,4)]}""")
            if o[0] or o[1]: bad('desborde',f'{w}px {lang}: {o[1]}')
            nav=pg.evaluate("(()=>{const n=document.querySelector('nav .wrap');return n.scrollWidth>n.clientWidth})()")
            if nav: bad('menú',f'{w}px {lang}: la barra superior no cabe')
            for e in pg._errs: bad('errores',f'{w}px {lang}: {e}')
            pg.context.close()

    # 2. Móvil: botones con zona táctil pequeña, textos diminutos, botón WhatsApp tapando contenido
    pg=page(390,780,True); pg.goto(BASE+'index.html'); pg.add_style_tag(content=NOANIM)
    small=pg.evaluate("""()=>[...document.querySelectorAll('a,button')].filter(e=>e.offsetParent&&!e.closest('.mnav')).map(e=>{const b=e.getBoundingClientRect();return [(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,25),Math.round(b.width),Math.round(b.height)]}).filter(x=>x[1]<24||x[2]<24)""")
    for s in small: bad('móvil táctil',f'zona pequeña ({s[1]}×{s[2]} px): «{s[0]}»')
    tiny=pg.evaluate("""()=>{const r=new Set();document.querySelectorAll('body *').forEach(e=>{if(!e.offsetParent)return;const t=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());const f=parseFloat(getComputedStyle(e).fontSize);if(t&&f<12)r.add(Math.round(f*10)/10+'px «'+e.innerText.trim().slice(0,25)+'»')});return [...r].slice(0,8)}""")
    for t in tiny: bad('móvil texto',f'texto muy pequeño: {t}')
    pg.evaluate("scrollTo(0,document.body.scrollHeight)"); pg.mouse.wheel(0,10); pg.wait_for_timeout(300)
    ov=pg.evaluate("""()=>{const w=document.querySelector('.wa-float').getBoundingClientRect();return [...document.querySelectorAll('footer a, footer span')].filter(e=>{const b=e.getBoundingClientRect();return !(b.right<w.left||b.left>w.right||b.bottom<w.top||b.top>w.bottom)}).map(e=>e.innerText.slice(0,30))}""")
    if ov: bad('móvil WhatsApp',f'el botón flotante tapa el pie: {ov}')
    pg.context.close()

    # 3. Menú móvil
    pg=page(390,780,True); pg.goto(BASE+'index.html')
    pg.tap('.menu-btn'); pg.wait_for_timeout(200)
    if pg.evaluate("document.getElementById('mnav').hidden"): bad('menú móvil','no se abre')
    pg.mouse.click(200,700); pg.wait_for_timeout(200)
    if not pg.evaluate("document.getElementById('mnav').hidden"): bad('menú móvil','no se cierra al tocar fuera')
    pg.evaluate("document.getElementById('mnav').hidden=true")
    for h in pg.eval_on_selector_all('.mnav a','es=>es.map(e=>e.getAttribute("href"))'):
        pg.tap('.menu-btn'); pg.wait_for_timeout(150); pg.tap(f'.mnav a[href="{h}"]'); pg.wait_for_timeout(900)
        top=pg.evaluate(f"document.querySelector('{h}').getBoundingClientRect().top")
        if top<60 or top>200: bad('menú móvil',f'{h}: la sección queda en {round(top)} px (tapada o mal colocada)')
    pg.context.close()

    # 4. Enlaces del menú de escritorio y anclas
    pg=page(1280); pg.goto(BASE+'index.html')
    for h in pg.eval_on_selector_all('.links a:not(.btn)','es=>es.map(e=>e.getAttribute("href"))'):
        if not pg.query_selector(h): bad('anclas',f'{h} no existe'); continue
        pg.click(f'.links a[href="{h}"]'); pg.wait_for_timeout(900)
        top=pg.evaluate(f"document.querySelector('{h}').getBoundingClientRect().top")
        if top<60 or top>200: bad('anclas',f'{h}: la sección queda en {round(top)} px')
    pg.context.close()

    # 5. Idiomas: textos sin traducir
    pg=page(1280); pg.goto(BASE+'index.html'); pg.click('button[data-lang="es"]')
    es=pg.evaluate("[...document.querySelectorAll('[data-i18n]')].map(e=>[e.dataset.i18n,e.innerText.trim()])")
    for lang in ['ca','en']:
        pg.click(f'button[data-lang="{lang}"]')
        tr=dict(pg.evaluate("[...document.querySelectorAll('[data-i18n]')].map(e=>[e.dataset.i18n,e.innerText.trim()])"))
        same=[k for k,v in es if tr.get(k)==v and k not in('nav.c','nav.t','k1.ch','k2.r','k3.r','k1.r','meta2','meta3','meta1','cli','c.eye','sv2')]
        if same: bad('idiomas',f'{lang}: sin traducir {same}')
        if pg.evaluate("document.documentElement.lang")!=lang: bad('idiomas',f'lang del html no cambia a {lang}')
    pg.context.close()

    # 6. Contadores
    pg=page(1280); pg.goto(BASE+'index.html'); pg.click('button[data-lang="es"]')
    for el in pg.query_selector_all('[data-count]'): el.scroll_into_view_if_needed(); pg.wait_for_timeout(1900)
    for t,c in pg.evaluate("[...document.querySelectorAll('[data-count]')].map(e=>[e.textContent,e.dataset.count])"):
        if t.replace('.','')!=c: bad('contadores',f'muestra {t} en vez de {c}')
    pg.context.close()

    # 7. Test: puntuaciones, teclado y botón "pegado" en móvil
    for answers,exp in [(['Sí']*5,10),(['No']*5,0),(['Sí','A veces','No','Sí','A veces'],6)]:
        pg=page(1280); pg.goto(BASE+'index.html'); pg.click('button[data-lang="es"]')
        for a in answers: pg.click(f'.qz-opts button:has-text("{a}")')
        sc=int(pg.inner_text('.qz-score b'))
        if sc!=exp: bad('test',f'{answers} da {sc} y debería dar {exp}')
        pg.context.close()
    pg=page(1280); pg.goto(BASE+'index.html'); pg.click('button[data-lang="es"]')
    pg.focus('.qz-opts button'); 
    for _ in range(5): pg.keyboard.press('Enter'); pg.wait_for_timeout(80)
    if not pg.query_selector('.qz-score'): bad('test','no se puede completar con el teclado')
    pg.context.close()
    pg=page(390,780,True); pg.goto(BASE+'index.html'); pg.click('button[data-lang="es"]'); pg.add_style_tag(content='*{transition:none!important}')
    pg.locator('#qz').scroll_into_view_if_needed()
    for i in range(3):
        btn=pg.locator('.qz-opts button').nth(0); btn.tap(); pg.wait_for_timeout(150)
        st=pg.evaluate("(()=>{const b=document.querySelector('.qz-opts button');const s=getComputedStyle(b);return [s.backgroundColor, document.activeElement===b, b.matches(':hover'), b.matches(':focus-visible')]})()")
        if st[0]!='rgba(0, 0, 0, 0)' or st[1]: bad('test móvil',f'pregunta {i+2}: el botón aparece iluminado ({st[0]}; hover={st[2]}, foco visible={st[3]})'); break
    pg.context.close()

    # 8. Hover "pegado" en otros elementos al tocar (móvil)
    pg=page(390,780,True); pg.goto(BASE+'index.html'); pg.add_style_tag(content='*{transition:none!important}.r{opacity:1!important;transform:none!important}')
    for sel in ['.edu-card','.hero .btn-line','.lang button[data-lang="ca"]']:
        e=pg.locator(sel).first; e.scroll_into_view_if_needed(); before=pg.evaluate(f"[getComputedStyle(document.querySelector('{sel}')).backgroundColor,getComputedStyle(document.querySelector('{sel}')).transform].join()")
        pg.evaluate(f"document.querySelector('{sel}').addEventListener('click',e=>e.preventDefault(),{{once:true}})")
        e.tap(); pg.wait_for_timeout(150)
        after=pg.evaluate(f"[getComputedStyle(document.querySelector('{sel}')).backgroundColor,getComputedStyle(document.querySelector('{sel}')).transform].join()")
        hov=pg.evaluate(f"document.querySelector('{sel}').matches(':hover')")
        if after!=before: bad('móvil hover',f'{sel}: cambia de aspecto y se queda así tras tocarlo ({before} → {after})')
    pg.context.close()

    # 9. Páginas legales
    for pgname in ['aviso-legal.html','privacidad.html']:
        for w in [360,1280]:
            pg=page(w,mobile=w<820); pg.goto(BASE+pgname)
            if pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"): bad('legal',f'{pgname} {w}px desborda')
            for e in pg._errs: bad('legal',f'{pgname}: {e}')
            if not pg.query_selector('a.back[href="./"]'): bad('legal',f'{pgname}: falta enlace de volver')
            pg.context.close()

    # 10. Imágenes, alt y peso
    pg=page(1280); pg.goto(BASE+'index.html'); pg.add_style_tag(content=NOANIM)
    pg.evaluate("(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}})()"); pg.wait_for_timeout(2500)
    for s,ok,alt in pg.evaluate("[...document.images].map(i=>[i.src.split('/').pop(),i.complete&&i.naturalWidth>0,i.alt])"):
        if not ok: bad('imágenes',f'{s} no carga')
        if not alt: bad('imágenes',f'{s} sin texto alternativo')
    pg.context.close()
    b.close()

pg=None
print('\n'.join(issues) if issues else 'SIN FALLOS')
print(f'\nTotal: {len(issues)} incidencias')
