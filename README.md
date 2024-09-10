# Generador de Números Aleatorios

Este es un proyecto Flask que permite generar números aleatorios de diferentes distribuciones (Uniforme, Exponencial y Normal), visualizar los resultados en un histograma y guardar las imágenes generadas.

## Requisitos

Antes de ejecutar la aplicación, asegúrese de tener instalados los siguientes paquetes:

- Python 3.x
- pip

## Instalación

Siga estos pasos para configurar y ejecutar la aplicación en un entorno virtual (venv).

### En Windows

1. **Crear un entorno virtual**:
python -m venv venv

2. **Activar el entorno virtual**:
.\venv\Scripts\activate

3. **Instalar las dependencias**:
pip install -r requirements.txt

3. **Ejecutar la aplicación Flask**:
python main.py

### En Linux

1. **Crear un entorno virtual**:
python3 -m venv venv

2. **Activar el entorno virtual**:
source venv/bin/activate

3. **Instalar las dependencias**:
pip install -r requirements.txt

3. **Ejecutar la aplicación Flask**:
python main.py

## Uso

Abra su navegador web y vaya a http://127.0.0.1:5000/ o http://localhost:5000/.
Rellene los parámetros en el formulario de la página principal.
Seleccione la distribución que desea generar y haga clic en "Generar".
Visualice los resultados en la página de distribución, donde podrá ver el histograma y, si lo seleccionó, los valores generados.

## Notas

Asegúrese de que la carpeta static tenga permisos de escritura, ya que las imágenes de los histogramas se guardarán en esta carpeta.
Si encuentra algún error o problema, revise los mensajes de error en la consola y ajuste los parámetros según sea necesario.