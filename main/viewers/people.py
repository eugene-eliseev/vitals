from django.views.generic import ListView, DetailView

from main.forms import PeopleForm
from main.models import People
from main.views import MainCreateView, MainUpdateView, MainDeleteView


class PeopleCreateView(MainCreateView):
    model = People
    form_class = PeopleForm


class PeopleUpdateView(MainUpdateView):
    model = People
    form_class = PeopleForm


class PeopleDeleteView(MainDeleteView):
    model = People


class PeopleList(ListView):
    model = People
    template_name = 'people_list.html'


class PeopleDetail(DetailView):
    model = People
    template_name = 'people_detail.html'