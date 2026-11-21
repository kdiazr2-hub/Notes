"""Generate area indexes and session notes from curriculum/*.txt.

Usage: python -I build.py <scratchpad> <vault_dir> [--write]
Without --write it only validates and prints a report.
"""
import os, re, sys, glob
sys.stdout.reconfigure(encoding='utf-8')

SCR, VAULT = sys.argv[1], sys.argv[2]
WRITE = '--write' in sys.argv
NOTES = os.path.join(VAULT, '3. Notes')

BOOKS = {
    'IWANAGA': ('Atlas of Oral and Maxillofacial Anatomy - Iwanaga & Tubbs (2021)', 'Iwanaga & Tubbs, Atlas of OMF Anatomy'),
    'SALYER1': ('Atlas of Craniofacial and Cleft Surgery Vol I Craniofacial Surgery - Salyer & Bardach (2008)', 'Salyer & Bardach, Atlas Vol I'),
    'SALYER2': ('Atlas of Craniofacial and Cleft Surgery Vol II Cleft Lip and Palate Surgery - Salyer & Bardach (2008)', 'Salyer & Bardach, Atlas Vol II'),
    'KATZUNG': ('Basic and Clinical Pharmacology 14th Ed - Katzung (2018)', 'Katzung, Basic and Clinical Pharmacology'),
    'RIUS': ('Bioestadística Métodos y aplicaciones - Ríus Díaz & Barón López', 'Ríus y Barón, Bioestadística'),
    'ORELLANA': ('Bioestadística aplicada a investigaciones científicas en salud - Orellana & Cañarte (2022)', 'Orellana, Bioestadística aplicada'),
    'ALONSO': ('Cleft Lip and Palate Treatment A Comprehensive Guide - Alonso & Raposo-Amaral (2018)', 'Alonso, Cleft Lip and Palate Treatment'),
    'SKULLBASE': ('Cranial, Craniofacial and Skull Base Surgery - Cappabianca, Califano & Iaconetta (2010)', 'Cappabianca, Skull Base Surgery'),
    'SPERBER': ('Craniofacial Development - Sperber (2001)', 'Sperber, Craniofacial Development'),
    'MCCARTHY': ('Craniofacial Distraction - McCarthy (2017)', 'McCarthy, Craniofacial Distraction'),
    'CFM_TCS': ('Craniofacial Microsomia and Treacher Collins Syndrome - Yates & Markiewicz (2022)', 'Yates, Craniofacial Microsomia and TCS'),
    'THALLER': ('Craniofacial Surgery - Thaller, Bradley & Garri (2008)', 'Thaller, Craniofacial Surgery'),
    'CCNOTES': ('Critical Care Notes Clinical Pocket Guide - Jones & Fix (2009)', 'Critical Care Notes'),
    'JIMENEZ': ('Endoscopic Craniosynostosis Surgery An Illustrated Guide to Endoscopic Techniques - Jimenez (2023)', 'Jimenez, Endoscopic Craniosynostosis Surgery'),
    'REYNEKE': ('Essentials of Orthognathic Surgery 3rd Ed - Reyneke (2022)', 'Reyneke, Essentials of Orthognathic Surgery'),
    'MARIK': ('Evidence-Based Critical Care 3rd Ed - Marik (2015)', 'Marik, Evidence-Based Critical Care'),
    'TRAUMA': ('Facial Trauma Surgery From Primary Repair to Reconstruction - Dorafshar, Rodriguez & Manson (2020)', 'Dorafshar, Facial Trauma Surgery'),
    'FERRARO': ("Ferraro's Fundamentals of Maxillofacial Surgery 2nd Ed - Taub, Patel, Buchman & Cohen (2015)", "Ferraro's Fundamentals"),
    'PERRY': ('Manual of Operative Maxillofacial Trauma Surgery - Perry & Holmes (2014)', 'Perry & Holmes, Operative Maxillofacial Trauma'),
    'SINGH': ('Maxillofacial Trauma A Clinical Guide - Singh & Sharma (2021)', 'Singh, Maxillofacial Trauma'),
    'CSO': ('Neurosurgical Aspects of Craniosynostosis - Di Rocco & Kestle (2024)', 'Di Rocco, Neurosurgical Aspects of Craniosynostosis'),
    'SECRETS': ('Oral and Maxillofacial Surgery Secrets 3rd Ed - Abubaker (2016)', 'OMFS Secrets'),
    'FRAGISKOS': ('Oral Surgery - Fragiskos (2007)', 'Fragiskos, Oral Surgery'),
    'MOORE': ('Principles of Oral and Maxillofacial Surgery 6th Ed - Moore (2011)', 'Moore, Principles of OMFS'),
    'ELLIS': ('Surgical Approaches to the Facial Skeleton 3rd Ed - Ellis & Zide (2019)', 'Ellis & Zide, Surgical Approaches'),
}

# Books split into volumes to stay under GitHub's 100 MB file limit: key -> [(first, last), ...] in the original
# page numbering. Curriculum and tocs/ keep using original pages; links point to "<file> - Vol N.pdf".
VOLUMES = {}

def book_file(key, page=None):
    """File name (without .pdf) and page within that file for a page of the original book."""
    fn = BOOKS[key][0]
    for k, (a, b) in enumerate(VOLUMES.get(key, []), 1):
        if page is None or a <= page <= b:
            return f'{fn} - Vol {k}', (page - a + 1 if page else None)
    return fn, page

def book_label(key):
    return BOOKS[key][1] + (f' ({len(VOLUMES[key])} vols.)' if key in VOLUMES else '')

BAD_CHARS = set('\\/:*?"<>|#^[]')
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\t', ' ')).strip()

_toc_cache = {}
def toc(key):
    if key not in _toc_cache:
        path = os.path.join(SCR, 'tocs', BOOKS[key][0] + '.txt')
        rows = []
        if os.path.exists(path):
            for line in open(path, encoding='utf-8', newline='').read().split('\n'):
                m = re.match(r'^(.*?)\s+\[p(\d+|\?)\]\s*$', line, re.S)
                if m:
                    rows.append((norm(m.group(1)), None if m.group(2) == '?' else int(m.group(2))))
        _toc_cache[key] = rows
    return _toc_cache[key]

def clean_title(t):
    t = t.replace('◆', '').strip()
    if t.isupper():
        t = t.title()
    for c in '[]|#^':
        t = t.replace(c, ' ')
    return norm(t)

errors, warnings = [], []
MATCHES = []

def resolve_source(spec, where):
    key, _, rest = spec.partition(' ')
    if key not in BOOKS:
        errors.append(f'{where}: unknown book {key}')
        return None
    rest = rest.strip()
    page = None
    if rest.startswith('!'):
        label = rest[1:]
        m = re.search(r'\s*@(\d+)$', label)
        if m:
            page, label = int(m.group(1)), label[:m.start()]
        return key, clean_title(label), page
    q = re.sub(r'\s+', '', rest)
    for title, p in toc(key):
        if q in re.sub(r'\s+', '', title):
            MATCHES.append((key, rest, title, p))
            return key, clean_title(title), p
    errors.append(f'{where}: not found in {key}: "{rest}"')
    return None

def parse():
    areas, cur_area, cur_mod, cur_ses = [], None, None, None
    for path in sorted(glob.glob(os.path.join(SCR, 'curriculum', '*.txt'))):
        for n, raw in enumerate(open(path, encoding='utf-8'), 1):
            line = raw.rstrip('\n').strip()
            where = f'{os.path.basename(path)}:{n}'
            if not line:
                continue
            if line.startswith('@AREA'):
                num, name, slug = [x.strip() for x in line[5:].split('|')]
                cur_area = dict(num=num, name=name, slug=slug, books=[], modules=[], where=where)
                areas.append(cur_area); cur_mod = cur_ses = None
            elif line.startswith('@BOOKS'):
                cur_area['books'] = [b.strip() for b in line[6:].split(',')]
            elif line.startswith('## '):
                cur_mod = dict(title=line[3:].strip(), sessions=[], refs=[])
                cur_area['modules'].append(cur_mod); cur_ses = None
            elif line.startswith('# '):
                title = line[2:].strip()
                # file name = order within the module + title, e.g. "01. Superficial anatomy of the face"
                cur_ses = dict(title=title, file=f"{len(cur_mod['sessions']) + 1:02d}. {title}",
                               sources=[], objectives=[], where=where, area=cur_area, module=cur_mod)
                cur_mod['sessions'].append(cur_ses)
            elif line.startswith('S '):
                src = resolve_source(line[2:], where)
                if src: cur_ses['sources'].append(src)
            elif line.startswith('- '):
                cur_ses['objectives'].append(line[2:].strip())
            elif line.startswith('> '):
                cur_mod['refs'].append((line[2:].strip(), where))
            else:
                errors.append(f'{where}: unparsed line: {line}')
    return areas

def link_source(key, label, page):
    short = BOOKS[key][1]
    fn, page = book_file(key, page)
    target = f'{fn}.pdf' + (f'#page={page}' if page else '')
    return f'[[{target}|{short} — {label}]]'

def main():
    areas = parse()
    sessions = [s for a in areas for m in a['modules'] for s in m['sessions']]
    by_title = {}
    reserved = set()
    rp = os.path.join(SCR, 'reserved_names.txt')
    if os.path.exists(rp):
        reserved = {l.strip().lower() for l in open(rp, encoding='utf-8') if l.strip()}
    for s in sessions:
        t = s['title']
        if any(c in BAD_CHARS for c in t):
            errors.append(f"{s['where']}: illegal char in title: {t}")
        if t.lower() in by_title:
            errors.append(f"{s['where']}: duplicate title: {t}")
        if t.lower() in reserved:
            errors.append(f"{s['where']}: title collides with archived note: {t}")
        by_title[t.lower()] = s
        if not s['sources']:
            warnings.append(f"{s['where']}: no sources: {t}")
        if len(s['objectives']) < 2:
            warnings.append(f"{s['where']}: <2 objectives: {t}")
        if any(p is None for _, _, p in s['sources']):
            pass
    for a in areas:
        for m in a['modules']:
            for t, where in m['refs']:
                if t.lower() not in by_title:
                    errors.append(f'{where}: cross-reference not found: {t}')
    nopage = sum(1 for s in sessions for _, _, p in s['sources'] if not p)
    nsrc = sum(len(s['sources']) for s in sessions)
    print(f'areas={len(areas)} sessions={len(sessions)} sources={nsrc} without_page={nopage}')
    for a in areas:
        print(f"  {a['num']}. {a['name']}: {sum(len(m['sessions']) for m in a['modules'])} sessions, {len(a['modules'])} modules")
    if '--dump' in sys.argv:
        for k, q, t, p in MATCHES:
            flag = '' if re.sub(r'\s+','',t).startswith(re.sub(r'\s+','',q)) else '  <-- not prefix'
            print(f'{k:10s} p{p}	{q[:40]:40s} => {t[:80]}{flag}')
        return
    for w in warnings: print('WARN', w)
    for e in errors: print('ERROR', e)
    if errors or not WRITE:
        return
    write(areas, by_title)

def index_name(a):
    return f"{a['name']} - Index"

def write(areas, by_title):
    for a in areas:
        adir = os.path.join(NOTES, f"{a['num']}. {a['name']}")
        os.makedirs(adir, exist_ok=True)
        flat = [s for m in a['modules'] for s in m['sessions']]
        for i, s in enumerate(flat):
            mi = a['modules'].index(s['module']) + 1
            mdir = os.path.join(adir, f"{mi:02d}. {s['module']['title']}")
            os.makedirs(mdir, exist_ok=True)
            prev_ = f"[[{flat[i-1]['file']}]]" if i > 0 else '—'
            next_ = f"[[{flat[i+1]['file']}]]" if i + 1 < len(flat) else '—'
            lines = ['---', 'tipo: sesion', f'aliases: ["{s["title"]}"]', f'area: "[[{index_name(a)}]]"',
                     f'modulo: "{s["module"]["title"]}"', f'tags: [area/{a["slug"]}]',
                     'estado: pendiente', '---',
                     '> [!todo] Session objectives']
            lines += [f'> - [ ] {o}' for o in s['objectives']]
            lines += ['', '**Sources**']
            lines += [f'- {link_source(*src)}' for src in s['sources']]
            lines += ['', f'**Index:** [[{index_name(a)}]] · **Previous:** {prev_} · **Next:** {next_}',
                      '', '---', '', '']
            path = os.path.join(mdir, s['file'] + '.md')
            if os.path.exists(path):
                continue  # never overwrite: below the second '---' the notes belong to the user
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write('\n'.join(lines))
            print('created', path)
        # area index
        n = len(flat)
        books = ' · '.join(f"[[{book_file(b)[0]}.pdf|{book_label(b)}]]" for b in a['books'])
        out = ['---', 'tipo: indice-area', f'area: {a["name"]}', f'tags: [area/{a["slug"]}]', f'sesiones: {n}', '---',
               f"# {a['name']} — Index", '',
               '> [!abstract] About this index',
               f"> Unified syllabus of **{n} sessions** built from: {books}.",
               '> Tick a session when your notes for it are complete. Links marked ↗ point to sessions that live in another area.',
               '']
        for mi, m in enumerate(a['modules'], 1):
            out.append(f"## {mi}. {m['title']}")
            for s in m['sessions']:
                out.append(f"- [ ] [[{s['file']}]]")
            for t, _ in m['refs']:
                s = by_title[t.lower()]
                out.append(f"- ↗ [[{s['file']}]] · *{s['area']['name']}*")
            out.append('')
        ipath = os.path.join(adir, index_name(a) + '.md')
        if os.path.exists(ipath):
            # never overwrite an index: the user's ticks live there
            text = open(ipath, encoding='utf-8').read()
            for s in flat:
                if f"[[{s['file']}]]" not in text:
                    print(f"ADD TO INDEX MANUALLY ({index_name(a)}): {s['file']}")
            continue
        with open(ipath, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(out))
        print('created', ipath)
    # summary for the global index
    with open(os.path.join(SCR, 'areas_summary.tsv'), 'w', encoding='utf-8') as f:
        for a in areas:
            f.write(f"{a['num']}\t{a['name']}\t{index_name(a)}\t{sum(len(m['sessions']) for m in a['modules'])}\t{','.join(a['books'])}\n")
    print('written')

main()
