#!/usr/bin/env python3
"""Standalone bilingual List introduction. Python standard library; no env reads."""
import argparse,html,json,re,shutil
from pathlib import Path
H=html.escape

def build(repo,out):
 cfg=json.loads((repo/'site/project.json').read_text());content=json.loads((repo/'site/content.json').read_text());out.mkdir(parents=True,exist_ok=True);media=out/'media';media.mkdir(exist_ok=True)
 for n in ['style.css','demo.js']:shutil.copy(repo/'site'/n,out/n)
 for src,name in [('docs/readme/banner.png','banner.png'),('docs/readme/assets/frankie.svg','signature.svg')]:shutil.copy(repo/src,media/name)
 for name in ['gallery-current.png','stack-current.png','marked-current.png','compare-current.png']:shutil.copy(repo/'site/assets'/name,media/name)
 # Fail if example items no longer match the real bundled collection.
 raw=(repo/'src/lib/workspace-constants.ts').read_text();source=json.loads('['+raw.split('export const DEFAULT_ITEMS = [',1)[1].split('];',1)[0].rstrip().rstrip(',')+']')
 for item in content['zh']['demo_items']:assert item in source,item
 (out/'.nojekyll').touch()
 for lang,c in content.items():
  zh=lang=='zh';pre='../' if zh else './';dest=out/'zh' if zh else out;dest.mkdir(exist_ok=True)
  articles=lambda xs:''.join('<article><h3>'+H(a)+'</h3><p>'+H(b)+'</p></article>' for a,b in xs)
  gallery=''.join(f'<figure><a href="{pre}media/{name}"><img src="{pre}media/{name}" alt="{H(cap,quote=True)}" loading="lazy" width="1468" height="1247"></a><figcaption>{H(cap)}</figcaption></figure>' for name,cap in zip(['gallery-current.png','stack-current.png','marked-current.png','compare-current.png'],c['captions']))
  rows=''.join(f'<tr><th scope="row">{H(t)}</th><td><input type="checkbox" data-owner="me" data-index="{i}" aria-label="{H(c["me"]+": "+t,quote=True)}" {"checked" if i in [0,1] else ""}></td><td><input type="checkbox" data-owner="them" data-index="{i}" aria-label="{H(c["them"]+": "+t,quote=True)}" {"checked" if i in [0,2] else ""}></td></tr>' for i,t in enumerate(c['demo_items']))
  data=json.dumps({'items':c['demo_items'],'labels':c['buckets']},ensure_ascii=False).replace('<','\\u003c')
  page=f'''<!doctype html><html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Frankie List | {'清单与分享快照' if zh else 'Notebooks and shared snapshots'}</title><meta name="description" content="{H(c['intro'],quote=True)}"><link rel="canonical" href="{cfg['pages_url']+('zh/' if zh else '')}"><link rel="alternate" hreflang="en" href="{cfg['pages_url']}"><link rel="alternate" hreflang="zh-CN" href="{cfg['pages_url']}zh/"><meta name="theme-color" content="#f1f2f4"><meta property="og:type" content="website"><meta property="og:title" content="Frankie List"><meta property="og:description" content="{H(c['intro'],quote=True)}"><meta property="og:url" content="{cfg['pages_url']+('zh/' if zh else '')}"><meta property="og:image" content="{cfg['pages_url']}media/banner.png"><link rel="stylesheet" href="{pre}style.css"></head><body><a class="skip" href="#main">{H(c['skip'])}</a><header class="shell"><a class="brand" href="{pre}"><img src="{pre}media/signature.svg" width="90" height="38" alt="Frankie"><strong>List</strong></a><nav aria-label="{'页面导航' if zh else 'Page navigation'}"><a href="#notebook">{c['nav'][0]}</a><a href="#use">{c['nav'][1]}</a><a href="#screens">{c['nav'][2]}</a><a href="#start">{c['nav'][3]}</a><a href="{pre}" lang="en" {'aria-current="page"' if not zh else ''}>EN</a><a href="{pre}zh/" lang="zh-CN" {'aria-current="page"' if zh else ''}>中文</a></nav></header>
<main id="main" class="shell"><section class="hero"><div><h1>{H(c['headline']).replace(chr(10),'<br>')}</h1><p class="lead">{H(c['intro'])}</p><a class="button" href="{cfg['app_url']}">{H(c['open'])} ↗</a></div><figure class="hero-screen"><img src="{pre}media/marked-current.png" alt="{H(c['captions'][2])}" width="1468" height="1247" fetchpriority="high"></figure></section>
<section class="section" id="notebook"><h2>{H(c['concept_title'])}</h2><p class="lead narrow">{H(c['concept'])}</p><div class="features">{articles(c['features'])}</div></section>
<section class="section"><h2>{H(c['compare_title'])}</h2><p class="lead narrow">{H(c['compare_intro'])}</p><div class="comparison-demo"><div class="paper"><table><thead><tr><th></th><th scope="col">{H(c['me'])}</th><th scope="col">{H(c['them'])}</th></tr></thead><tbody>{rows}</tbody></table><button type="button" id="reset">{H(c['reset'])}</button></div><div class="buckets" id="buckets" aria-live="polite"></div></div><p class="small">{H(c['demo_note'])}</p><div class="snapshot"><h3>{H(c['snapshot_title'])}</h3><p>{H(c['snapshot_body'])}</p></div></section>
<section class="section" id="use"><h2>{H(c['workflow_title'])}</h2><ol class="steps">{''.join('<li><h3>'+H(a)+'</h3><p>'+H(b)+'</p></li>' for a,b in c['steps'])}</ol></section>
<section class="section" id="screens"><h2>{H(c['gallery_title'])}</h2><div class="gallery">{gallery}</div></section>
<section class="section runtime" id="start"><div><h2>{H(c['storage_title'])}</h2><p>{H(c['storage'])}</p><details><summary>{'分享与本地加密的边界' if zh else 'Sharing and local encryption limits'}</summary><p>{H(c['security'])}</p></details></div><div><h3>{H(c['run'])}</h3><pre><code>npm ci\nnpm run dev</code></pre><p>{H(c['run_note'])}</p><a href="https://github.com/{cfg['repository']}/blob/main/site/GUIDE.md">{H(c['guide'])} ↗</a></div></section></main><footer class="shell"><span>{H(c['footer'])}</span><a href="https://github.com/{cfg['repository']}">{H(c['source'])} ↗</a></footer><script id="demo-data" type="application/json">{data}</script><script src="{pre}demo.js" defer></script></body></html>'''
  (dest/'index.html').write_text(page)
 print(out)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',default='_site');a=p.parse_args();build(Path(__file__).resolve().parents[1],Path(a.out).resolve())
