# coding=utf-8
import os
import sys
import configparser
from pathlib import Path

sys.path.append('../')

ROOT_DIR = os.path.dirname(__file__)
TOP_DIR = os.path.dirname(ROOT_DIR)
HOME_DIR = Path.home()

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