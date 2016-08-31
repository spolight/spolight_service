import sys

from spolight import create_app

reload(sys)
sys.setdefaultencoding('utf-8')

application = create_app()

if __name__ == '__main__' :
    print 'starting server...'
    application.run(host='0.0.0.0', port=5000, debug=True )
