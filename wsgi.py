#! /usr/bin/python3
import sys

sys.path.insert(0, '/var/www/box_packing/')
from box_packing.app import app as application

application.secret_key = 'supersecretkey'
