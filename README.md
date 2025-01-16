# ChatBot Supremo

ChatBot Supremo es una aplicación de chat impulsada por IA mediante el uso de la API de OpenAI para el reconocimiento de lenguaje natural en el contexto del mercado inmobiliario. Esta aplicación fue desarrollada en la Hackatón organizada por el equipo de TOCTOC, una empresa líder en soluciones tecnológicas para el sector inmobiliario en América Latina. La aplicación está desarrollada utilizando Python, Flask, JavaScript, entre otras tecnologías.

## Requisitos 

Para ejecutar este proyecto asegúrate de tener lo siguiente instalado en la máquina:
- **Python** (v3.13.1 o superior). Puedes verificar tu version con: 

    ```bash
     python --version
     ```

**Nota:**  El proyecto está diseñado para ejecutarse con las versiones mencionadas. No se garantiza la compatibilidad con versiones anteriores.

## ¿Cómo ejecutar este proyecto?

Sigue los pasos a continuación para clonar y ejecutar el proyecto en tu entorno local:

**Nota:** La ejecucion de los comandos siguientes deben realizarce en la raíz del proyecto a excepcion del paso 1.

Una vez realizados estos pasos por primera vez para volver a ejecutar la aplicacion se requiere realizar los pasos 3, 5 y 6. Estos pasos deben realizarse siempre en el directorio raiz del proyecto.

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Dagt07/hackaton-toctoc.git
    cd hackaton-toctoc
    ```
2. **Crear un ambiente de python:**

    ```bash
    python -m venv venv
    ```
3. **Activar el ambiente de python (utilizando powershell):**

    ```bash
    .\venv\Scripts\Activate.ps1
    ```
4. **Instalar las dependencias:** 

    ```bash
    pip install -r requirements.txt
    ```
5. **Creación de archivo .env:** Este archivo se utiliza para almacenar la clave con la que se va a hacer la conexión a la API de OpenAI. Cambia `inserte_la_llave` por tu OpenAI Key real.

    ```bash
    echo "OPENAI_KEY=inserte_la_llave" > .env
    ```
6. **Ejecutar el proyecto:** Inicia el servidor de desarrollo con el siguiente comando:

    ```bash
    python .\src\app.py
    ```
7. **Acceder a la aplicación:** Abre tu navegador y dirígete a http://127.0.0.1:5000. (El puerto puede variar si el 5000 no está disponible).



