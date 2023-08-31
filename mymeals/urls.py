from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from meals.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meals.urls')),
]

handler404 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
