# TECH READ QA TEAM

Esta es una guía básica para configurar un proyecto Python con Visual Studio Code, Pytest, y asegurándonos de que sea compatible con macOS y Windows.

## Paso 1: Clonar el Repositorio

Clona tu repositorio desde GitHub a tu máquina local utilizando el siguiente comando en tu terminal:

```sh
git clone https://github.com/tu_usuario/tu_proyecto.git
```

## Paso 2: Abrir el Proyecto en Visual Studio Code
Abre Visual Studio Code y selecciona "File" > "Open Folder". Navega hasta la carpeta de tu proyecto y ábrela.

## Paso 3: Configurar el Entorno Virtual (Recomendado)
Es una buena práctica utilizar entornos virtuales para cada proyecto. Abre la terminal en Visual Studio Code e ingresa los siguientes comandos:

```sh
cd tech-red-qa
python3 -m venv venv
```

Luego, activa el entorno virtual:

En macOS/Linux:

```sh
source venv/bin/activate
```

En Windows:
```sh
venv\Scripts\activate
```

## Paso 4: Instalar Dependencias
Instala las dependencias necesarias, como pytest, usando pip:

```sh
pip install -r requirements.txt
```

## Paso 5: Configurar el Interprete de Python en Visual Studio Code
1. Abre la pestaña de Extensions en la barra lateral (icono de paquete cuadrado) y busca e instala la extensión "Python" de Microsoft.
2. Abre el menú "View" > "Command Palette" (o presiona Cmd + Shift + P en macOS o Ctrl + Shift + P en Windows/Linux) y escribe "Python: Select Interpreter".
3. Selecciona el intérprete Python del entorno virtual que creaste en el paso 3 (tu_proyecto/venv/bin/python en macOS o tu_proyecto\venv\Scripts\python.exe en Windows).

## Paso 6: Configurar la raíz del proyecto
Debemos agregar el directorio de la raíz del proyecto a la variable de entorno PYTHONPATH.

1. Añade el directorio raíz del proyecto a PYTHONPATH:
   - Abre la terminal de Visual Studio Code.
   - Ejecuta el siguiente comando para agregar el directorio raíz del proyecto a la variable de entorno PYTHONPATH:

```sh
export PYTHONPATH=/Users/TU_USER/Documents/technocrat_repositories/CrossQualityTeam/tech-red-qa
```

2. Ejecuta pytest:

Ejecuta tus pruebas desde el terminal de Visual Studio Code. Puedes usar el siguiente comando:
```sh
pytest tests/
```
<img width="1026" alt="pytest_test" src="https://github.com/PlatformUnityCI/cross-quality-ci/assets/9554315/4568e2a9-a390-48cf-83ca-a3d87c2bb8cf">