"""
Descargar todos los datos del portal municipal de datos abiertos de la Ciudad de Córdoba, Argentina
"""
import logging
import json
import os
import requests
import sys
from slugify import slugify


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


# ----------- DESCARAGR LOS METADATOS
base_url = 'https://gobiernoabierto.cordoba.gob.ar'
data_url = '/api/datos-abiertos/'
save_pages_to = 'json_pages'
next_data = base_url + data_url

full_datasets = []
# los tipos de datos se infieren por el campo "icon" de los recursos
icons = set()  # tipos de datos. Para saber si son descargables
# no es exacto pero estos serían los descargables (otros son referencias a web externas, repositorios de github, etc)
allowed_download_icons = ['json', 'ods', 'image', 'jpeg', 'kmz', 'csv', 'pdf', 'shp', 'docx', 'doc', 'kml', 'xls', 'xlsx', 'jpg', 'txt', 'zip']
datasets = 0
versiones = 0
recursos = 0

c = 0
while next_data:
    c += 1
    cache = os.path.join(save_pages_to, f'{c}.json')
    if os.path.isfile(cache):
        f = open(cache, 'r')
        data = json.load(f)
        f.close()
        logger.info(f'Already exists: {cache}')
    else:
        logger.info(f'Downloading: {next_data} as {cache} ...')
        response = requests.get(next_data)
        data = response.json()
        f = open(cache, 'w')
        f.write(json.dumps(data, indent=4))
        f.close()

    for dataset in data['results']:
        datasets += 1
        full_datasets.append(dataset)
        logger.info('Dataset: {}'.format(dataset['titulo']))
        # versiones del dataset
        for version in dataset['versiones']:
            versiones += 1
            logger.info(' - Version: {}'.format(version['titulo']))
            # cada version puede estar en varios formatos (llamados _recursos_)
            for recurso in version['recursos']:
                recursos += 1
                logger.info('   - Recurso: {}'.format(recurso['titulo']))
                icon = recurso['icon']
                logger.info('     + Icon: {}'.format(icon))
                icons.add(icon)
                if recurso['url'] is not None:
                    url = recurso['url'] if recurso['url'].startswith('http') else base_url + recurso['url']
                else:
                    url = None
                logger.info('     + URL: {}'.format(url))

                # ver si es algo decargable
                if url and icon in allowed_download_icons:
                    # que lastima que no hay IDs ...
                    no_unique_name = '{}---{}---{}.{}'.format(dataset['titulo'], version['titulo'], recurso['titulo'], icon)
                    dest = 'data/{}'.format(slugify(no_unique_name))
                    if os.path.isfile(dest):
                        logger.info(f'Already downloaded {no_unique_name} from {url}')
                        continue
                    logger.info(f'#### DOWNLOADING {no_unique_name} from {url}')
                    data_response = requests.get(url, allow_redirects=True)
                    f = open(dest, 'wb')
                    f.write(data_response.content)
                    f.close()

    next_data = data['next']
    logger.info('###################')
    logger.info(f'Procesados: {datasets} datasets, {versiones} versiones y {recursos} recursos')
    logger.info('###################')

logger.info(f'Finalizado: {datasets} datasets, {versiones} versiones y {recursos} recursos')
logger.info(f'Icons {icons}')