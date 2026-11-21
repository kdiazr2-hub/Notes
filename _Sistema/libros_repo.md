---
tipo: sistema
actualizado: 2026-11-21
---
# Conexión con el repositorio de libros

Desde el 2026-11-21 el temario (`3. Notes`) se construye **solo** con los 25 libros del repositorio de GitHub **`kdiazr2-hub/libros`**. Los enlaces de las sesiones usan **exactamente el mismo nombre de archivo** que tienen allí, por ejemplo:

`[[Facial Trauma Surgery From Primary Repair to Reconstruction - Dorafshar, Rodriguez & Manson (2020).pdf#page=162|…]]`

## En el ordenador (Obsidian)
`2. Sources/Libros/` no va en git. Para que los enlaces abran, esa carpeta debe tener los 25 PDF con esos nombres. Lo más sencillo es descargar el repositorio de libros y copiar sus PDF ahí (sin la carpeta `contenido/`, que no hace falta en Obsidian).

## En una sesión en la nube
1. Añadir el repositorio a la sesión (`add_repo` kdiazr2-hub/libros) y clonarlo junto a la bóveda.
2. El nombre del PDF en el bloque **Sources** es el mismo que en el repositorio.
3. Leer solo las páginas del capítulo: `contenido/<nombre>.txt`, donde **la página N del PDF es `texto.split('\f')[N-1]`**; o pypdf sobre el PDF si hacen falta figuras.

## Claves del generador (`_Sistema/generador/build.py`)

| Clave | Libro |
|---|---|
| IWANAGA | Atlas of Oral and Maxillofacial Anatomy - Iwanaga & Tubbs (2021) |
| SALYER1 | Atlas of Craniofacial and Cleft Surgery Vol I Craniofacial Surgery - Salyer & Bardach (2008) |
| SALYER2 | Atlas of Craniofacial and Cleft Surgery Vol II Cleft Lip and Palate Surgery - Salyer & Bardach (2008) |
| KATZUNG | Basic and Clinical Pharmacology 14th Ed - Katzung (2018) |
| RIUS | Bioestadística Métodos y aplicaciones - Ríus Díaz & Barón López |
| ORELLANA | Bioestadística aplicada a investigaciones científicas en salud - Orellana & Cañarte (2022) |
| ALONSO | Cleft Lip and Palate Treatment A Comprehensive Guide - Alonso & Raposo-Amaral (2018) |
| SKULLBASE | Cranial, Craniofacial and Skull Base Surgery - Cappabianca, Califano & Iaconetta (2010) |
| SPERBER | Craniofacial Development - Sperber (2001) |
| MCCARTHY | Craniofacial Distraction - McCarthy (2017) |
| CFM_TCS | Craniofacial Microsomia and Treacher Collins Syndrome - Yates & Markiewicz (2022) |
| THALLER | Craniofacial Surgery - Thaller, Bradley & Garri (2008) |
| CCNOTES | Critical Care Notes Clinical Pocket Guide - Jones & Fix (2009) |
| JIMENEZ | Endoscopic Craniosynostosis Surgery An Illustrated Guide to Endoscopic Techniques - Jimenez (2023) |
| REYNEKE | Essentials of Orthognathic Surgery 3rd Ed - Reyneke (2022) |
| MARIK | Evidence-Based Critical Care 3rd Ed - Marik (2015) |
| TRAUMA | Facial Trauma Surgery From Primary Repair to Reconstruction - Dorafshar, Rodriguez & Manson (2020) |
| FERRARO | Ferraro's Fundamentals of Maxillofacial Surgery 2nd Ed - Taub, Patel, Buchman & Cohen (2015) |
| PERRY | Manual of Operative Maxillofacial Trauma Surgery - Perry & Holmes (2014) |
| SINGH | Maxillofacial Trauma A Clinical Guide - Singh & Sharma (2021) |
| CSO | Neurosurgical Aspects of Craniosynostosis - Di Rocco & Kestle (2024) |
| SECRETS | Oral and Maxillofacial Surgery Secrets 3rd Ed - Abubaker (2016) |
| FRAGISKOS | Oral Surgery - Fragiskos (2007) |
| MOORE | Principles of Oral and Maxillofacial Surgery 6th Ed - Moore (2011) |
| ELLIS | Surgical Approaches to the Facial Skeleton 3rd Ed - Ellis & Zide (2019) |

## Nombres anteriores en la bóveda
10 de estos libros ya estaban en `2. Sources/Libros/` con otro nombre (mismo PDF, mismas páginas). Si los tienes así en el ordenador, basta con renombrarlos:

| Nombre anterior | Nombre actual |
|---|---|
| `1. Craniofacial Development and Growth (Craniofacial Development).pdf` | `Craniofacial Development - Sperber (2001).pdf` |
| `1. Craniofacial microsomia and treacher collins syndrome.pdf` | `Craniofacial Microsomia and Treacher Collins Syndrome - Yates & Markiewicz (2022).pdf` |
| `1. Neurosurgical Aspects of Craniosynostosis (Springer Nature Switzerland) - libgen.li.pdf` | `Neurosurgical Aspects of Craniosynostosis - Di Rocco & Kestle (2024).pdf` |
| `1. Trauma facial.pdf` | `Facial Trauma Surgery From Primary Repair to Reconstruction - Dorafshar, Rodriguez & Manson (2020).pdf` |
| `2. Cranial, craniofacial and skull base surgery.pdf` | `Cranial, Craniofacial and Skull Base Surgery - Cappabianca, Califano & Iaconetta (2010).pdf` |
| `2. Oral Surgery.pdf` | `Oral Surgery - Fragiskos (2007).pdf` |
| `3. Bioestadistica.pdf` | `Bioestadística Métodos y aplicaciones - Ríus Díaz & Barón López.pdf` |
| `3. Johan P. Reyneke - Essen 3 edicion.pdf` | `Essentials of Orthognathic Surgery 3rd Ed - Reyneke (2022).pdf` |
| `6. Iwanaga Tubbs - Atlas of Oral and Maxillofacial Anatomy.pdf` | `Atlas of Oral and Maxillofacial Anatomy - Iwanaga & Tubbs (2021).pdf` |
| `Basic and Clinical Pharmacology.pdf` | `Basic and Clinical Pharmacology 14th Ed - Katzung (2018).pdf` |
