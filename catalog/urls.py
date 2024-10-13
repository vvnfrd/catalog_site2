from django.urls import path

from catalog.views import catalog_list

app_name = 'catalog_list'

urlpatterns = [
    path('', catalog_list, name='catalog_list'),

]