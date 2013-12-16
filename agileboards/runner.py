#!/usr/bin/env python
"""
agileboards.runner
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2014 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from logan.runner import run_app, configure_app

import base64
import os


KEY_LENGTH = 40

CONFIG_TEMPLATE = """
# This file is just Python, with a touch of Django which means you
# you can inherit and tweak settings to your hearts content.
from agileboards.settings import *

import os.path

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        # You can swap out the engine for MySQL easily by changing this value
        # to ``django.db.backends.mysql`` or to PostgreSQL with
        # ``django.db.backends.postgresql_psycopg2``

        # If you change this, you'll also need to install the appropriate python
        # package: psycopg2 (Postgres) or mysql-python
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': os.path.join(CONF_ROOT, 'agileboards.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

###########
## etc. ##
###########

# If this file ever becomes compromised, it's important to regenerate your SECRET_KEY
# Changing this value will result in all current sessions being invalidated
SECRET_KEY = %(default_key)r
"""


def generate_settings():
    """
    This command is run when ``default_path`` doesn't exist, or ``init`` is
    run and returns a string representing the default data to put into their
    settings file.
    """
    output = CONFIG_TEMPLATE % dict(
        default_key=base64.b64encode(os.urandom(KEY_LENGTH)),
    )

    return output


def initialize_app(config):
    apply_legacy_settings(config)


def apply_legacy_settings(config):
    settings = config['settings']

    # Set ALLOWED_HOSTS if it's not already available
    if not settings.ALLOWED_HOSTS and settings.AGILEBOARDS_URL_PREFIX:
        from urlparse import urlparse
        urlbits = urlparse(settings.AGILEBOARDS_URL_PREFIX)
        if urlbits.hostname:
            settings.ALLOWED_HOSTS = (urlbits.hostname,)


def configure():
    configure_app(
        project='agileboards',
        default_config_path='~/.agileboards/agileboards.conf.py',
        default_settings='agileboards.settings',
        settings_initializer=generate_settings,
        settings_envvar='AGILEBOARDS_CONF',
        initializer=initialize_app,
    )


def main():
    run_app(
        project='agileboards',
        default_config_path='~/.agileboards/agileboards.conf.py',
        default_settings='agileboards.settings',
        settings_initializer=generate_settings,
        settings_envvar='AGILEBOARDS_CONF',
        initializer=initialize_app,
    )


if __name__ == '__main__':
    main()
