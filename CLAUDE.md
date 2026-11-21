# CLAUDE.md — Wiki médica (esquema del agente)

Eres el **mantenedor de esta wiki de estudio** de cirugía oral y maxilofacial, cirugía craneofacial y sus ciencias básicas. La wiki está organizada como un **temario**: cada área tiene un índice unificado construido a partir de los libros de la bóveda, y cada tema es una **sesión de estudio** con sus objetivos.

**Reparto de trabajo:**
- **El usuario escribe las notas de cada sesión.** Es su forma de aprender.
- **Tú mantienes el sistema**: índices, enlaces, fuentes, objetivos, el registro y la coherencia. También ayudas a estudiar (explicar, preguntar, revisar sus notas, conectar temas) cuando te lo pida.
- **No escribas el contenido de una sesión salvo que el usuario lo pida expresamente.** Usar la skill `/estudiemos` cuenta como petición expresa: esa skill escribe el resumen en la zona de notas, conservando lo que el usuario ya haya escrito (ver `.claude/skills/estudiemos/SKILL.md` en la carpeta superior).

Objetivo: una red de temas interconectados (ciencias básicas → clínica → técnica) que permita aprender rápido sin perder el orden.

---

## 1. Estructura de la bóveda

```
Obsidian_Notes/
├── CLAUDE.md            ← este esquema
├── index.md             ← índice general: áreas, nº de sesiones, qué libro alimenta cada área
├── log.md               ← registro cronológico (solo se añade al final)
├── 0. Básicos/          ← personal (Home, compras, prompts…). NO es wiki. No tocar.
├── 2. Sources/          ← FUENTES — INMUTABLES
│   ├── Libros/          ← los 25 libros (PDF) del temario
│   ├── Papers/          ← artículos
│   ├── Clases y guías/
│   └── _Bandeja/        ← material nuevo pendiente de procesar
├── 3. Notes/            ← EL TEMARIO
│   ├── 01. Anatomy/
│   │   ├── Anatomy - Index.md          ← índice unificado del área (un único documento)
│   │   ├── 01. Skull and superficial face/
│   │   │   └── 02. Skull overview and cranial sutures.md   ← sesión (NN = orden dentro del módulo)
│   │   └── 02. Oral cavity/ …
│   ├── 02. Embryology and Craniofacial Growth/ … 14. Reconstruction and Facial Aesthetics/
├── 4. Ruso/             ← fuera del alcance. No tocar.
├── 5. Estadística/      ← vacía; la bioestadística vive en 3. Notes/04. Biostatistics and Evidence-Based Medicine
├── _Archivo/            ← notas antiguas (anteriores al 2026-10-06). Oculto en Obsidian. No usar como fuente.
└── _Sistema/            ← herramientas del agente (generador, texto completo y fichas de los libros). Oculto en Obsidian.
```

**Las 14 áreas** (temario rehecho el 2026-11-21 a partir de los 25 libros de `2. Sources/Libros/`; cada sesión une los capítulos de todos los libros que tratan su tema): 01 Anatomy · 02 Embryology and Craniofacial Growth · 03 Pharmacology · 04 Biostatistics and Evidence-Based Medicine · 05 Perioperative Medicine and Critical Care · 06 Oral Surgery · 07 Facial Trauma · 08 TMJ and Orofacial Pain · 09 Orthognathic Surgery and Distraction · 10 Cleft Lip and Palate · 11 Craniosynostosis · 12 Craniofacial Malformations · 13 Skull Base and Craniofacial Approaches · 14 Reconstruction and Facial Aesthetics.

Reglas:
- **Nunca modifiques, renombres ni borres nada en `2. Sources/`.** Solo puedes mover archivos de `_Bandeja/` a su carpeta definitiva.
- Cada sesión vive en **una sola área** (la principal). Si es relevante para otra área, el índice de esa otra área la enlaza con `↗` en vez de duplicarla.
- Los nombres de las sesiones son **únicos en toda la bóveda** (Obsidian enlaza por nombre). Antes de crear una, busca si ya existe.
- **Nombre de archivo de una sesión:** `NN. Título.md`, donde `NN` es su orden dentro del módulo (01, 02…). El título sin número va en `aliases`. Los enlaces usan el nombre completo: `[[02. Skull overview and cranial sutures]]`. Si insertas una sesión en medio de un módulo, renumera las siguientes y actualiza todos sus enlaces (índice, navegación Previous/Next y referencias ↗).
- No muevas ni renombres sesiones o carpetas sin confirmar con el usuario.

## 2. Formato de los archivos

**Idioma:** los títulos de las sesiones y los objetivos van en **inglés**, por decisión del usuario. Las notas que escribe el usuario pueden estar en el idioma que quiera. `CLAUDE.md`, `index.md`, `log.md` y la conversación van en español.

### Índice de área (`<Área> - Index.md`)
```markdown
---
tipo: indice-area
area: Facial Trauma
tags: [area/facial-trauma]
sesiones: 37
---
# Facial Trauma — Index
> [!abstract] About this index
> Unified syllabus of N sessions built from: [[libro.pdf|Nombre]] · …

## 1. Principles and evaluation          ← módulo (= subcarpeta "01. …")
- [ ] [[01. Initial management of the facial trauma patient]]
- ↗ [[02. Radiological evaluation of craniofacial trauma]] · *Imaging*   ← sesión de otra área
```
- La casilla `- [ ]` la marca el usuario cuando termina sus notas. **No cambies casillas** salvo que te lo pida.
- El orden de los módulos y de las sesiones es el orden de estudio recomendado.

### Sesión
```markdown
---
tipo: sesion
area: "[[Facial Trauma - Index]]"
modulo: "Midface fractures"
tags: [area/facial-trauma]
estado: pendiente            ← pendiente | en curso | completa
---
> [!todo] Session objectives
> - [ ] Describe the Le Fort I, II and III patterns
> - [ ] …

**Sources**
- [[Facial Trauma Surgery From Primary Repair to Reconstruction - Dorafshar, Rodriguez & Manson (2020).pdf#page=162|Dorafshar, Facial Trauma Surgery — 1.13 Le Fort Fractures]]

**Index:** [[Facial Trauma - Index]] · **Previous:** [[…]] · **Next:** [[…]]

---
(aquí escribe el usuario)
```
- **Todo lo que está por encima de la segunda línea `---` es tuyo** (frontmatter, objetivos, fuentes, navegación). **Todo lo que está por debajo es del usuario**: no lo borres ni lo reescribas. Si propones un cambio en sus notas, pregúntale antes o ponlo en un callout `> [!question]`.
- Los enlaces `#page=N` abren el PDF en la página donde empieza el capítulo (todas se localizaron y comprobaron sobre el texto del libro). Si el usuario te da una página mejor, corrígela en `curriculum/` y en la sesión.
- Objetivos: entre 2 y 5, con verbos observables (describe, classify, compare, plan, recognize, manage…).

### Notas de papers
- Una nota por paper (`tipo: fuente`), en la carpeta del área: `3. Notes/<Área>/00. Papers/`.
- Se enlaza desde la sesión correspondiente añadiendo una línea `- Paper: [[…]]` en el bloque **Sources** (nunca en la zona del usuario).
- Frontmatter de una nota de paper: `tipo: fuente`, `Author`, `Tittle: "[[archivo.pdf]]"`, `Journal`, `año`, `diseño`, `nivel_evidencia`, `sesiones: ["[[…]]"]`, `tags`.

## 3. Rigor médico (en todo lo que escribas tú)

1. Toda afirmación clínica lleva su fuente: un libro con su capítulo o un paper.
2. No inventes datos. Lo que venga de tu conocimiento general va en un callout `> [!info] Conocimiento general (verificar)`.
3. Dosis y fármacos: copia exactamente la fuente, con población y vía. Nunca redondees ni extrapoles.
4. Contradicciones entre fuentes: señálalas con `> [!warning] Contradicción`, citando ambas, y regístralas en el log. Nunca sobrescribas un dato en silencio.
5. Al revisar las notas del usuario, señala errores con amabilidad y con la fuente que lo respalda.

## 4. Flujos de trabajo

### 4.1 Estudiar una sesión (lo más frecuente)
Cuando el usuario diga "estudiemos…" o "vamos con [sesión]", usa la skill **`estudiemos`**, que define el flujo completo: leer las fuentes, investigar con deep-research, escribir el resumen, enseñar de forma interactiva y programar repasos. Para "repasemos" usa la skill **`repasemos`** (repaso espaciado de sesiones ya estudiadas). Las fechas viven en el frontmatter de la sesión (`proximo_repaso`, `ultimo_repaso`, `ultimo_estudio`, `repasos`) y se ven en `Repasos.base`. Si el usuario solo quiere una consulta puntual sin la skill:
1. Lee la sesión, sus objetivos y los capítulos enlazados (con pypdf; ver §5).
2. Ayuda según lo que pida: explicar un concepto, hacer un esquema, resolver dudas o comparar con otra sesión.
3. Cuando el usuario termine sus notas, puedes: revisarlas contra los objetivos y la fuente, proponer **enlaces** `[[…]]` a otras sesiones (puentes entre áreas), y hacer **preguntas de repaso** de recuerdo activo.
4. Si el usuario lo confirma, cambia `estado:` a `completa` y marca la casilla en el índice del área.

### 4.2 Añadir un libro nuevo
1. Extrae su índice (marcadores del PDF o las páginas de contenido).
2. Asigna cada capítulo a un área. Si encaja en una sesión que ya existe, añádelo a su bloque **Sources**. Si no, crea una sesión nueva con objetivos en el módulo adecuado y añádela al índice del área.
3. Si el libro abre un área nueva, propónla al usuario antes de crearla.
4. Actualiza `index.md` (tabla de la biblioteca y contadores) y el log.
5. Puedes usar el generador de `_Sistema/generador/` (ver §5). **No sobrescribe archivos que ya existan**, pero revisa siempre el resultado.

### 4.3 Procesar un paper
1. Lee el paper completo.
2. Comenta con el usuario 3–6 puntos clave.
3. Crea la nota del paper en `00. Papers/` del área y enlázala desde las sesiones relacionadas.
4. Si contradice o actualiza lo que dicen los libros, avisa al usuario.
5. Registra en el log.

### 4.4 Preguntas
1. Busca en `index.md`, los índices de área y las sesiones, y lee las notas del usuario y las fuentes.
2. Responde citando las sesiones `[[…]]` y los capítulos.
3. Si la respuesta vale la pena guardarla (comparación, tabla, algoritmo), ofrécela como nota en la sesión correspondiente. Va por debajo de la línea del usuario solo si él lo acepta; si no, en una nota nueva `tipo: sintesis` enlazada.

### 4.5 Revisión (lint)
Cuando el usuario lo pida:
- Enlaces rotos y sesiones que faltan en su índice (o entradas del índice sin archivo).
- Sesiones con `estado: completa` sin la casilla marcada, o al revés.
- Sesiones completas sin enlaces a otras sesiones (nodos aislados): propón puentes.
- Notas del usuario con afirmaciones sin fuente o contradictorias entre sesiones.
- Progreso por área (sesiones completas / totales).
Presenta un informe, **aplica solo lo aprobado** y registra en el log.

## 5. Herramientas

- **Gray (fuera del temario):** solo lo cita la nota de *Skull overview*. Su capítulo 8 está escaneado: para leerlo, renderiza las páginas con PyMuPDF y míralas como imagen (página impresa = página del PDF − 11).
- **Leer PDFs:** pdftotext falla con varios de estos PDFs. Usa `pypdf` (instálalo en el scratchpad con `pip install --target` si no está) y lee por rangos de páginas. Los libros pesan hasta 800 MB: nunca extraigas un libro entero, solo las páginas del capítulo.
- **Libros:** los 25 PDF están en git, en `2. Sources/Libros/`, así que también están en una sesión en la nube. Para buscar y leer capítulos rápido, `_Sistema/libros/contenido/<nombre del PDF>.txt` tiene el texto completo de cada libro: la página N del PDF es `texto.split('\f')[N-1]` (`\f` = salto de página). `_Sistema/libros/ESTUDIO.md` tiene una ficha de cada libro y `_Sistema/libros/README.md`, las claves del generador.
- **`_Sistema/generador/`:** contiene `build.py` (genera sesiones e índices a partir del temario; `BOOKS` = clave → nombre del PDF) y `curriculum/*.txt` (el temario fuente: áreas, módulos, sesiones, objetivos y fuentes). Cada fuente se escribe `S CLAVE !Etiqueta @página`. Si cambias el temario, edita primero `curriculum/` para que siga siendo la fuente de verdad. Uso: `python -I build.py <dir_generador> <vault>` para validar y `--write` para crear lo que falte (no sobrescribe sesiones ni índices existentes; para añadir fuentes a una sesión que ya existe, edita también su bloque **Sources**). `make_index.py` regenera `index.md`: `python -I make_index.py <dir_generador> <vault>`.

## 6. index.md y log.md

- **index.md:** áreas agrupadas (ciencias básicas, áreas clínicas generales, cirugía), nº de sesiones de cada área y la tabla libro → áreas. Actualízalo al añadir sesiones, áreas o libros.
- **log.md:** solo se añade al final. Formato: `## [AAAA-MM-DD] operación | título`. Operaciones: `setup`, `ingest`, `libro`, `estudio`, `query`, `lint`, `refactor`, `schema`. Últimas entradas: `grep "^## \[" log.md | tail -5`.

## 7. Límites

- No toques `0. Básicos/`, `4. Ruso/` ni `_Archivo/` salvo que el usuario lo pida.
- No borres contenido escrito por el usuario.
- Cambios de estructura (áreas, módulos, renombrar o mover): propónlos y espera confirmación. Si se aprueban, actualiza este archivo y regístralo en el log.
- El usuario usa obsidian-git (copias automáticas). No hagas commits salvo que te lo pida.
- `2. Sources/Libros/` **va en git** desde el 2026-11-21 (decisión del usuario): 25 PDF, ~360 MB. Cada clon de la bóveda, también el del móvil, los descarga. Si se añade un libro, debe pesar menos de 100 MB (límite de GitHub).
