"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.contrib import staticfiles 
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

jwtpatterns = [
    url(r'^jwt/refresh-token/', refresh_jwt_token, name='refresh_jwt_token'),
    url(r'^jwt/api-token-verify/', verify_jwt_token, name='verify_jwt_token'),
    url(r'^jwt/api-token-auth/', obtain_jwt_token, name='obtain_jwt_token'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('app.urls')),
    url(r'api/', include("app.urls")),
]
urlpatterns += jwtpatterns
urlpatterns += staticfiles_urlpatterns()

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)