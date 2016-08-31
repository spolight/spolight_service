# -*- coding: utf-8 -*-

from flask import Blueprint
from spolight.spolight_logger import Log

spolight = Blueprint('spolight', __name__, template_foler='../templates', static_folder='../static')

Log.info('static folder : %s' % spolight.static_folder)
Log,info('template folder : %s' % spolight.template_folder)
