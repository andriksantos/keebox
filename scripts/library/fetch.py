"""Step 1: download READMEs and license files for every list in lists.json.
If lists.json does not exist yet, it is created from awesome.md (the sindresorhus/awesome readme)."""
import re as _re, json as _json, os as _os
if not _os.path.exists('lists.json'):
    _t=open('awesome.md').read(); _t=_t[_t.index('## Platforms'):]
    _t=_t[:_t.index('## Related')] if '## Related' in _t else _t
    _cat=None; _out=[]; _parent=None
    for _line in _t.split('\n'):
        _m=_re.match(r'^## (.+)',_line)
        if _m: _cat=_m.group(1).strip(); _parent=None; continue
        _m=_re.match(r'^(\s*)- \[([^\]]+)\]\((https://github\.com/([^/]+/[^/#)]+))[^)]*\)\s*(?:-\s*(.*))?',_line)
        if _m:
            _ind=len(_m.group(1).replace('\t','  '))
            if _ind==0: _parent=_m.group(2)
            _out.append({'cat':_cat,'name':_m.group(2),'parent':None if _ind==0 else _parent,'repo':_m.group(4),'desc':(_m.group(5) or '').strip()})
    _json.dump(_out,open('lists.json','w'),indent=0)
import json,os,time,urllib.request,concurrent.futures as cf
L=json.load(open('lists.json'))
RN=['readme.md','README.md','Readme.md','README.markdown','readme.markdown','README.rst','README']
LN=['license','LICENSE','license.md','LICENSE.md','LICENSE.txt','license.txt','LICENCE','LICENCE.md','COPYING','UNLICENSE','LICENSE-CC0']
T0=time.time()
def get(repo,f):
    u=f'https://raw.githubusercontent.com/{repo}/HEAD/{f}'
    for t in range(3):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'keebox'}),timeout=20)
            return r.read().decode('utf-8','replace')
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            if e.code==429: time.sleep(10); continue
            return None
        except Exception: time.sleep(2)
    return None
def work(o):
    key=o['repo'].replace('/','__')
    p=f'raw/{key}.json'
    if os.path.exists(p) or time.time()-T0>150: return 0
    rd=None;rf=None
    for f in RN:
        rd=get(o['repo'],f)
        if rd: rf=f;break
    lic=None;lf=None
    for f in LN:
        lic=get(o['repo'],f)
        if lic: lf=f;break
    json.dump({'repo':o['repo'],'readme':rd,'readme_file':rf,'license':lic,'license_file':lf},open(p,'w'))
    return 1
with cf.ThreadPoolExecutor(12) as ex: n=sum(ex.map(work,L))
print('fetched',n,'total',len(os.listdir('raw')),'of',len(L))
