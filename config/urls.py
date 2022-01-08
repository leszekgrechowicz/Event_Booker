from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from config import settings

urlpatterns = [
    path('829admin976/', admin.site.urls, name="admin"),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('event_booker.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
