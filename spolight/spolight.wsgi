"""
spolight web application
"""

import sys
sys.path.insert(0,'/Users/parkhyunjae/spolight_service/spolight')

from photolog import create_app
application = create_app('/Users/parkhyunjae/spolight_service/spolight/spolight/resource/config.cfg')      
