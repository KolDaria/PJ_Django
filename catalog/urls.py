from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_list, contact_view, home_view, product_detail, product_list

app_name = CatalogConfig.name

urlpatterns = [
    path('product_detail/<int:product_id>', product_detail, name='product_detail'),
    path('product_list/', product_list, name='product_list'),
    path('', home_view, name='home_view'),
    path('contacts/', contact_list, name='contact_list'),
    path('contact_view/', contact_view, name='contact_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
