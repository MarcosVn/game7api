#!/home/meues581/.env/bin/python
import os
import sys
import site

site.addsitedir('/home/menuw652/menuwebenv/lib/python2.7/site-packages/')
sys.path.append('/home/menuw652/public_html')
sys.path.append('/home/menuw652/public_html/menuweb.com.br')

 
os.environ['DJANGO_SETTINGS_MODULE'] = 'game7api.settings'
 
activate_env=os.path.expanduser("/home/menuw652/menuwebenv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django_fastcgi.servers.fastcgi import runfastcgi
from django.core.servers.basehttp import get_internal_wsgi_application
 
wsgi_application = get_internal_wsgi_application()
runfastcgi(wsgi_application, method="prefork", daemonize="false", minspare=1, maxspare=1, maxchildren=1)
