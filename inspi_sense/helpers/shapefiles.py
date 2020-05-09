from inspi_sense.helpers.constants import PROG_NAME

from os import path, getcwd, chdir, mkdir
import urllib
import zipfile
import matplotlib.pyplot as plt
import geopandas as gpd
from logging import getLogger

log = getLogger(f'{__name__}.{PROG_NAME}')
info = log.info

info(f'Logger started for {__name__}')


def download_zip(url=None):
    chdir('..')
    print(getcwd())
    if path.exists(getcwd() + '/temp/'):
        print('yay')
    else:
        mkdir(getcwd() + '/temp/')

