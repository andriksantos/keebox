import json,re,os
pages=json.load(open('pages.json')); bodies=json.load(open('bodies.json'))
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','docs','library'); os.makedirs(D,exist_ok=True)
def plain(s): return re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',s).replace('"','').strip()
for p in pages:
    desc=plain(p['desc']) or f"Curated {p['name']} resources."
    if not desc.endswith('.'): desc+='.'
    meta_desc=f"{p['n']:,} curated {p['name']} resources: {desc}"[:300]
    fm=['---',f'title: {json.dumps(p["name"]+" – Awesome List with "+format(p["n"],",")+" resources",ensure_ascii=False)}',
        f'description: {json.dumps(meta_desc,ensure_ascii=False)}','---','']
    head=[f'# {plain(p["name"])}','',desc,'',
      '!!! info "Source"',
      f'    {p["n"]:,} resources imported from [{p["repo"]}](https://github.com/{p["repo"]}), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **{p["cat"]}**.','']
    open(f'{D}/{p["slug"]}.md','w').write('\n'.join(fm+head)+bodies[p['slug']]+'\n')
# library index
from collections import defaultdict
by=defaultdict(list)
for p in pages: by[p['cat']].append(p)
tot=sum(p['n'] for p in pages)
L=['---','title: "KEEBOX Library – 444 Awesome Lists, 74,000+ Resources"',
   f'description: "The KEEBOX Library brings {len(pages)} public-domain awesome lists and {tot:,} developer resources into one searchable place, organized by category."','---','',
   '# KEEBOX Library','',
   f'**{len(pages)} awesome lists · {tot:,} resources · one place.** Every list below is dedicated to the public domain (CC0 or Unlicense) by its authors and imported here so you can browse and search everything without leaving KEEBOX. Each page credits its original repository.','',
   '!!! tip "How to use the Library"','    Use the search bar (press <kbd>/</kbd>) to find a list by name, or browse by category below. Lists that require attribution are linked from the [Credits](../credits.md) page; lists without an open license are not reproduced.','']
for cat in sorted(by):
    ps=sorted(by[cat],key=lambda p:p['name'].lower())
    L+=[f'## {cat}','',f'{len(ps)} lists · {sum(p["n"] for p in ps):,} resources','']
    L+=[f'- [{plain(p["name"])}]({p["slug"]}.md) · {p["n"]:,} — {plain(p["desc"]) or "Curated resources."}' for p in ps]+['']
open(f'{D}/index.md','w').write('\n'.join(L))
print('written',len(pages)+1)
