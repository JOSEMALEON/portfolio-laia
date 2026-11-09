/* Portfolio Laia Orfila · funcionamiento (necesita js/idiomas.js cargado antes) */

const nav=document.getElementById('nav');
addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>10),{passive:true});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.r').forEach(el=>io.observe(el));

/* Idiomas: aplica las traducciones de js/idiomas.js */
const els=[...document.querySelectorAll('[data-i18n]')], labs=[...document.querySelectorAll('[data-i18n-label]')];
T.es={title:document.title,photo:labs[0]&&labs[0].dataset.label};
els.forEach(e=>T.es[e.dataset.i18n]=e.innerHTML);
function setLang(l){
  const d=T[l]||T.es;
  els.forEach(e=>{const v=d[e.dataset.i18n]; if(v!=null) e.innerHTML=v;});
  labs.forEach(e=>e.dataset.label=d.photo);
  document.title=d.title; document.documentElement.lang=l; window.__onLang&&window.__onLang(l);
  document.querySelectorAll('.lang button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.lang===l));
  try{localStorage.setItem('lang',l)}catch(e){}
}
document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));
let saved; try{saved=localStorage.getItem('lang')}catch(e){}
const nl=(navigator.language||'es').slice(0,2).toLowerCase();
setLang(saved||(['es','ca','en'].includes(nl)?nl:'en'));
/* Contadores: suben de 0 al dato real al aparecer en pantalla */
const fmtN=n=>String(n).replace(/\B(?=(\d{3})+(?!\d))/g,document.documentElement.lang==='en'?',':'.');
const cio=new IntersectionObserver(es=>es.forEach(e=>{
  if(!e.isIntersecting) return; cio.unobserve(e.target);
  const el=e.target,end=+el.dataset.count,t0=performance.now(),d=1600;
  const step=t=>{const p=Math.min((t-t0)/d,1); el.textContent=fmtN(Math.round(end*(1-Math.pow(1-p,3)))); if(p<1&&el.isConnected) requestAnimationFrame(step);};
  requestAnimationFrame(step);
}),{threshold:.6});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches) document.querySelectorAll('[data-count]').forEach(el=>{el.textContent='0';cio.observe(el);});

/* Test "¿Tu Instagram vende?" (textos en js/idiomas.js → QZ) */
let qi=0,ans=[];
/* Saber si se usa teclado o pantalla táctil/ratón */
let usingKeyboard=false;
addEventListener('keydown',()=>{usingKeyboard=true;});
addEventListener('pointerdown',()=>{usingKeyboard=false;});
function qR(focus){
  const L=QZ[document.documentElement.lang]||QZ.es, el=document.getElementById('qz');
  if(qi<5){
    el.innerHTML=`<div class="qz-top"><span>${L.step} ${qi+1} ${L.of} 5</span><div class="qz-bar"><i style="width:${qi*20}%"></i></div></div><h3>${L.q[qi]}</h3><div class="qz-opts">${L.o.map((o,k)=>`<button type="button" data-v="${2-k}">${o}</button>`).join('')}</div>`;
    el.querySelectorAll('.qz-opts button').forEach(b=>b.addEventListener('click',()=>{ans[qi]=+b.dataset.v;qi++;qR(true);}));
  }else{
    const sc=ans.reduce((a,b)=>a+b,0), t=L.res[sc<=4?0:sc<=7?1:2], weak=ans.map((v,k)=>v<2?L.tips[k]:null).filter(Boolean);
    el.innerHTML=`<div class="qz-res"><div class="qz-score"><b>${sc}</b>/10<small>${L.score}</small></div><div><h3>${t[0]}</h3><p>${t[1]}</p></div></div><h4>${L.tipsT}</h4><ul class="qz-tips">${(weak.length?weak:[L.all]).map(x=>`<li>${x}</li>`).join('')}</ul><div class="cta-row"><a class="btn btn-dark" href="https://wa.link/pn85h8" target="_blank" rel="noopener">${L.cta}</a><button type="button" class="btn btn-ghost" id="qz-again">${L.again}</button></div>`;
    el.querySelector('#qz-again').addEventListener('click',()=>{qi=0;ans=[];qR(true);});
  }
  if(focus&&usingKeyboard){const f=el.querySelector('button,a'); f&&f.focus({preventScroll:true});}
}
window.__onLang=()=>qR(false); qR(false);

/* Menú móvil */
const mb=document.querySelector('.menu-btn'), mn=document.getElementById('mnav');
const mClose=()=>{mn.hidden=true;mb.setAttribute('aria-expanded','false');};
mb.addEventListener('click',()=>{const open=mn.hidden;mn.hidden=!open;mb.setAttribute('aria-expanded',String(open));});
mn.querySelectorAll('a').forEach(a=>a.addEventListener('click',mClose));
addEventListener('keydown',e=>{if(e.key==='Escape')mClose();});
document.addEventListener('click',e=>{if(!mn.hidden&&!e.target.closest('nav'))mClose();});

/* WhatsApp flotante: aparece al pasar la portada */
const wa=document.querySelector('.wa-float');
addEventListener('scroll',()=>wa.classList.toggle('show',scrollY>500),{passive:true});
