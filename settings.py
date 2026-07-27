from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'vercel-build-placeholder-key-safe-to-change'
DEBUG = False
ALLOWED_HOSTS = ['*']

# أهم سطرين يبحث عنهما نظام Vercel لتحديد نقطة الإقلاع
WSGI_APPLICATION = 'config.wsgi.application' # تأكد أنها تنتهي بـ .application
ROOT_URLCONF = 'config.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
