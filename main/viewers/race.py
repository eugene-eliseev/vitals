from django.views.generic import ListView

from main.forms import RaceForm
from main.models import Race
from main.views import MainCreateView


class RaceCreateView(MainCreateView):
    model = Race
    form_class = RaceForm


class RaceList(ListView):
    model = Race
    template_name = 'race_list.html'
