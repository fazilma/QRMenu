from django.conf import settings
from django.core.files.storage import default_storage


app_storage = None
if settings.DEBUG == True:
    app_storage = default_storage
else:
    app_storage = ''