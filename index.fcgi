#!/home/meues581/.env/bin/python
import os
import sys
import site

#/home/meues581/public_html/registrodeimoveisonline.com.br
 
site.addsitedir('/home/meues581/.env/lib/python2.7/site-packages/')
# Adicione ao PATH do Python as seguintes pastas
sys.path.append('/home/meues581/public_html')
sys.path.append('/home/meues581/public_html/registrodeimoveisonline.com.br')
#sys.path.append('/home/meues581/public_html/libs')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'consulta1rimc.settings'
 
activate_env=os.path.expanduser("/home/meues581/.env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
 
# Aqui utilizamos a biblioteca de FastCGI que baixamos anteriormente.
from django_fastcgi.servers.fastcgi import runfastcgi
from django.core.servers.basehttp import get_internal_wsgi_application
 
wsgi_application = get_internal_wsgi_application()
runfastcgi(wsgi_application, method="prefork", daemonize="false", minspare=1, maxspare=1, maxchildren=1)
