from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_list, contact_view, home_view

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('contacts/', contact_list, name='contact_list'),
    path('contact_view/', contact_view, name='contact_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
