# Configurar un flujo CI/CD con GitHub Actions para tu proyecto

Para configurar un flujo de CI/CD con GitHub Actions para tu proyecto, sigue estos pasos:

## 1. Crear la ruta donde se alojarán el workflow de ci-cd.yml
Desde la terminal de Visual Studio, drea la carpeta `.github` en la raíz de tu proyecto:
```sh
mkdir .github
```

## 2. Dentro de .github, crea una carpeta workflows y un archivo YAML para tu flujo de trabajo (por ejemplo, ci-cd.yml):
```sh
mkdir .github/workflows
touch .github/workflows/ci-cd.yml
```
Bien, ahora la estructura de directorios para alojar todos los archivos `.yml` está creado:

```sh
tech-red-qa/
│
└── .github/
    └── workflows/
        └── ci-cd.yml
```

## 3. Edita el archivo ci-cd.yml con la siguiente configuración básica:
Este flujo de trabajo se ejecutará en cada push a la rama principal y realizará las siguientes acciones:

- Descargar el repositorio.
- Configurar Python.
- Instalar las dependencias especificadas en requirements.txt.
- Ejecutar los tests utilizando pytest.

```sh
name: CI/CD Pipeline

on:
  push:
    branches:
      - tech-red-qa-github-action

jobs:
      # Define un trabajo llamado build
  build:
    runs-on: ubuntu-latest

    steps:
      # Paso 1: Obtener el contenido del repositorio
      - name: Checkout repository
        uses: actions/checkout@v4

      # Paso 2: Configurar Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.X
          architecture: 'x64'

      # Paso 3: Instalar las dependencias
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # Paso 4: Configurar la variable de entorno PythonPath
      - name: Configure Python Path
        run: echo "PYTHONPATH=${{ github.workspace }}/tech-red-qa" >> $GITHUB_ENV

      # Paso 5: Instalar el proyecto
      - name: Install Project
        run: |
          python -m pip install -e .

      # Paso 6: Ejecutar las pruebas con Pytest
      - name: Run tests
        run: |
          cd ${{ github.workspace }}/tests
          pytest labs/test_foo.py

```

## 4. Configuración del requirements.txt

Asegúrate de que tu `requirements.txt` incluya pytest (_colocando solo `pytest` conseguirás que se instale la última versión disponible_)

```sh
pytest
```

## 5. Pushear los cambios al remoto

Añade, haz commit y empuja los cambios.

Esto configurará un flujo de trabajo simple que ejecutará tus pruebas en cada push a la rama principal. Puedes personalizar este archivo YAML según tus necesidades y agregar más pasos, como la construcción de distribuciones, despliegues, etc.

```sh
git add .github/workflows/ci-cd.yml
git commit -m "Añadir flujo de CI/CD con GitHub Actions"
git push origin main
```
