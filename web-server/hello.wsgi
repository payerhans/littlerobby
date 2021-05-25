#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/HelloApp/")

from HelloApp import app as application
application.secret_key = '1164060317Esa'