"Eres un profesor que solo tiene 4 horas conmigo y nunca volverá a verme. Tu único objetivo es hacerme funcional en [HABILIDAD] antes de que se acabe el tiempo.
No me den teoría sin uso práctico. No me den una lista.
Dime qué aprender primero, qué ignorar por completo, y qué ejercicio, si lo hago una sola vez, ya me pone por delante del 70% de las personas que llevan meses
estudiando esto."

"No me expliques [CONCEPTO]. Ponme directo en una situación real donde tendría que usarlo y probablemente me equivoque. Cuando me equivoque, no me den la respuesta. Hazme una pregunta que me obligue a encontrar dónde está roto mi razonamiento. Solo dame la respuesta después de que lo intente al menos dos veces.
Repite el ciclo hasta que lo haga bien sin dudar."

"Este contenido me confunde. Antes de explicarlo, dime cuál es la única frase que, si la entiendo, hace que el resto tenga sentido solo. Explica solo esa frase primero. Usa una analogía cotidiana, sin tecnicismos. Luego hazme 3 preguntas que solo alguien que de verdad entendió podría responder. No sigas hasta que pase las tres.
[Pega el contenido aquí]"

"Mi objetivo real es [OBJETIVO]. No es aprender [HABILIDAD] en general. Es lograr [RESULTADO ESPECÍFICO] en [PLAZO]. Ya sé [LO QUE YA DOMINAS]. Con eso, créame una ruta de 7 días. Cada día con una sola tarea de máximo 45 minutos, un criterio claro para saber si quedó bien hecha, y qué no hacer ese día para no perder tiempo. Si la ruta completa no me lleva al objetivo, reconstrúyela hasta que
sí lo haga."

"Creo que ya domino [HABILIDAD]. Quiero que me demuestres que estoy equivocado. Hazme 5 preguntas que parezcan simples pero que expongan los vacíos de alguien que nunca profundizó de verdad. Por cada respuesta, dime qué revela sobre lo que aún me falta en la base. No seas condescendiente. Si estoy siendo superficial, dímelo directo."

"Acabo de estudiar [TEMA]. Voy a explicar lo que entendí como si fueras un niño de 10 años. Mientras explico, deténme cada vez que use jerga sin saber qué significa, salte un paso en el razonamiento o simplifique tanto que quede incorrecto. Al final, dime exactamente qué revelan esos errores sobre lo que todavía no tengo sólido."

Entorno:
MI ENTORNO LOCAL DE DESARROLLO DE IA

HARDWARE
- ASUS TUF Gaming F15
- CPU: Intel Core i5-11400H, 6 núcleos / 12 hilos
- RAM: 32 GB
- GPU: NVIDIA GeForce RTX 3050 Laptop
- VRAM: 4 GB
- Windows 11
- Aproximadamente 1.4 TB de almacenamiento

ENTORNO
- Python 3.12.10
- Entorno virtual:
  C:\AI\environments\scientific-ai
- VS Code
- Git
- Ollama
- CUDA funcionando correctamente con PyTorch
- PyTorch 2.11.0 + CUDA 12.8
- torch.cuda.is_available() = True

ESTRUCTURA
C:\AI\
├── environments\
│   └── scientific-ai\
├── projects\
├── datasets\
├── models\
└── notebooks\

MODELOS LOCALES / OLLAMA
- Qwen 3.5 9B
- Qwen 2.5 3B
- Modelos Gemma instalados
- Ollama disponible como API/backend local
- Puedo añadir EmbeddingGemma para RAG si el proyecto lo necesita

DEEP LEARNING / IA
- PyTorch
- torchvision
- torchaudio
- Hugging Face Transformers
- datasets
- accelerate
- safetensors
- huggingface-hub

VISIÓN ARTIFICIAL
- OpenCV 5
- Ultralytics / YOLO
- MediaPipe
- Pillow
- scikit-image
- Albumentations

CIENCIA / MATEMÁTICAS
- NumPy
- SciPy
- SymPy
- Pandas
- scikit-learn
- Matplotlib
- JupyterLab

DOCUMENTOS / RAG
- PyMuPDF
- PyPDF
- python-docx
- openpyxl
- ChromaDB
- Pydantic

IMAGEN MÉDICA
- pydicom
- SimpleITK

CAPACIDADES QUE QUIERO PRIORIZAR
- Inteligencia artificial aplicada a medicina
- Cirugía maxilofacial y craneofacial
- Análisis facial
- Detección de landmarks
- Procesamiento de fotografías clínicas
- Computer vision
- Machine learning y deep learning
- Entrenamiento de modelos propios
- Análisis de DICOM/CT/CBCT
- Matemáticas, geometría y física
- Lectura y análisis de PDFs/artículos/libros
- RAG científico
- Aplicaciones con LLM locales
- Idiomas
- Automatización
- Aplicaciones científicas

LIMITACIONES IMPORTANTES
- Solo tengo 4 GB de VRAM.
- Priorizar modelos pequeños/eficientes.
- Usar ROI y reducir resolución cuando sea posible.
- Evitar cargar varios modelos grandes simultáneamente.
- CPU y 32 GB RAM pueden complementar la GPU.
- Para entrenamientos grandes puedo considerar GPU cloud.

Cuando te describa una nueva aplicación que quiero crear:
1. analiza si puedo hacerla con los recursos anteriores;
2. dime qué componentes existentes conviene reutilizar;
3. recomienda la arquitectura;
4. dime si necesito instalar algo adicional;
5. evita recomendar dependencias que ya tengo;
6. prioriza soluciones que funcionen bien con 4 GB de VRAM;
7. separa IA/ML de algoritmos determinísticos cuando estos sean más precisos;
8. si hay varias alternativas, recomiéndame la más apropiada para mi hardware;
9. dime qué debería ejecutarse localmente y qué, si algo, sería mejor ejecutar en cloud;
10. propón una estructura de proyecto dentro de C:\AI\projects.
