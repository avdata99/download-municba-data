# Descarga completa de los datos del portal de datos abiertos de la Municipalidad de Córdoba

La Municipalidad de Córdoba publicó en su gestión de Gobierno Abierto 2016-2019 un portal de datos abiertos con un API que permite ver en tiempo real los datos que están abiertos.  

Este portal de datos abiertos es software libre y [puede verse en GitLab](https://gitlab.com/municipalidad-de-cordoba/Qhapax).  

Las llamadas API usadas para esta extracción son:
- Datos: https://gobiernoabierto.cordoba.gob.ar/api/datos-abiertos/
- Categorías: https://gobiernoabierto.cordoba.gob.ar/api/categorias-datos-abiertos/

Más sobre los datos [aquí](data.md).  

Descargar todo:

```
python3 download.py 
Downloading: https://gobiernoabierto.cordoba.gob.ar/api/datos-abiertos/ as json_pages/1.json ...

...

Dataset: Zonas catastrales
 - Version: Zonas catastrales
   - Recurso: SHP Zonas catastrales
     + Icon: map
     + URL: https://gobiernoabierto.cordoba.gob.ar/media/datos/zona.rar

...

Finalizado: 648 datasets, 2021 versiones y 6209 recursos

```
