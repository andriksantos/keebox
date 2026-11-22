import json,re
from convert import convert
res=json.load(open('classified.json'))
imp=[r for r in res if r['group']=='import' and r['has_readme']]
def slug(s): return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',s.lower())).strip('-') or 'list'
used=set(); pages=[]; total=0; empty=[]
for r in sorted(imp,key=lambda x:(x['cat'],x['name'].lower())):
    d=json.load(open('raw/'+r['repo'].replace('/','__')+'.json'))
    body,n=convert(d['readme'],r['repo'])
    if n<3: empty.append(r['repo']); continue
    s=slug(r['name']); base=s; i=2
    while s in used: s=f'{base}-{i}'; i+=1
    used.add(s)
    pages.append({**r,'slug':s,'n':n,'body':body}); total+=n
json.dump([{k:v for k,v in p.items() if k!='body'} for p in pages],open('pages.json','w'),indent=0)
json.dump({p['slug']:p['body'] for p in pages},open('bodies.json','w'))
print('pages',len(pages),'links',total,'skipped (<3 links / no content)',len(empty))
from collections import Counter
print(Counter(p['cat'] for p in pages).most_common(5))
print(sorted(pages,key=lambda p:-p['n'])[:5] and [(p['name'],p['n']) for p in sorted(pages,key=lambda p:-p['n'])[:8]])
