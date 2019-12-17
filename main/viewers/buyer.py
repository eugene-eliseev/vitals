from django.views.generic import ListView, DetailView

from main.forms import BuyerForm
from main.models import Buyer
from main.views import MainCreateView, MainUpdateView, MainDeleteView


class BuyerCreateView(MainCreateView):
    model = Buyer
    form_class = BuyerForm


class BuyerUpdateView(MainUpdateView):
    model = Buyer
    form_class = BuyerForm


class BuyerDeleteView(MainDeleteView):
    model = Buyer


class BuyerList(ListView):
    model = Buyer
    template_name = 'buyer_list.html'


class BuyerDetail(DetailView):
    model = Buyer
    template_name = 'buyer_detail.html'