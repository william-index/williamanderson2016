# /extensions/datetimeformat.py

import jinja2
from datetime import datetime

def datetimeformat(value, format='%Y-%m-%dT00:00:00-05:00'):
    time = datetime.strptime(value, '%Y/%m/%d')
    return time.strftime(format)

def datetimenow(string):
    time = datetime.now().time()
    return time.strftime('%Y-%m-%dT%H:%M:%S-05:00')

class Datetimeformat(jinja2.ext.Extension):
    def __init__(self, environment):
        super(Datetimeformat, self).__init__(environment)
        environment.filters['datetimeformat'] = datetimeformat
        environment.filters['datetimenow'] = datetimenow
