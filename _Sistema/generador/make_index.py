"""Regenerate Obsidian_Notes/index.md from the curriculum (areas, session counts, book -> areas table).

Usage: python -I make_index.py <generador_dir> <vault>
"""
import os, sys, io, collections, datetime
G, V = sys.argv[1], sys.argv[2]
sys.path.insert(0, G)
sys.argv = ['build.py', G, V]
_out = sys.stdout
sys.stdout = open(os.devnull, 'w', encoding='utf-8')
import build  # validation only, output discarded
sys.stdout = _out
areas = build.parse()
BOOKS = build.BOOKS

rows = [(a['num'], a['name'], f"{a['name']} - Index", sum(len(m['sessions']) for m in a['modules'])) for a in areas]
total = sum(r[3] for r in rows)
used = collections.defaultdict(list)
for a in areas:
    for b in a['books']:
        used[b].append(f"[[{a['name']} - Index\\|{a['name']}]]")

groups = [('Basic sciences', ['01', '02', '03', '04', '05', '06', '07']),
          ('Diagnosis and general clinical areas', ['08', '09', '10', '11', '12']),
          ('Oral and maxillofacial surgery', ['13', '14', '15', '16', '17', '18', '19'])]
by = {r[0]: r for r in rows}
out = ['---', 'tipo: indice', f'actualizado: {datetime.date.today().isoformat()}', '---', '# Índice de la wiki', '',
       '> [!abstract] Estado',
       f'> **{len(rows)} áreas · {total} sesiones · {len(BOOKS)} libros + 12 papers.**',
       '> Cada área tiene un índice con sus sesiones. Cada sesión empieza con sus objetivos y enlaza al capítulo exacto del libro; debajo van las notas.',
       '> Estado de una sesión: `estado: pendiente` → `en curso` → `completa` (propiedad en el frontmatter), y la casilla del índice del área.',
       '',
       '## Repasos',
       'Sesiones con repaso vencido o próximo (se llenan al estudiar con `/estudiemos`; se repasan con `/repasemos`):',
       '', '![[Repasos.base]]', '']
for title, nums in groups:
    out += [f'## {title}', '', '| # | Área | Sesiones |', '|---|---|---|']
    for n in nums:
        r = by[n]
        out.append(f'| {r[0]} | [[{r[2]}\\|{r[1]}]] | {r[3]} |')
    out.append('')
out += ['## Biblioteca: qué libro alimenta cada área', '', '| Libro | Áreas |', '|---|---|']
for k, (fn, short) in sorted(BOOKS.items(), key=lambda x: x[1][0]):
    vols = build.VOLUMES.get(k, [])
    cell = f"[[{fn}.pdf\\|{short}]]" if not vols else \
        f"{short}: " + ' · '.join(f"[[{fn} - Vol {i}.pdf\\|Vol {i}]]" for i in range(1, len(vols) + 1))
    out.append(f"| {cell} | {' · '.join(used.get(k, [])) or '—'} |")
out += ['', '## Papers',
        '- 12 artículos en `2. Sources/Papers/` (labio y paladar hendido, cresta ilíaca, microtia). Se integrarán en las sesiones correspondientes cuando se procesen.', '',
        '## Archivo', '- Las notas anteriores al 2026-10-06 están en `_Archivo/` (oculto en Obsidian).', '']
with open(os.path.join(V, 'index.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(out))
print(f'index.md: {len(rows)} areas, {total} sessions')
