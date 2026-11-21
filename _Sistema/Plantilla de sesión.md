# Plantilla de sesión

Formato de las notas de sesión en `3. Notes/`. La idea: **repasar = intentar recordar, no releer**. La nota debe caber en una o dos pantallas. Ejemplo completo: [[01. Skull overview and cranial sutures]].

```
---
tipo: sesion
aliases: [...]
area: "[[<Área> - Index]]"
modulo: "<módulo>"
tags: [area/<área>]
estado: completado
fecha: AAAA-MM-DD
---
# Título

**En una frase:** la idea que lo explica todo.
**Index:** [[<Área> - Index]] · **Siguiente:** [[...]]

## Mapa            → tablas o esquemas con la estructura del tema + figuras clave
## Lo esencial     → 5–7 puntos, cada uno con su "porque…"
## No confundir    → tabla A vs. B: cómo distinguirlos
## Caso            → viñeta clínica; resolución en > [!example]- (colapsada)
## Ponte a prueba  → > [!question]- con la respuesta escondida;
                     preguntas con imagen: > [!question] + imagen + > > [!success]- Respuesta
## Mis errores     → lo que fallé en la sesión y por qué
## Conexiones      → [[Nota existente]] (motivo del enlace); solo enlaces a notas que existen
## Fuentes         → libro + página/figura
```

## Convenciones

- **Figuras de los libros:** se recortan del PDF en `2. Sources/Libros/` y se guardan en `2. Sources/Figuras/<Área>/` con el nombre `<Autor> Fig <n> - <descripción>.jpg`. Se insertan con `![[nombre.jpg|ancho]]` y un pie en cursiva que diga qué mirar en la imagen.
- **Anki:** un mazo por sesión, `Cirugía Maxilofacial::<NN Área>::<NN Tema>`, con el tipo de nota "Notes - Básica" (id 1607392319; campos Pregunta / Respuesta / Fuente). Las imágenes se nombran `notes_<área><NN>_<clave>.jpg` para que no choquen entre mazos. El GUID de cada tarjeta sale del texto de la pregunta, así que reimportar actualiza las tarjetas en vez de duplicarlas.
