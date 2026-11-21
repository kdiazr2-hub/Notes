---
tipo: sistema
actualizado: 2026-11-21
---
# Conexión con el repositorio de libros

Los PDF de `2. Sources/Libros/` no están en git (ver CLAUDE.md §7), así que **en una sesión en la nube no existen**. En ese caso, los libros se leen del repositorio de GitHub **`kdiazr2-hub/libros`**.

Qué hay en ese repositorio:
- Los PDF, con su **título original** (título - autores (año)).
- `contenido/<mismo nombre>.txt`: el texto completo de cada libro. Las páginas están separadas por un salto de página (`\f`), así que **la página N del PDF es `texto.split('\f')[N-1]`**. Los enlaces `#page=N` de las sesiones sirven tal cual.
- `ESTUDIO.md`: una ficha de cada libro (temas, estructura y puntos clave).

## Cómo usarlo en una sesión en la nube
1. Añadir el repositorio a la sesión (`add_repo` kdiazr2-hub/libros) y clonarlo junto a la bóveda.
2. Traducir el nombre del libro que aparece en el bloque **Sources** de la sesión con la tabla de abajo.
3. Leer solo las páginas del capítulo: con `contenido/*.txt` (lo más rápido) o con pypdf sobre el PDF si hacen falta figuras.
4. Escribir las notas en la sesión de la bóveda, como siempre (skill `estudiemos`). **Los enlaces de la bóveda no se cambian**: siguen apuntando al nombre local del PDF.

## Libros que están en los dos sitios
Mismo libro y mismo número de páginas (comprobado el 2026-11-21), así que los `#page=N` coinciden.

| Nombre en la bóveda (`2. Sources/Libros/`) | Nombre en `kdiazr2-hub/libros` | Págs. |
|---|---|---|
| `1. Craniofacial Development and Growth (Craniofacial Development).pdf` | `Craniofacial Development - Sperber (2001).pdf` | 218 |
| `1. Craniofacial microsomia and treacher collins syndrome.pdf` | `Craniofacial Microsomia and Treacher Collins Syndrome - Yates & Markiewicz (2022).pdf` | 523 |
| `1. Neurosurgical Aspects of Craniosynostosis (Springer Nature Switzerland) - libgen.li.pdf` | `Neurosurgical Aspects of Craniosynostosis - Di Rocco & Kestle (2024).pdf` | 1127 |
| `1. Trauma facial.pdf` | `Facial Trauma Surgery From Primary Repair to Reconstruction - Dorafshar, Rodriguez & Manson (2020).pdf` | 585 |
| `2. Cranial, craniofacial and skull base surgery.pdf` | `Cranial, Craniofacial and Skull Base Surgery - Cappabianca, Califano & Iaconetta (2010).pdf` | 352 |
| `2. Oral Surgery.pdf` | `Oral Surgery - Fragiskos (2007).pdf` | 369 |
| `3. Bioestadistica.pdf` | `Bioestadística Métodos y aplicaciones - Ríus Díaz & Barón López.pdf` | 322 |
| `3. Johan P. Reyneke - Essen 3 edicion.pdf` | `Essentials of Orthognathic Surgery 3rd Ed - Reyneke (2022).pdf` | 321 |
| `6. Iwanaga Tubbs - Atlas of Oral and Maxillofacial Anatomy.pdf` | `Atlas of Oral and Maxillofacial Anatomy - Iwanaga & Tubbs (2021).pdf` | 170 |
| `Basic and Clinical Pharmacology.pdf` | `Basic and Clinical Pharmacology 14th Ed - Katzung (2018).pdf` | 1265 |

Los otros 22 libros de la bóveda (Posnick, Neville, Gray, AO, Berkowitz…) **no están** en el repositorio de libros: en la nube no se pueden leer.

## Libros que solo están en el repositorio de libros
Todavía no forman parte del temario: ninguna sesión los cita en **Sources**. Para estudiarlos por sesión hay que añadirlos primero (CLAUDE.md §4.2).

| Libro (`kdiazr2-hub/libros`) | Págs. | Áreas probables |
|---|---|---|
| Atlas of Craniofacial and Cleft Surgery Vol I Craniofacial Surgery - Salyer & Bardach (2008) | 443 | Craniofacial Surgery · Orthognathic Surgery |
| Atlas of Craniofacial and Cleft Surgery Vol II Cleft Lip and Palate Surgery - Salyer & Bardach (2008) | 457 | Cleft Lip and Palate |
| Bioestadística aplicada a investigaciones científicas en salud - Orellana & Cañarte (2022) | 238 | Biostatistics |
| Cleft Lip and Palate Treatment A Comprehensive Guide - Alonso & Raposo-Amaral (2018) | 396 | Cleft Lip and Palate |
| Craniofacial Distraction - McCarthy (2017) | 234 | Craniofacial Surgery · Orthognathic Surgery |
| Craniofacial Surgery - Thaller, Bradley & Garri (2008) | 419 | Craniofacial Surgery |
| Critical Care Notes Clinical Pocket Guide - Jones & Fix (2009) | 238 | Critical Care |
| Endoscopic Craniosynostosis Surgery An Illustrated Guide to Endoscopic Techniques - Jimenez (2023) | 269 | Craniofacial Surgery |
| Evidence-Based Critical Care 3rd Ed - Marik (2015) | 836 | Critical Care |
| Ferraro's Fundamentals of Maxillofacial Surgery 2nd Ed - Taub, Patel, Buchman & Cohen (2015) | 500 | Facial Trauma · Orthognathic Surgery |
| Manual of Operative Maxillofacial Trauma Surgery - Perry & Holmes (2014) | 180 | Facial Trauma |
| Maxillofacial Trauma A Clinical Guide - Singh & Sharma (2021) | 468 | Facial Trauma |
| Oral and Maxillofacial Surgery Secrets 3rd Ed - Abubaker (2016) | 557 | Oral Surgery (y repaso general) |
| Principles of Oral and Maxillofacial Surgery 6th Ed - Moore (2011) | 358 | Oral Surgery |
| Surgical Approaches to the Facial Skeleton 3rd Ed - Ellis & Zide (2019) | 444 | Facial Trauma · Anatomy |

*Craniofacial Distraction* (McCarthy, 234 págs.) **no es** el mismo libro que `1. Distracción osteogenica del esqueleto facial.pdf` (605 págs.).
