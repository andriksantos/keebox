import json,re,os,sys
SKIP=re.compile(r'^(contents|table of contents|index|contributing|contribute|contributors|contribution|license|licence|footnotes|related( lists)?|credits|acknowledg|sponsors?|backers?|support|code of conduct|how to contribute|maintainers?|toc|navigation)\b',re.I)
def absurl(u,repo):
    u=u.strip()
    if u.startswith(('http://','https://','mailto:')): return u
    if u.startswith('#'): return None
    if u.startswith('//'): return 'https:'+u
    u=u.lstrip('./')
    return f'https://github.com/{repo}/blob/HEAD/{u}'
def clean_inline(s,repo):
    s=re.sub(r'<img[^>]*>','',s,flags=re.I)
    s=re.sub(r'!\[[^\]]*\]\([^)]*\)','',s)                     # images/badges
    s=re.sub(r'\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)','',s)        # linked badges
    s=re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',lambda m:f'[{m.group(2)}]({m.group(1)})',s,flags=re.I)
    s=re.sub(r'<[^>]+>','',s)
    def fix(m):
        u=absurl(m.group(2),repo)
        return f'[{m.group(1)}]({u})' if u else m.group(1)
    s=re.sub(r'\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)',fix,s)
    s=s.replace('{{','{ {').replace('{%','{ %')
    return s.rstrip()
def convert(md,repo):
    md=re.sub(r'<!--.*?-->','',md,flags=re.S)
    md=re.sub(r'```.*?```','',md,flags=re.S)
    lines=md.split('\n'); out=[]; skipping=False; skip_level=0; seen_h=False; n=0
    for line in lines:
        h=re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$',line)
        if h:
            lvl=len(h.group(1)); title=clean_inline(h.group(2),repo)
            title=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',title).strip()
            if lvl==1: continue
            if skipping and lvl>skip_level: continue
            skipping=False
            if SKIP.match(re.sub(r'^[^\w]+','',title)): skipping=True; skip_level=lvl; continue
            if not title: continue
            lvl=max(2,min(lvl,4)); out.append(''); out.append('#'*lvl+' '+title); out.append(''); seen_h=True; continue
        if skipping or not seen_h: continue
        m=re.match(r'^(\s*)[-*+]\s+(.*)',line)
        if m and '](' in m.group(2):
            ind=len(m.group(1).replace('\t','    ')); depth=min(ind//2,3)
            item=clean_inline(m.group(2),repo)
            if not re.search(r'\]\((https?://|mailto:)',item): continue
            out.append('    '*depth+'- '+item); n+=1
    # drop headings with nothing under them
    res=[];
    for i,l in enumerate(out):
        if l.startswith('#'):
            nxt=[x for x in out[i+1:] if x.strip()]
            if not nxt or (nxt[0].startswith('#') and len(nxt[0].split(' ')[0])<=len(l.split(' ')[0])): continue
        res.append(l)
    txt='\n'.join(res); txt=re.sub(r'\n{3,}','\n\n',txt)
    return txt.strip(),n
if __name__=='__main__':
    repo=sys.argv[1]; d=json.load(open('raw/'+repo.replace('/','__')+'.json'))
    t,n=convert(d['readme'] or '',repo); print(n); print(t[:2500])
