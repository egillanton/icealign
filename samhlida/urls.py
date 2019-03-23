"""icealign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from samhlida import views

app_name = 'samhlida'

urlpatterns = [
    re_path(r'^biblian/$', views.Biblian.as_view(), name='biblian'),
    re_path(r'^baekur/$', views.Baekur.as_view(), name='baekur'),
    re_path(r'^ees/$', views.Ees.as_view(), name='ees'),
    re_path(r'^ema/$', views.Ema.as_view(), name='ema'),
    re_path(r'^eso/$', views.Eso.as_view(), name='eso'),
    re_path(r'^fornritin/$', views.Fornritin.as_view(), name='fornritin'),
    re_path(r'^hagstofan/$', views.Hagstofan.as_view(), name='hagstofan'),
    re_path(r'^kde4/$', views.Kde4.as_view(), name='kde4'),
    re_path(r'^opensubtitles/$', views.Opensubtitles.as_view(), name='opensubtitles'),
    re_path(r'^tatoeba/$', views.Tatoeba.as_view(), name='tatoeba'),
    re_path(r'^ubuntu/$', views.Ubuntu.as_view(), name='ubuntu'),
    re_path(r'^$', views.Samhlida.as_view(), name="index"),
]
