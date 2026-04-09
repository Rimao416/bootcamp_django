
from django.contrib import admin
from django.urls import path,include
# Pour servir les ficheirs médias (photos uploadées)

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # include : délègue toutes les autres URLS à notre fichiers clinique/urls
    path('',include('clinique.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
