from django.urls import path

from contacts.views import contacts

app_name = 'contacts'

urlpatterns = [
    path('contacts/', contacts, name='info'),

]