"""Busca y recorta figuras de los libros de 2. Sources/Libros.

    pip install pymupdf

1) Buscar la página de una figura por el texto de su pie:
    python3 _Sistema/figuras/figura.py buscar "Iwanaga" "Lateral view of the skull" --preview /tmp/prev.png
   Imprime la página, el tamaño de la página, las cajas de las imágenes y los pies de figura.
   Con --preview guarda una vista previa a baja resolución para revisar el recorte.

2) Recortar (coordenadas en puntos PDF, x0 y0 x1 y1; usa las cajas que imprime "buscar"):
    python3 _Sistema/figuras/figura.py recortar "Iwanaga" 13 48 52 548 268 \
        "01. Anatomy" "Iwanaga Fig 2.6 - Vista lateral del cráneo"
   Guarda 2. Sources/Figuras/<Área>/<nombre>.jpg a 200 dpi.
"""
import sys
from pathlib import Path

import pymupdf

VAULT = Path(__file__).resolve().parents[2]
LIBROS = VAULT / '2. Sources' / 'Libros'


def libro(fragmento):
    hits = [p for p in LIBROS.glob('*.pdf') if fragmento.lower() in p.name.lower()]
    if len(hits) != 1:
        sys.exit(f'"{fragmento}" coincide con {len(hits)} libros: {[h.name for h in hits]}')
    return pymupdf.open(hits[0])


def buscar(frag, texto, preview=None):
    doc = libro(frag)
    for i, pg in enumerate(doc):
        if pg.search_for(texto):
            print(f'página {i + 1}  tamaño {pg.rect}')
            for info in pg.get_image_info():
                print('  imagen', [round(v) for v in info['bbox']])
            for b in pg.get_text('blocks'):
                if b[4].lstrip().lower().startswith(('fig', 'figure', 'figura')):
                    print('  pie', [round(v) for v in b[:4]], b[4].strip()[:70])
            if preview:
                pg.get_pixmap(dpi=60).save(preview)
            return
    print('no encontrado')


def recortar(frag, pagina, x0, y0, x1, y1, area, nombre):
    pg = libro(frag)[int(pagina) - 1]
    destino = VAULT / '2. Sources' / 'Figuras' / area
    destino.mkdir(parents=True, exist_ok=True)
    pix = pg.get_pixmap(dpi=200, clip=pymupdf.Rect(*map(float, (x0, y0, x1, y1))))
    salida = destino / f'{nombre}.jpg'
    pix.save(salida, jpg_quality=85)
    print(salida, pix.width, 'x', pix.height)


if __name__ == '__main__':
    cmd, *a = sys.argv[1:]
    if cmd == 'buscar':
        prev = a[a.index('--preview') + 1] if '--preview' in a else None
        buscar(a[0], a[1], prev)
    elif cmd == 'recortar':
        recortar(*a)
    else:
        sys.exit(__doc__)
