import json,glob,re
L={o['repo']:o for o in json.load(open('lists.json'))}
def detect(text):
    if not text: return None
    t=text.lower()
    # restrictive first
    if re.search(r'attribution-noncommercial|attribution-noderivatives|attribution-noncommercial-|by-nc|by-nd|noncommercial[- ]\d|noncommercial-sharealike|noncommercial-noderivatives|\(cc by-nc|\(cc by-nd',t): return 'restrictive'
    if 'cc0' in t or 'creative commons legal code\n\ncc0' in t or 'to the extent possible under law' in t or 'public domain dedication' in t: return 'public-domain'
    if 'this is free and unencumbered software released into the public domain' in t or 'unlicense' in t: return 'public-domain'
    if re.search(r'attribution-sharealike|cc by-sa|by-sa ?[34]\.0|sharealike',t): return 'cc-by-sa'
    if re.search(r'creative commons attribution|cc by ?[34]\.0|cc-by|licenses/by/',t): return 'cc-by'
    if 'mit license' in t or 'permission is hereby granted, free of charge' in t: return 'mit'
    if 'apache license' in t: return 'apache-2.0'
    if 'gnu general public license' in t or 'gnu affero' in t: return 'gpl'
    if 'gnu free documentation license' in t: return 'gfdl'
    if 'redistribution and use in source and binary forms' in t: return 'bsd'
    if 'mozilla public license' in t: return 'mpl'
    if 'permission to use, copy, modify, and/or distribute' in t: return 'isc'
    if 'do what the fuck you want' in t: return 'wtfpl'
    if 'zero public license' in t: return '0pl'
    if 'do what you want to' in t: return 'dwyw'
    if 'artistic license' in t: return 'artistic-2.0'
    if 'gnu free documentation' in t: return 'gfdl'
    if 'has dedicated the work to the public domain' in t: return 'public-domain'
    if re.search(r'attribution 3\.0|attribution 4\.0',t): return 'cc-by'
    return 'unknown'
res=[]
for f in glob.glob('raw/*.json'):
    d=json.load(open(f)); lic=detect(d['license']); src='license-file'
    if lic in (None,'unknown') and d['readme']:
        rd=d['readme']; m=re.search(r'#+\s*licen[sc]e[^\n]*\n(.{0,1500})',rd,re.I|re.S)
        sec=m.group(1) if m else ''
        # badges anywhere mentioning cc0
        badge=' '.join(re.findall(r'!\[[^\]]*\]\([^)]*(?:cc0|publicdomain|licenses/by|by-sa|by-nc)[^)]*\)',rd,re.I))
        l2=detect(sec+' '+badge) if (sec or badge) else None
        if l2 and l2!='unknown': lic,src=l2,'readme'
    if lic is None: lic='none'
    group={'public-domain':'import','restrictive':'exclude','none':'exclude','unknown':'review'}.get(lic,'credits')
    res.append({**L[d['repo']],'license':lic,'license_source':src,'group':group,'has_readme':bool(d['readme'])})
json.dump(res,open('classified.json','w'),indent=0)
from collections import Counter
print(Counter(r['license'] for r in res)); print(Counter(r['group'] for r in res))
for r in [r for r in res if r['group']=='review'][:15]: print('REVIEW',r['repo'])
