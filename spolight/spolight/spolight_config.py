# -*- coding: utf-8 -*-
class SpolightConfig(object):
    DB_URL= 'postgresql://localhost/spo_db'
    # session timeout
    PERMANENT_SESSION_LIFETIME = 60 * 60
    LOG_LEVEL = 'debug'
    LOG_FILE_PATH = 'resource/log/spolight.log'
    DB_LOG_FLAG = 'True'
    #OAuth
    GOOGLE_APP_KEY    = ''
    GOOGLE_APP_SECRET = ''
    GOOLGE_CALLBACK_SERVER = 'http://localhost:5000'
