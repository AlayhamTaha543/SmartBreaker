import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# هذا السطر يخبر بايثون بتمرير القراءة لمجلد إعداداتك الأصلي
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-build')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['.vercel.app', 'now.sh', 'localhost', '127.0.0.1']

# تحديد نقطة الإقلاع التي يبحث عنها Vercel
WSGI_APPLICATION = 'config.wsgi.app'
ROOT_URLCONF = 'config.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
