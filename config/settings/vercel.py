import os
import dj_database_url
from pathlib import Path

# تحديد المسار الرئيسي للمشروع بشكل صحيح
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# قراءة المتغيرات البيئية التي قمنا بضبطها في لوحة تحكم Vercel سابقاً
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key-for-vercel-build')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# السماح لجميع نطاقات Vercel بتشغيل التطبيق
ALLOWED_HOSTS = ['.vercel.app', 'now.sh', 'localhost', '127.0.0.1', '*']

# نقطة الإقلاع والروابط الأساسية لمجلد config الخاص بك
WSGI_APPLICATION = 'config.wsgi.app'
ROOT_URLCONF = 'config.urls'

# ربط قاعدة بيانات Supabase مجمّعة الاتصال (Transaction Pooler)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# التطبيقات الأساسية المفعّلة في مشروعك (تأكد من مطابقتها لتطبيقاتك إذا لزم الأمر)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# الإعدادات الافتراضية للملفات الثابتة لضمان عبور الفحص
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
