import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:/Users/Chi/AppData/Local/Programs/Python/Python38-32/Lib/site-packages")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:/Users/Chi/Desktop/Django Projects/EngineeringHelper') 
sys.path.append('C:/Users/Chi/Desktop/Django Projects/EngineeringHelper/EngineeringHelper')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'EngineeringHelper.settings' 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EngineeringHelper.settings")  
 
application = get_wsgi_application()