# Descarga completa de los datos del portal de datos abiertos de la Municipalidad de Córdoba

La Municipalidad de Córdoba publicó en su gestión de Gobierno Abierto 2016-2019 un portal de datos abiertos con un API que permite ver en tiempo real los datos que están abiertos.  

Este portal de datos abiertos es software libre y [puede verse en GitLab](https://gitlab.com/municipalidad-de-cordoba/Qhapax).  

Las llamadas API usadas para esta extracción son:
- Datos: https://gobiernoabierto.cordoba.gob.ar/api/datos-abiertos/
- Categorías: https://gobiernoabierto.cordoba.gob.ar/api/categorias-datos-abiertos/

Más sobre los datos [aquí](data.md).  

## Requerimientos

Se requiere python 3 y la'instalacion de los requerimientos

```
pip install -r requirements.txt
```

Descargar todo:

```
python3 download.py 
Downloading: https://gobiernoabierto.cordoba.gob.ar/api/datos-abiertos/ as json_pages/1.json ...

...

Dataset: Bono internacional
 - Version: INFORME DE SALDOS Y APLICACIÓN DE FONDOS BONO INTERNACIONAL 2016 A ABRIL DE 2017
   - Recurso: Anexos Informe Crédito Internacional
     + Icon: xlsx
     + URL: https://gobiernoabierto.cordoba.gob.ar/media/datos/Anexos_Informe_Credito_Internacional_A_Abrilvf.xlsx
Downloading Bono internacional---INFORME DE SALDOS Y APLICACIÓN DE FONDOS BONO INTERNACIONAL 2016 A ABRIL DE 2017---Anexos Informe Crédito Internacional.xlsx from https://gobiernoabierto.cordoba.gob.ar/media/datos/Anexos_Informe_Credito_Internacional_A_Abrilvf.xlsx


...

Finalizado: 648 datasets, 2021 versiones y 6209 recursos

```

Son 5.441 archivos, 2,2 GB.  Quedan subidos a [esta carpeta de Google Drive](https://drive.google.com/drive/folders/1VL1ciK50NzdQ31JiPzSl-oskCWtaHy2g?usp=sharing).  
