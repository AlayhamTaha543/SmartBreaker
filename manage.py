#!/usr/bin/env python
import os
import sys

def main():
    # توجيه النظام لملف الإعدادات المخصص لـ Vercel كخيار افتراضي
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.vercel')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed? "
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
