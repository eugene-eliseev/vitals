from django.views.generic import ListView

from main.forms import VitalForm
from main.models import Vital
from main.views import MainCreateView


class VitalCreateView(MainCreateView):
    model = Vital
    form_class = VitalForm


class VitalList(ListView):
    model = Vital
    template_name = 'vital_list.html'
