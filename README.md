# PEC2 - Convex Hull
PEC2 - Visualización de Datos - Data Science - UOC

## Autores
Julen

## Estructura del proyecto
+ /src/
    - main.py: archivo desde donde se ejecuta el código principal

+ /data/
    - data_links.txt: url de la fuente de datos

+ README.md: contiene informción útil respecto al proyecto, como quienes son sus autores o como se ejecuta.

+ requirements.txt:  librerías necesarias para ejecutar el código.

+ .gitignore: se añaden los archivos que no se quieren incluir en el repositorio

+ mapa_gull.html: archivo html resultante de ejecutar el código. Contiene la visualización convex hull

## Instalación

**Creación del entorno virtual**

En el terminal del proyecto se deberá poner el siguiente comando:

```shell
python -m venv venvgull
```

**Activación del entorno virtual**
```shell
venvgull\Scripts\activate
```

**Instalar requirements**
```shell
pip install -r requirements.txt
```

## Instrucciones para el Run

**Ejecución del main**
```shell
python src/main.py
```

**Antes de subir el codigo a git, hacer update del requirements.txt**
```shell
pip3 freeze > requirements.txt
```
