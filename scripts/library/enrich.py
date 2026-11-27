"""Add original context to every KEEBOX Library page.

Run after writelib.py (idempotent: re-running replaces the previous block).

For each docs/library/<slug>.md it inserts, right after the "Source" note:
  - "About this list": a hand-written introduction from intros.json when
    available, otherwise a summary built from the page's own data;
  - "What you'll find": the sections of the list with their link counts.
And at the end of the page:
  - "Related lists": internal links to other lists in the same category.

Why: Google reported many Library pages as "Crawled - currently not indexed"
because they only reproduced the upstream awesome list. This adds unique
text and internal links to every page.
"""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, '..', '..', 'docs', 'library'))
INTROS = json.load(open(os.path.join(HERE, 'intros.json'), encoding='utf-8'))
TOP_START, TOP_END = '<!-- kb-about:start -->', '<!-- kb-about:end -->'
BOT_START, BOT_END = '<!-- kb-related:start -->', '<!-- kb-related:end -->'


def strip_block(s, a, b):
    return re.sub(re.escape(a) + r'.*?' + re.escape(b) + r'\n*', '', s, flags=re.S)


def parse(path):
    s = open(path, encoding='utf-8').read()
    s = strip_block(strip_block(s, TOP_START, TOP_END), BOT_START, BOT_END).rstrip() + '\n'
    title = re.search(r'^# (.+)$', s, re.M)
    cat = re.search(r'Category: \*\*([^*]+)\*\*', s)
    desc = re.search(r'^description: "?\d[\d,]* curated .+? resources: (.+?)"?$', s, re.M)
    sections, cur = [], None
    for line in s.splitlines():
        m = re.match(r'^##\s+(.+)$', line)
        if m:
            cur = [re.sub(r'[^\w\s&/().,+#-]', '', m.group(1)).strip(), 0]
            sections.append(cur)
        elif cur and re.match(r'^\s*[-*] \[', line):
            cur[1] += 1
    return dict(
        text=s,
        title=title.group(1).strip() if title else os.path.basename(path)[:-3],
        cat=cat.group(1).strip() if cat else 'Miscellaneous',
        desc=desc.group(1).strip().rstrip('.') if desc else '',
        sections=[x for x in sections if x[1] > 0],
    )


def fallback_intro(p):
    t, d, secs = p['title'], p['desc'], p['sections']
    total = sum(n for _, n in secs)
    lead = f'**{t}**' + (f' — {d[0].lower() + d[1:]}.' if d and not d.lower().startswith('curated') else '.')
    biggest = sorted(secs, key=lambda x: -x[1])[:3]
    parts = [lead, f'This page brings together {total:,} links about {t}, grouped into {len(secs)} sections.']
    if biggest:
        names = ', '.join(f'**{n}**' for n, _ in biggest)
        parts.append(f'The largest sections are {names}, a good place to start if you are exploring the topic for the first time.')
    parts.append(f'It belongs to the **{p["cat"]}** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.')
    return ' '.join(parts)


def main():
    pages = {}
    for path in sorted(glob.glob(os.path.join(DOCS, '*.md'))):
        slug = os.path.basename(path)[:-3]
        if slug == 'index':
            continue
        pages[slug] = (path, parse(path))

    by_cat = {}
    for slug, (_, p) in pages.items():
        by_cat.setdefault(p['cat'], []).append(slug)

    for slug, (path, p) in pages.items():
        intro = INTROS.get(slug) or fallback_intro(p)
        secs = p['sections']
        about = [TOP_START, '', '## About this list', '', intro, '']
        if len(secs) > 1:
            about += ["### What you'll find", '']
            about += [f'- **{n}** — {c} link{"s" if c != 1 else ""}' for n, c in secs[:12]]
            if len(secs) > 12:
                about.append(f'- …and {len(secs) - 12} more sections')
            about.append('')
        about += [TOP_END, '', '']
        block = '\n'.join(about)

        s = p['text']
        # insert after the Source admonition (indented lines following it)
        m = re.search(r'!!! info "Source"\n(?:    .*\n)+', s)
        if m:
            s = s[:m.end()] + '\n' + block + s[m.end():].lstrip('\n')
        else:
            h = re.search(r'^# .+\n', s, re.M)
            s = s[:h.end()] + '\n' + block + s[h.end():]

        siblings = [x for x in by_cat[p['cat']] if x != slug]
        # stable, page-specific selection: neighbours alphabetically around the page
        allc = sorted(by_cat[p['cat']])
        i = allc.index(slug)
        ring = allc[i + 1:] + allc[:i]
        pick = ring[:8] if len(ring) <= 8 else ring[:4] + ring[-4:]
        rel = [BOT_START, '', '## Related lists', '',
               f'More lists in the **{p["cat"]}** category of the [KEEBOX Library](index.md):', '']
        rel += [f'- [{pages[x][1]["title"]}]({x}.md)' for x in pick if x in siblings]
        rel += ['', BOT_END, '']
        s = s.rstrip() + '\n\n' + '\n'.join(rel)
        open(path, 'w', encoding='utf-8').write(s)

    print(f'enriched {len(pages)} pages, {sum(1 for x in pages if x in INTROS)} with hand-written intros')


if __name__ == '__main__':
    main()
