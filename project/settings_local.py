# -*- coding: utf-8 -*-

import os, sys
ProjectPath = os.path.realpath(os.path.dirname(__file__))
DataRoot = os.path.normpath(ProjectPath + '/../data/') + '/'
StaticRoot = os.path.normpath(ProjectPath + '/../static/') + '/'
LocalePaths = (os.path.normpath(ProjectPath + '/locale/') + '/',)
FontPath = os.path.normpath(StaticRoot + 'fonts/') + '/'
sys.path.append(os.path.normpath(ProjectPath) + '/')

#*************************************************************
# Environment settings

Deploy = True
DebugToolbar = False
PrependWWW = False


Admins = (
    ('Eden Kirin', 'edkirin@gmail.com'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'diocles',                      # Or path to database file if using sqlite3.
        'USER': 'diocles',                      # Not used with sqlite3.
        'PASSWORD': 'pharmaphalanx44c01',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'abda': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'abda',                      # Or path to database file if using sqlite3.
        'USER': 'diocles',                      # Not used with sqlite3.
        'PASSWORD': 'pharmaphalanx44c01',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

UseCaching = True
if UseCaching:
    Caches = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'KEY_PREFIX': 'diocles',
        }
    }
else:
    Caches = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

EMAIL_HOST = 'mail.t-com.hr'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = "noreply@lobofarm.hr"  # from address for server error emails
SERVER_EMAIL = "noreply@lobofarm.hr"  # used as the from address for django.core.mail.mail_admins() and django.core.mail.mail_managers()

