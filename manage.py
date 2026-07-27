#!/usr/bin/env python
import os
import sys
from types import ModuleType

def main():
    # 1. إخبار نظام Django باستخدام ملف إعدادات وهمي للبناء
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vercel_build_settings')
    
    # 2. إنشاء وتجهيز ملف الإعدادات الوهمي في الذاكرة لتخطي فحص Vercel الصارم
    mod = ModuleType('vercel_build_settings')
    mod.SECRET_KEY = 'vercel-build-placeholder-key-safe-to-change'
    mod.DEBUG = False
    mod.ALLOWED_HOSTS = ['*']
    mod.ROOT_URLCONF = 'config.urls'
    mod.WSGI_APPLICATION = 'config.wsgi.app'
    mod.INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    mod.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
    sys.modules['vercel_build_settings'] = mod

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
