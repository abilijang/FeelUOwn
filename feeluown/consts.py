# -*- coding: utf-8 -*-

import os
from enum import Enum


THEMES_DIR = './feeluown/themes'
PLUGINS_DIR = './feeluown/plugins'
APP_ICON = './feeluown/feeluown.png'
DEFAULT_THEME_NAME = 'Tomorrow Night'


HOME_DIR = os.path.expanduser('~') + '/.FeelUOwn'

DATA_DIR = HOME_DIR + '/data'
USER_PLUGINS_DIR = HOME_DIR + '/plugins'
USER_THEMES_DIR = HOME_DIR + '/themes'
CACHE_DIR = HOME_DIR + '/cache'
SONG_DIR = HOME_DIR + '/songs'
COLLECTIONS_DIR = HOME_DIR + '/collections'

LOG_FILE = HOME_DIR + '/stdout.log'
