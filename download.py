"""
Descargar todos los datos del portal municipal de datos abiertos de la Ciudad de Córdoba, Argentina
"""
import logging
import json
import os
import requests
import sys


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
                logger.info('     + Icon: {}'.format(recurso['icon']))
                if recurso['url'] is not None:
                    url = recurso['url'] if recurso['url'].startswith('http') else base_url + recurso['url']
                else:
                    url = None
                logger.info('     + URL: {}'.format(url))
                

    next_data = data['next']


logger.info(f'Finalizado: {datasets} datasets, {versiones} versiones y {recursos} recursos')