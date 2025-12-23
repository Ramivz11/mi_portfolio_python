# 📉 Bot de Rastreo de Precios - MercadoLibre Argentina

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Estado](https://img.shields.io/badge/Estado-Funcional-green)

Este proyecto es una herramienta de automatización escrita en **Python** que monitorea el precio de productos específicos en MercadoLibre Argentina. Su objetivo es detectar bajadas de precio y generar un historial de datos para análisis.

## 🚀 Funcionalidades Clave

* **Web Scraping Ético:** Extrae datos simulando un navegador real (User-Agent) para evitar bloqueos.
* **Extracción de Metadatos:** Utiliza metadatos SEO ocultos para obtener precios precisos y evitar errores de formato visual.
* **Persistencia de Datos:** Guarda automáticamente cada consulta en un archivo `CSV` (Excel), registrando fecha, hora, título y precio.
* **Automatización:** Script configurado con la librería `schedule` para ejecutarse automáticamente en intervalos definidos (ej. diariamente a las 10:00 AM).

## 🛠️ Tecnologías Utilizadas

* **Python 3**: Lenguaje principal.
* **BeautifulSoup4**: Para el parseo de HTML y extracción de datos.
* **Requests**: Para las peticiones HTTP.
* **Schedule**: Para la planificación de tareas (Jobs).
* **CSV & Datetime**: Librerías estándar para manejo de archivos y fechas.

## ⚙️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/](https://github.com/)[TU_USUARIO]/mi_portfolio_python.git
   cd mi_portfolio_python