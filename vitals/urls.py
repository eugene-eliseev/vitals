"""vitals URL Configuration

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
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    url(r'^people/add/$', views.PeopleCreateView.as_view(), name='people_add'),
    url(r'^people/(?P<pk>\d+)/$', views.PeopleUpdateView.as_view(), name='people_update'),
    url(r'^people/(?P<pk>\d+)/delete/$', views.PeopleDeleteView.as_view(), name='people_delete'),
    url(r'^people_list/$', views.PeopleList.as_view(), name='people_list'),
    url(r'^people_info/(?P<pk>\d+)/$', views.PeopleDetail.as_view(), name='people_detail'),
    url(r'^race/add$', views.RaceCreateView.as_view()),
    url(r'^vital/add$', views.VitalCreateView.as_view()),
    url(r'^seller/add$', views.SellerCreateView.as_view()),
    url(r'^buyer/add$', views.BuyerCreateView.as_view()),
    url(r'^pv/add$', views.PeopleVitalCreateView.as_view()),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^explorer/', include('explorer.urls')),
]

