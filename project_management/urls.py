"""project_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from pm_module import views


urlpatterns = [

    url(r'^', include('auth_module.urls')),
    url(r'^', include('pm_module.urls')),
    url(r'^admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.conf.urls import include, url
# from django.contrib import admin
#
# from casino_finder import views
# from pm_module import views
# from rest_framework.urls import template_name
#
# from django.conf import settings
# from django.conf.urls.static import static
#
#
# urlpatterns = [
#     url(r'^$', views.index, name='homepage'),
#     url(r'^system_login/', include(admin.site.urls)),
#     url(r'^',include('auth_module.urls')),
#     url(r'^',include('casino_finder.urls')),
#     url(r'^',include('doctor_module.urls')),
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
