"""
agileboards.wsgi
~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2014 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agileboards.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
