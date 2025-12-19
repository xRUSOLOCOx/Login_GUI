# Login_GUI

Aplicación de interfaz gráfica de usuario para login construida con Flet.

**Estructura principal**
- `main.py` — punto de entrada de la aplicación.
- `components/` — componentes de UI (header, content, sign_in, sign_up, etc.).
- `controllers/` — lógica de control (navegación, contexto, transformaciones).
- `assets/` — imágenes, iconos, audio y video.

**Requisitos**
- Python 3.9+ (recomendado).
- Dependencias en `requirements.txt` (principalmente `flet`).

Instalación y ejecución (Windows `cmd.exe`):

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Notas:
- Si vas a desarrollar, activa tu entorno virtual antes de instalar dependencias.
- `.gitignore` ya incluye exclusiones para `__pycache__`, entornos virtuales y carpetas de editor.
- El proyecto usa un pequeño `app_context` para compartir `page` y `main_container` entre módulos.


