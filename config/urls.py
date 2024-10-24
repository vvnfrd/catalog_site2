from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('', include('contacts.urls', namespace='contacts')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
