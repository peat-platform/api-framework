__author__ = 'mpetyx'

import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
