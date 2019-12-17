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
import main.viewers.people as p
import main.viewers.pv as pv
import main.viewers.race as r
import main.viewers.seller as s
import main.viewers.buyer as b
import main.viewers.vital as v

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^explorer/', include('explorer.urls')),
    path('success/', views.success),
]

views_classes = {
    'people': {
        'add': p.PeopleCreateView,
        'update': p.PeopleUpdateView,
        'delete': p.PeopleDeleteView,
        'list': p.PeopleList,
        'detail': p.PeopleDetail
    },
    'race': {
        'add': r.RaceCreateView,
        'list': r.RaceList
    },
    'vital': {
        'add': v.VitalCreateView,
        'list': v.VitalList
    },
    'pv': {
        'add': pv.PeopleVitalCreateView,
        'update': pv.PeopleVitalUpdateView,
        'delete': pv.PeopleVitalDeleteView,
        'list': pv.PeopleVitalList,
        'detail': pv.PeopleVitalDetail
    },
    'seller': {
        'add': s.SellerCreateView,
        'update': s.SellerUpdateView,
        'delete': s.SellerDeleteView,
        'list': s.SellerList,
        'detail': s.SellerDetail
    },
    'buyer': {
        'add': b.BuyerCreateView,
        'update': b.BuyerUpdateView,
        'delete': b.BuyerDeleteView,
        'list': b.BuyerList,
        'detail': b.BuyerDetail
    }
}

for model_name, model_actions in views_classes.items():
    for action, view in model_actions.items():
        actions = [model_name, action]
        success_url = '/'.join([model_name, "list"])
        if action != "list":
            actions.insert(1, "(?P<pk>\d+)")
        actions_url = '/'.join(actions)
        urlpatterns.append(url(
            r'^{}/$'.format(actions_url),
            view.as_view(),
            name='{}_{}'.format(model_name, action)
        ))

