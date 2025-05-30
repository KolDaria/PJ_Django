from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ContactListListView, ContactView, HomeViewListView, ProductDetailDetailView,
                           ProductListListView)

app_name = CatalogConfig.name

urlpatterns = [
    path('product_list/', ProductListListView.as_view(), name='product_list'),
    path('product_detail/<int:product_id>', ProductDetailDetailView.as_view(), name='product_detail'),
    path('', HomeViewListView.as_view(), name='home_view'),
    path('contacts/', ContactListListView.as_view(), name='contact_list'),
    path('contact_view/', ContactView.as_view(), name='contact_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
