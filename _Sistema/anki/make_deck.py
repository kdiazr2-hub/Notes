"""Genera un mazo de Anki (.apkg) a partir de un archivo JSON de tarjetas.

Uso (desde cualquier carpeta):
    pip install genanki
    python3 "_Sistema/anki/make_deck.py" "_Sistema/anki/mazos/01-01 Skull and sutures.json" -o salida/

Formato del JSON:
{
  "mazo": "Oral and Maxillofacial Surgery::01 Anatomy::01 Skull and sutures",
  "fuente": "Anatomy 01 · Skull and sutures",          # se muestra en la respuesta
  "etiquetas": ["anatomy", "session01"],
  "prefijo_media": "notes_anat01_",                       # único por sesión
  "imagenes": {"clave": "2. Sources/Figuras/<Área>/<archivo>.jpg"},   # rutas desde la raíz del vault
  "tarjetas": [
    {"p": "Question", "r": "Answer", "img_p": "clave opcional", "img_r": "clave opcional",
     "guid": "opcional"}
  ]
}

Las tarjetas se escriben en inglés (ver _Sistema/Instrucciones de estudio.md).

El GUID de cada tarjeta sale del texto final de la pregunta: reimportar un mazo
actualiza las tarjetas en vez de duplicarlas. Si cambias el texto de una pregunta
ya estudiada (por ejemplo, al traducirla), fija su GUID anterior en "guid" para
que Anki la actualice y conserve su historial de repaso.
"""
import argparse, hashlib, json, os, shutil, tempfile
from pathlib import Path

import genanki

VAULT = Path(__file__).resolve().parents[2]

MODELO = genanki.Model(
    1607392319, 'Notes - Básica',
    fields=[{'name': 'Pregunta'}, {'name': 'Respuesta'}, {'name': 'Fuente'}],
    templates=[{
        'name': 'Tarjeta',
        'qfmt': '{{Pregunta}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Respuesta}}<br><br>'
                '<small style="color:#888">{{Fuente}}</small>',
    }],
    css='.card{font-family:-apple-system,Helvetica,Arial;font-size:20px;'
        'text-align:left;line-height:1.4;}',
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('json')
    ap.add_argument('-o', '--salida', default='.')
    args = ap.parse_args()

    datos = json.loads(Path(args.json).read_text(encoding='utf-8'))
    prefijo = datos['prefijo_media']
    tmp = Path(tempfile.mkdtemp())
    media = []
    for clave, ruta in datos.get('imagenes', {}).items():
        destino = tmp / f'{prefijo}{clave}.jpg'
        shutil.copy(VAULT / ruta, destino)
        media.append(str(destino))

    def img(clave):
        return f'<br><img src="{prefijo}{clave}.jpg" style="max-width:100%">' if clave else ''

    mazo_id = int(hashlib.md5(datos['mazo'].encode()).hexdigest()[:8], 16)
    mazo = genanki.Deck(mazo_id, datos['mazo'])
    for t in datos['tarjetas']:
        p = t['p'] + img(t.get('img_p'))
        r = t['r'] + img(t.get('img_r'))
        mazo.add_note(genanki.Note(model=MODELO, fields=[p, r, datos['fuente']],
                                   tags=datos.get('etiquetas', []),
                                   guid=t.get('guid') or genanki.guid_for(p)))

    os.makedirs(args.salida, exist_ok=True)
    salida = Path(args.salida) / (Path(args.json).stem + '.apkg')
    paquete = genanki.Package(mazo)
    paquete.media_files = media
    paquete.write_to_file(salida)
    print(f'{salida}: {len(datos["tarjetas"])} tarjetas, {len(media)} imágenes')


if __name__ == '__main__':
    main()
