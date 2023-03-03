# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DB_NAME'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': environ.get('DB_HOST', '127.0.0.1'),
        'PORT': environ.get('DB_PORT', 5432),
        'OPTIONS': {'options': '-c search_path=public,content'},
    }
}
