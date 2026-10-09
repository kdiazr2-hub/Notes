---
tipo: log
---
# Log de la wiki

Registro cronológico, solo se añade al final. Formato: `## [AAAA-MM-DD] operación | título`
Últimas entradas: `grep "^## \[" log.md | tail -5`

## [2026-10-06] setup | Creación del sistema wiki
- Creados: `CLAUDE.md` (esquema), [[index]], [[log]], [[MOC - Craneofacial]], [[MOC - Ciencias básicas]]
- Carpetas nuevas: `1. Mapas/`, `2. Sources/_Bandeja/`, `2. Sources/Libros/`, `2. Sources/Clases y guías/`, `3. Notes/9. Síntesis/`
- No se movió ni modificó ninguna nota existente.
- Inventario inicial: 28 páginas wiki (7 con contenido, 21 vacías o solo con frontmatter) y 12 PDFs en `2. Sources/Papers/`.
- Pendientes para el primer lint:
  - 8 notas de fuente de LPH tienen frontmatter pero no resumen (los PDFs están disponibles para procesarlos).
  - Notas de síndromes, genética, embriología y materiales vacías.
  - Faltan páginas de concepto centrales (ver "Conceptos pendientes" en [[index]]).
  - `2. Sources/Papers base.base` filtra la carpeta `Notes/3. Art. Notes`, que ya no existe: la Base no muestra nada.
  - Las notas existentes no tienen las propiedades `tipo`, `tags` ni la sección Conexiones.

## [2026-10-06] ingest | Todd 2024: Iliac Crest Bone Graft Harvest for Alveolar Cleft Repair (RS trefina vs abierta)
- Completada: [[Iliac Crest Bone Graft Harvest for Alveolar Cleft Repair]] (antes solo tenía frontmatter; se conservaron las propiedades originales)
- Creadas: [[Iliac crest bone graft]] (tecnica, parcial) · [[Alveolar bone grafting]] (concepto, esbozo; integra también datos de las notas de Molnar y Junn)
- Actualizadas: [[MOC - Craneofacial]] · [[index]]
- Contradicciones: ninguna con la wiki. Dentro del paper, el resumen dice que la trefina acorta la estancia, pero en Bykowski la trefina sola (2.7 d) no fue más corta que la abierta (2.4 d); el efecto lo da la bomba de analgesia (0.5 d). Queda anotado en la fuente.
- Notas: el PDF tiene la tabla xref dañada; pdftotext falla y el texto se extrajo con pypdf. Comprobar si otros PDFs dan el mismo problema.

## [2026-10-06] refactor | Reinicio de la wiki a partir de los libros: temario de 19 áreas
- A petición del usuario, la wiki se reconstruye desde cero a partir de los 31 libros de `2. Sources/Libros/`.
- Archivado (no borrado) en `_Archivo/`: todo el contenido anterior de `3. Notes/` y `1. Mapas/` (30 notas, incluidas las 3 creadas hoy en la ingesta de Todd). `_Archivo/` y `_Sistema/` quedan ocultos en Obsidian (`userIgnoreFilters` en `.obsidian/app.json`).
- Creadas 19 áreas en `3. Notes/`, cada una con un índice unificado (`<Área> - Index.md`) y sus sesiones agrupadas por módulos: **682 sesiones**. Cada sesión tiene objetivos, fuentes con enlace a la página del capítulo (`#page=N`) y navegación anterior/siguiente.
- Decisiones del usuario: títulos y objetivos en inglés; capítulos de distintos libros fusionados en una sola sesión; notas antiguas archivadas.
- Las sesiones que sirven a varias áreas viven en una sola y se enlazan con ↗ desde las demás.
- 5 libros no tienen marcadores (Katzung, Murray, Hartl, Fragiskos, Distraction Osteogenesis): sus enlaces abren la página 1 y la etiqueta indica el capítulo. Bioestadística tiene las páginas calculadas a mano.
- `CLAUDE.md` reescrito: ahora el usuario escribe las notas de cada sesión y el agente mantiene el sistema.
- El generador y el temario fuente quedan en `_Sistema/generador/` (no sobrescribe archivos existentes).
- Incidencia: durante la instalación, el generador reescribió una vez las 701 notas con contenido idéntico, unos 10 minutos después de crearlas. Ya está corregido.
- Pendiente: integrar los 12 papers de `2. Sources/Papers/` en las sesiones de LPH y craneofacial. La carpeta vacía `5. Estadística/` se podría eliminar.

## [2026-10-06] schema | Skill de estudio `estudiemos`
- Creada `../.claude/skills/estudiemos/SKILL.md`: localiza la sesión, lee los capítulos enlazados, investiga con deep-research, escribe el resumen en la zona de notas (sin borrar lo del usuario), enseña con recuperación activa y casos, y programa repasos espaciados.
- `CLAUDE.md` actualizado: la skill cuenta como autorización expresa para escribir en la zona de notas de la sesión.

## [2026-10-06] schema | Skill `repasemos` y vista de repasos
- Creada `../.claude/skills/repasemos/SKILL.md`: busca las sesiones con `proximo_repaso` ≤ hoy, hace preguntas intercaladas y casos sin rehacer el resumen, califica cada sesión (Bien/Regular/Mal), reprograma y deja historial en la nota.
- `estudiemos` ahora escribe `ultimo_estudio`, `proximo_repaso` y `repasos` en el frontmatter, y `## Próximos repasos` con casillas; los repasos los deriva a `repasemos`.
- Creada la vista `Repasos.base` (Toca hoy · Próximos 7 días · Todas programadas · En curso), embebida en [[index]]. Definidos los tipos de propiedad en `.obsidian/types.json` (fechas y número).

## [2026-10-06] refactor | Sesiones numeradas por orden dentro del módulo
- A petición del usuario, las 682 sesiones se renombraron a `NN. Título.md` (orden dentro de su módulo), para que el orden de estudio se vea en el explorador de archivos.
- Se reescribieron todos los enlaces (índices de área, navegación Previous/Next, referencias ↗) en 701 archivos; 0 enlaces a sesiones rotos. Cada sesión tiene ahora `aliases: ["<título sin número>"]`.
- Generador (`_Sistema/generador/build.py`) actualizado para usar el mismo formato de nombre; `CLAUDE.md` y la skill `estudiemos` actualizados.
- Detectado: 4 libros reemplazados por versiones comprimidas con sufijo `_compressed` (Atlas de ATM, Sperber, CFM y TCS, Distracción osteogénica). Mismo número de páginas que los originales, pero el cambio de nombre rompe sus enlaces de fuentes hasta que recuperen el nombre original.

## [2026-10-06] refactor | Anatomía completa de cabeza y cuello + secciones que faltaban en Imaging
- **Anatomy** se rehízo de 23 a **54 sesiones** en 10 módulos: osteología y base de cráneo; cara, cuero cabelludo y músculos; cavidad oral; nariz, órbita y oído; vísceras y glándulas del cuello (faringe, laringe, tiroides/paratiroides/tráquea/esófago, glándulas salivales); fascias y regiones del cuello; arterias (carótidas, ramas de la ECA, maxilar, cara, subclavia/vertebral, oftálmica, polígono de Willis, vasos receptores); venas, meninges y senos durales; linfáticos (niveles y drenaje por subsitio); los 12 pares craneales por separado, plexos cervical y braquial y sistema autónomo.
- Las sesiones de anatomía anteriores estaban vacías (sin notas ni casillas); se regeneraron. Copia de seguridad en el scratchpad de la sesión.
- Fuentes: Iwanaga + capítulos de visión general de *Diagnostic Imaging: Head and Neck* + Carstens (vasos, nervios, músculos, fascias, meninges) + capítulos puntuales de otros libros. **Laguna:** no hay un tratado completo de anatomía de cabeza y cuello en la biblioteca; se avisa en el índice del área.
- **Imaging**: añadido el módulo 6 (6 sesiones: senos paranasales, órbita, base de cráneo, trauma de base de cráneo y cara, hueso temporal, ángulo pontocerebeloso/CAI). Esas secciones del libro no entraron en la primera versión del temario.
- Reparadas las referencias ↗ desde TMJ y Reconstructive; la antigua sesión "Arteries of the head and neck and recipient vessels" se dividió en sesiones arteriales y "Recipient vessels for microvascular head and neck reconstruction".
- Total: **719 sesiones**. Nuevo script `_Sistema/generador/make_index.py` para regenerar `index.md`.

## [2026-10-06] libro | Gray, Anatomía para estudiantes (cap. 8, Cabeza y cuello)
- Nuevo libro: `1. Gray Anatomia Para Estudiantes ( PDFDrive ).pdf` (1069 pp.). El capítulo 8 (PDF pp. 759–1032) está escaneado, sin texto. Los apartados se localizaron por las cabeceras de página, y los subtemas del cuello revisando las miniaturas. Página impresa = página del PDF − 11.
- Añadido como fuente principal en las 54 sesiones de Anatomy, con enlace a la página de cada apartado: cráneo, cavidad craneal, meninges, encéfalo e irrigación, nervios craneales, cara, cuero cabelludo, órbita, oído, fosas temporal/infratemporal y pterigopalatina, cuello (fascia, venas, triángulo anterior, sistema carotídeo, pares craneales, tiroides/paratiroides, triángulo posterior, plexos, raíz del cuello, simpático, linfáticos), faringe, laringe, cavidades nasales y cavidad oral.
- Área regenerada (seguía sin notas ni casillas). Se elimina el aviso de laguna del índice de Anatomy. `index.md` regenerado (32 libros).
- CLAUDE.md y la skill `estudiemos` documentan cómo leer páginas escaneadas.

## [2026-10-08] refactor | Compresión de los libros de `2. Sources/Libros`
- Con aprobación del usuario, 14 libros se sustituyeron por versiones comprimidas **con el mismo nombre de archivo** (las imágenes se recomprimieron, se eliminaron objetos y fuentes duplicados, se quitaron los metadatos XMP por objeto y, en AO y Dolor, los trazados vectoriales pesados). Se conservan las páginas, los marcadores y el texto, así que los enlaces `#page=N` siguen siendo válidos.
- Se quitó el sufijo `_compressed` a los 6 libros que había comprimido el usuario (Atlas ATM, Sperber, Microsomía, Distracción, Imaging, Apert).
- Biblioteca: de 5,1 GB a 1,5 GB. Siguen por encima de 70 MB: Medicina del Dolor (94), Murray (91), Gray (82, totalmente escaneado) y Posnick (347; por encima del límite de 100 MB de GitHub).
- Verificación: los 32 libros tienen el mismo número de páginas que en `_Sistema/generador/tocs/`; 0 enlaces rotos a libros; los 1167 enlaces `#page=` caen dentro de su libro.

## [2026-10-08] refactor | Posnick dividido en 6 volúmenes
- *Orthognathic Surgery: Principles and Practice* (347 MB comprimido) se dividió por capítulos en 6 PDFs de 54–65 MB (`… - Vol 1…6.pdf`), con sus marcadores. Las páginas son idénticas a las del libro completo (0 diferencias de texto y de píxeles en las muestras).
- Cortes (páginas del libro completo): 1–553 · 554–817 · 818–1105 · 1106–1307 · 1308–1574 · 1575–1819.
- Se reescribieron 47 enlaces en 42 archivos (bloques **Sources** de 35 sesiones y 6 índices de área); los 41 enlaces con página abren en el capítulo de su etiqueta. `index.md` se regeneró con `make_index.py`.
- Generador: `build.py` tiene ahora `VOLUMES`/`book_file()`; el temario y `tocs/` siguen usando las páginas del libro completo. Documentado en CLAUDE.md §5.
- El PDF completo se movió fuera de la bóveda, a `Documentos/Libros completos (fuera de la boveda)/`.
- Ya ningún libro pasa de 100 MB; la biblioteca ocupa 1,5 GB.

## [2026-10-08] schema | Libros fuera de git
- Se subieron los libros a GitHub, pero tardaban demasiado en descargarse en el móvil, así que se sacaron del historial: se quitaron los 4 commits de libros, se añadió `.gitignore` con `2. Sources/Libros/` y el usuario hizo el push forzado. GitHub queda en `790c80e`, sin ningún PDF de libros; `.git` local pasó de 1,4 GB a 44 MB.
- Los 37 PDF siguen en el disco y en OneDrive; las skills los leen del disco. Ajustes del repositorio: `core.longpaths=true` y `core.autocrlf=input`. Documentado en CLAUDE.md §7.
