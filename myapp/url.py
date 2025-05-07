from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('createuser', views.createUser, name='createUser'),
    path('loginapi', views.login_api, name='login_api'),
    path('drive', views.driveUI, name='driveUI'),
    path('upload', views.fileUpload, name='upload'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)