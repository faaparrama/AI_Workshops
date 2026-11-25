"""Side menu for the self-guided workshop pages (w1 to w4).

add(html) turns the page's <ol class="toc"> into a side menu:
wide screens: a fixed column on the left; phones and zoomed pages: a bar at the top that opens a list.
The menu is built from the page's own table of contents, so the section names live in one place.
"""
import re

CSS = """
.skip{position:absolute;left:-999px;top:0;background:var(--ground);color:var(--maroon);padding:.5em 1em;z-index:30}
.skip:focus{left:8px;top:8px;outline:3px solid var(--maroon)}
main:focus{outline:none}
.footer a{overflow-wrap:anywhere}
.sidenav ol{list-style:none;margin:0;padding:0}
.sidenav a{display:flex;gap:.55em;align-items:baseline;padding:.42em .7em;border-left:4px solid transparent;color:var(--ink);text-decoration:none;line-height:1.3;font-size:.9rem}
.sidenav a:hover{text-decoration:underline}
.sidenav a .n{flex:none;min-width:1.3em;text-align:right;font-variant-numeric:tabular-nums}
.sidenav a .nm{flex:1;overflow-wrap:break-word}
.sidenav a .m{flex:none;color:var(--muted);font-size:.85em;white-space:nowrap}
.sidenav a[aria-current]{border-left-color:var(--maroon);background:var(--maroon-soft);font-weight:700}
.sidenav a:focus-visible{outline:3px solid var(--maroon);outline-offset:-3px}
.sidenav .title{font-weight:700;color:var(--maroon);margin:0 0 .5rem;padding:0 .7em;font-size:.95rem}
:root .sidenav button.ghost{display:none}
@media (min-width:68rem){
  .sidenav{position:fixed;left:0;top:0;bottom:0;width:16.5rem;overflow-y:auto;padding:1.5rem .6rem 2rem;border-right:1px solid var(--rule);background:var(--surface);z-index:10}
  body{margin-left:max(17rem,calc((100vw - 44rem)/2));margin-right:auto}
}
@media (max-width:67.99rem){
  main h2,main a,main button,main input,main textarea,main select,main summary{scroll-margin-top:4rem}
  .sidenav{margin:0 0 1rem}
  .sidenav .title{padding:0}
  .js .sidenav{position:sticky;top:0;z-index:20;margin:-1.5rem -16px 1rem;background:var(--ground);border-bottom:1px solid var(--rule-strong)}
  .js .sidenav .title{display:none}
  :root.js .sidenav button.ghost{display:flex;width:100%;justify-content:space-between;align-items:center;gap:1em;border:0;border-radius:0;padding:.65em 16px;min-height:2.75rem;text-align:left;background:var(--ground);color:var(--maroon)}
  .js .sidenav button .cur{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .js .sidenav button .cue{flex:none;font-weight:400}
  .js .sidenav ol{display:none;position:absolute;left:0;right:0;top:100%;max-height:70vh;overflow-y:auto;background:var(--ground);border-top:1px solid var(--rule);border-bottom:2px solid var(--maroon);padding:.4rem 0}
  .js .sidenav.open ol{display:block}
  .sidenav a{min-height:2.75rem;align-items:center}
}
@media print{.sidenav,.skip{display:none!important}body{margin:0 auto!important}}
"""

JS = """<script>
(function(){
  var nav=document.getElementById('sidenav'), btn=document.getElementById('navBtn');
  if(!nav||!btn) return;
  document.documentElement.classList.add('js');
  var links=Array.prototype.slice.call(nav.querySelectorAll('a')), cur=btn.querySelector('.cur'), cue=btn.querySelector('.cue');
  var heads=links.map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); });
  function setOpen(o){ nav.classList.toggle('open',o); btn.setAttribute('aria-expanded',String(o)); cue.textContent=o?'Close':'Sections'; }
  function mark(){
    var k=-1, line=window.innerHeight*0.3;
    heads.forEach(function(h,i){ if(h && h.getBoundingClientRect().top<=line) k=i; });
    if(window.innerHeight+window.scrollY>=document.documentElement.scrollHeight-4) k=links.length-1;
    links.forEach(function(a,i){ if(i===k) a.setAttribute('aria-current','location'); else a.removeAttribute('aria-current'); });
    cur.textContent = k<0 ? 'Start of the workshop' : links[k].querySelector('.n').textContent+' of '+links.length+': '+links[k].querySelector('.nm').textContent;
    var a=links[k]; if(a && nav.scrollHeight>nav.clientHeight+4 && getComputedStyle(nav).position==='fixed'){
      var r=a.getBoundingClientRect(); if(r.top<0||r.bottom>window.innerHeight) nav.scrollTop+=r.top-window.innerHeight/2; }
  }
  var wait=false;
  function later(){ if(wait) return; wait=true; requestAnimationFrame(function(){ wait=false; mark(); }); }
  btn.addEventListener('click',function(){ setOpen(!nav.classList.contains('open')); });
  nav.addEventListener('keydown',function(e){ if(e.key==='Escape' && nav.classList.contains('open')){ setOpen(false); btn.focus(); } });
  document.addEventListener('click',function(e){ if(!nav.contains(e.target)) setOpen(false); });
  links.forEach(function(a,i){ a.addEventListener('click',function(){ setOpen(false); var h=heads[i]; if(h){ h.setAttribute('tabindex','-1'); setTimeout(function(){ h.focus({preventScroll:true}); },0); } }); });
  window.addEventListener('scroll',later,{passive:true}); window.addEventListener('resize',later);
  setOpen(false); mark();
})();
</script>
"""


def add(html):
    toc = re.search(r'<ol class="toc">(.*?)</ol>\n*', html, re.S)
    items = re.findall(r'<a href="#([\w-]+)">(.*?)</a>\s*<span class="status">(.*?)</span>', toc.group(1), re.S)
    heads = re.findall(r'<h2 id="([\w-]+)"', html)
    assert [i[0] for i in items] == heads, "the table of contents and the section headings do not match"
    lis = "\n".join(
        f'    <li><a href="#{i}"><span class="n">{n}</span><span class="nm">{name}</span><span class="m">{mins}</span></a></li>'
        for n, (i, name, mins) in enumerate(items, 1))
    nav = ('<a class="skip" href="#content">Skip to the workshop</a>\n'
           '<nav class="sidenav" id="sidenav" aria-label="Sections of this workshop">\n'
           '  <p class="title">Sections</p>\n'
           '  <button type="button" class="ghost" id="navBtn" aria-expanded="false" aria-controls="navList">'
           '<span class="cur">Start of the workshop</span> <span class="cue">Sections</span></button>\n'
           f'  <ol id="navList" role="list">\n{lis}\n  </ol>\n</nav>\n<main id="content" tabindex="-1">\n')
    html = html.replace(toc.group(0), "", 1)
    html = html.replace("<body>\n", "<body>\n" + nav, 1)
    html = html.replace("</footer>", "</footer>\n</main>", 1)
    i = html.rindex("</style>", 0, html.index("<body>"))
    html = html[:i] + CSS + ":root h2:focus{outline:none}\n" + html[i:]
    return html.replace("</body>", JS + "</body>", 1)
