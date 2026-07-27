from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# إعدادات أساسية ثابتة لتخطي فحص Vercel الأولي بنجاح
SECRET_KEY = 'vercel-build-placeholder-key-safe-to-change'
DEBUG = False
ALLOWED_HOSTS = ['*']

# أهم سطرين يبحث عنهما نظام Vercel
WSGI_APPLICATION = 'config.wsgi.app'
ROOT_URLCONF = 'config.urls'

# قاعدة بيانات وهمية للفحص فقط (التطبيق الفعلي سيقرأ من ملف الإنتاج لاحقاً)
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
