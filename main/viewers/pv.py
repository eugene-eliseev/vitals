from django.views.generic import ListView, DetailView

from main.forms import PeopleVitalForm
from main.models import PeopleVital
from main.views import MainCreateView, MainUpdateView, MainDeleteView


class PeopleVitalCreateView(MainCreateView):
    model = PeopleVital
    form_class = PeopleVitalForm


class PeopleVitalUpdateView(MainUpdateView):
    model = PeopleVital
    form_class = PeopleVitalForm


class PeopleVitalDeleteView(MainDeleteView):
    model = PeopleVital


class PeopleVitalList(ListView):
    model = PeopleVital
    template_name = 'pv_list.html'


class PeopleVitalDetail(DetailView):
    model = PeopleVital
    template_name = 'pv_detail.html'