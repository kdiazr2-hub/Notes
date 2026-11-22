# Plantilla de sesión

Formato de las notas de sesión en `3. Notes/`. **La nota se escribe en inglés** (ver [[Instrucciones de estudio]]). La idea: **repasar = intentar recordar, no releer**. La nota debe caber en una o dos pantallas. Ejemplo completo: [[01. Skull overview and cranial sutures]].

```
---
tipo: sesion
aliases: [...]
area: "[[<Area> - Index]]"
modulo: "<module>"
tags: [area/<area>]
estado: completado
fecha: AAAA-MM-DD
---
# Title

**In one sentence:** the idea that explains everything.
**Index:** [[<Area> - Index]] · **Next:** [[...]]

## Map              → tablas o esquemas con la estructura del tema + figuras clave
## Essentials       → 5–7 puntos, cada uno con su "because…"
## Don't confuse    → tabla A vs. B: cómo distinguirlos
## Case             → viñeta clínica; resolución en > [!example]- Resolution (colapsada)
## Test yourself    → > [!question]- con la respuesta escondida;
                      preguntas con imagen: > [!question] + imagen + > > [!success]- Answer
## My mistakes      → lo que el usuario falló en la sesión y por qué (en primera persona)
## Connections      → [[Existing note]] (motivo del enlace); solo enlaces a notas que existen
## Sources          → libro + página/figura
```

## Convenciones

- **Figuras de los libros:** se recortan del PDF en `2. Sources/Libros/` y se guardan en `2. Sources/Figuras/<Area>/` con el nombre `<Author> Fig <n> - <English description>.jpg`. Se insertan con `![[name.jpg|width]]` y un pie en cursiva, en inglés, que diga qué mirar en la imagen.
- **Anki (en inglés):** un mazo por sesión, `Oral and Maxillofacial Surgery::<NN Area>::<NN Topic>`, con el tipo de nota "Notes - Básica" (id 1607392319; campos Pregunta / Respuesta / Fuente, que son nombres internos). Las imágenes se nombran `notes_<area><NN>_<key>.jpg` para que no choquen entre mazos. El GUID de cada tarjeta sale del texto de la pregunta, así que reimportar actualiza las tarjetas en vez de duplicarlas. Si cambias una pregunta ya estudiada, fija su GUID anterior en el campo `guid` del JSON.
