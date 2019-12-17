activate_this = 'C:/Users/User/dev/app-bobross/env/Scripts/activate.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site


site.addsitedir('C:/Users/User/dev/app-bobross/env/Lib/site-packages')

sys.path.append('C:/Users/User/dev/app-bobross')
sys.path.append('C:/Users/User/dev/app-bobross/bobross')

os.environ['DJANGO_SETTINGS_MODULE'] = 'bobross.settings.prod'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bobross.settings.prod")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
