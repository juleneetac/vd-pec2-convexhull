# practica1-webscraping
Reto 2 - Práctica 1- Tipología y ciclo de vida de los datos - Data Science - UOC

## Autores
Julen Garralaga

Sandra Ros

## Estructura del proyecto
+ /src/
    - main.py: archivo desde donde se ejecuta el archivo scraper_ovio.py
    - scraper_ovio.py: contiene las funciones que se encargan de hacer el scraping

+ /data/
    - output_dataset.csv: csv resultante tras aplicar el scraping

+ README.md: contiene informción útil respecto al proyecto, como quienes son sus autores o como se ejecuta.

+ requirements.txt:  librerías necesarias para ejecutar el código.

+ .gitignore: se añaden los archivos que no se quieren incluir en el repositorio

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

**Nota**: Para la función "get_products()" se establece un m¡valor de max_pages = 10 por defecto, este parámetro puede ser modificado en caso de que la categoría que se vaya a buscar, tiene más de 10 páginas.

**Antes de subir el codigo a git, hacer update del requirements.txt**
```shell
pip3 freeze > requirements.txt
```

## DOI de Zenodo

El DOI de Zenodo se encuentra en el siguiente enlace:
https://doi.org/10.5281/zenodo.14048084
