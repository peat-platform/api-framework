import sys
import os

this_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(this_path + '/configs')) # add xtreme to our path

from configs.settings_local import *

try:
    with open('configs/application.id', 'r+') as f:
        APPLICATION_ENV = f.read()
except IOError as e:
    APPLICATION_ENV = 'production'

if APPLICATION_ENV == 'development':
    from configs.settings_development import *
elif APPLICATION_ENV == 'production':
    from configs.settings_production import *