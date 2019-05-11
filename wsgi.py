import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.append(sys.path.append(os.path.dirname(os.path.realpath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tna.settings")

application = get_wsgi_application()
