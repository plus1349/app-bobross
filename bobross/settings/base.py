import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# base_dir = lambda *args: os.path.join(BASE_DIR, *args)

ROOT_DIR = os.path.dirname(BASE_DIR)
# root_dir = lambda *args: os.path.join(ROOT_DIR, *args)

SECRET_KEY = 'mq(_@iwt8-h+k59spl%*^x9q2p+ex9i=e06px08*!1+w*(hzu&'

DEBUG = False

SITE_ID = 1

INSTALLED_APPS = (
    'djangocms_admin_style', # required before 'django.contrib.admin'

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'menus',
    'rest_framework',
    'rest_framework.authtoken',
    'sekizai',
    'treebeard',
    'filer',
    'easy_thumbnails',
    'mptt',

    'api',
    'paintings',
    'users',

    # required after custom apps
    'cms',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_column',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    # 'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'bobross.urls.base'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (os.path.join(ROOT_DIR, 'bobross', 'templates'),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.i18n',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
)

CMS_TEMPLATES = (
    ('base.html', 'Base'),
)

WSGI_APPLICATION = 'bobross.wsgi.application'

AUTH_USER_MODEL = 'users.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = (
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
)

_ = lambda x: x

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian'))
)

LOCALE_PATHS = (os.path.join(ROOT_DIR, 'bobross', 'locale'),)

USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_ZONE = 'UTC'

FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(ROOT_DIR, 'bobross', 'static'),)
STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATIC_URL = '/static/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'api.renderers.JSONRenderer',
    )
}

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
