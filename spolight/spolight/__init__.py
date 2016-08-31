# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, url_for

def print_settings(config):
    print '================================================='
    print 'SETTINGS for SPOLIGHT'
    print '================================================='
    for key, value in config:
        print '%s=%s' % (key, value)
    print '================================================='


def not_found(error):
    return render_template('404.html'), 404

def server_error(error):
    err_msg = str(error)
    return render_template('500.html', err_msg=err_msg), 500

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

def create_app(config_filepath='resource/config.cfg'):
    spolight_app = Flask(__name__)

    # set configuration
    from spolight.spolight_config import SpolightConfig
    spolight_app.config.from_object(SpolightConfig)
    spolight_app.config.from_pyfile(config_filepath, silent=True)
    print_settings(spolight_app.config.iteritems())

    # initialize Log object
    from spolight.spolight_logger import Log
    log_filepath = os.path.join(spolight_app.root_path, spolight_app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)

    # initialize DBManager object, create table(init_db() function)
    from spolight.database import DBManager
    #db_filepath = os.path.join(spolight_app.root_path, spolight_app.config['DB_FILE_PATH'])
    db_url = spolight_app.config['DB_URL'] #+ db_filepath
    DBManager.init(db_url, eval(spolight_app.config['DB_LOG_FLAG']))
    DBManager.init_db()

    # import all module from controller package 
    ##from spolight.controller import *

    # register blueprint to apply routing & template path
    from spolight.spolight_blueprint import spolight
    spolight_app.register_blueprint(spolight)

    from spolight.cache_session import SimpleCacheSessionInterface
    spolight_app.session_interface = SimpleCacheSessionInterface()

    #error handler for 404 and 500
    spolight_app.error_handler_spec[None][404] = not_found
    spolight_app.error_handler_spec[None][500] = server_error

    # filter function for pagination
    spolight_app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    return spolight_app


