GOOGLE_LOGIN_CLIENT_ID = "360171152864-1vbhe2nh4dt7tmqgoqf5nnk1kti5qkrp.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "34HiDfIc8fjei3WihMpAezAC"
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SECRET_KEY = 'super secret key'

OAUTH_CREDENTIALS={
    'google': {
        'id': GOOGLE_LOGIN_CLIENT_ID,
        'secret': GOOGLE_LOGIN_CLIENT_SECRET
    }
}
