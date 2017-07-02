"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

import homepage.views
import karyawan.views
import kehadiran.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', karyawan.views.profil),
    url(r'^login/', homepage.views.login_view),
    url(r'^logout/', homepage.views.logout_view),
    # url(r'^daftar_hadir/', kehadiran.views.daftar_hadir),
]
