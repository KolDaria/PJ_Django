from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (CategoryDetailView, ContactListListView, ContactView, HomeViewListView, ProductCreateView,
                           ProductDeleteView, ProductDetailDetailView, ProductListListView, ProductUpdateView,
                           unpublish_product)

app_name = CatalogConfig.name

urlpatterns = [
    path('products_list/', ProductListListView.as_view(), name='products_list'),
    path('product_detail/<int:pk>', ProductDetailDetailView.as_view(), name='product_detail'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('', HomeViewListView.as_view(), name='home_view'),
    path('contacts/', ContactListListView.as_view(), name='contact_list'),
    path('contact_view/', ContactView.as_view(), name='contact_view'),
    path('product/<int:pk>/unpublish/', unpublish_product, name='unpublish_product'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
