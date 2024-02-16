# TECH READ QA TEAM

¡Excelente! Vamos a comenzar paso a paso.

Aquí hay una guía básica para configurar un proyecto Python con Visual Studio Code, Pytest, y asegurándonos de que sea compatible con macOS y Windows.

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

## Paso 6: Configurar Pytest en Visual Studio Code
1. Asegúrate de tener la extensión "Python Test Explorer for Visual Studio" instalada desde la pestaña de Extensions.
2. Abre el menú "View" > "Command Palette" y escribe "Python Test Explorer: Discover Tests".
3. Configura el archivo de configuración pytest.ini o setup.cfg según tus necesidades. Puedes dejarlo vacío por ahora y configurarlo más tarde.

## Paso 7: Prueba de Ejecución con Pytest
Crea algunos tests en tu proyecto y ejecútalos utilizando el explorador de pruebas de Visual Studio Code.

Con estos pasos, deberías tener un entorno de desarrollo básico configurado en macOS. Repite los pasos en Windows, asegurándote de utilizar barras invertidas `\` en lugar de barras diagonales `/` en los comandos de terminal. Además, ten en cuenta las diferencias de configuración para rutas y activación de entornos virtuales en Windows.