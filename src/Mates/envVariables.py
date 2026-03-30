SECRET_KEY_env = 'django-insecure-gpooiwq9+a@xg)wm0zop%jf4iyncv(prcm5@a@cw^&sb62^#3h'

DATABASES_env = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mates",
        "USER": "postgres",
        "PASSWORD": "kirigaya_kazut0",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "b2gj6jiyrj3q5lqg885e",
#         "USER": "u5fbl3kt0xxuspa5jeod",
#         "PASSWORD": "2i4lNjYcQYrpy7JhBKKuaFc4l1BpF0",
#         "HOST": "b2gj6jiyrj3q5lqg885e-postgresql.services.clever-cloud.com",
#         "PORT": "50013",
#         'CONN_MAX_AGE': 60,
#     }
    
# }

CORS_ALLOWED_ORIGINS_env = [
    'http://localhost:3030',
    'http://localhost:5173',
    'http://localhost:5174',
    "https://unisotropous-lauren-persuadably.ngrok-free.dev",
    "https://app-5cacd864-779f-4f64-a831-73e859e46fdc.cleverapps.io",
]

CSRF_TRUSTED_ORIGINS_env = [
    'https://unisotropous-lauren-persuadably.ngrok-free.dev',
]

CORS_ALLOW_HEADERS_env = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "ngrok-skip-browser-warning", 
]