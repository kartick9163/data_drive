# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('', include('myapp.url')),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.url')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
