DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'G249database',
    }
},
INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
],
MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
    # ...
],
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    # Add the domains or origins that are allowed to make CORS requests
    'http://localhost:8000',  # Example: Allow requests from localhost:3000
    'g249-django-git-main-keinoc.vercel.app',
    "https://g249-app.herokuapp.com",
    "http://127.0.0.1:3000"   # Example: Allow requests from example.com
]