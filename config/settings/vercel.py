import os
from .base import *

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.vercel.app', 'now.sh', 'localhost', '127.0.0.1', '*']

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CELERY_TASK_ALWAYS_EAGER = True
