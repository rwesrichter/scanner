# coding=utf-8
import os
import sys
import configparser
from pathlib import Path

sys.path.append('../')

ROOT_DIR = os.path.dirname(__file__)
TOP_DIR = os.path.dirname(ROOT_DIR)
HOME_DIR = Path.home()

DATA_DIR = os.path.join(TOP_DIR, 'data')

VALID_CONFIG_NAMES = ['config.ini',
                      '.config.ini']

VALID_CONFIG_DIRS = [HOME_DIR, TOP_DIR, ROOT_DIR]

def locate_config():
    for d in VALID_CONFIG_DIRS:
        for n in VALID_CONFIG_NAMES:
            path = Path(d, n)
            if path.exists():
                return str(path)


def get_config(path=None):

    if not path:
        config_path = locate_config()
    else:
        config_path = path
    cfg = configparser.ConfigParser()

    if not config_path:
        raise ValueError("Unable to find a config.ini file.")

    cfg.read(config_path)

    return cfg

pass_dict = {'hall': 0,
             'bathroom': 0,
             'water': 0,
             'nurse': 1,
             'admin': 2,
             'councilor': 3,
             'teacher': 4,
             'detention': 5}

code_dict = {0: 'hall',
             1: 'nurse',
             2: 'admin',
             3: 'councilor',
             4: 'teacher',
             5: 'detention'}