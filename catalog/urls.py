from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_view, contacts, home

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contact_view/', contact_view, name='contact_view'),
]
