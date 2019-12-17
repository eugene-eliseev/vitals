from django.views.generic import ListView, DetailView

from main.forms import SellerForm
from main.models import Seller
from main.views import MainCreateView, MainUpdateView, MainDeleteView


class SellerCreateView(MainCreateView):
    model = Seller
    form_class = SellerForm


class SellerUpdateView(MainUpdateView):
    model = Seller
    form_class = SellerForm


class SellerDeleteView(MainDeleteView):
    model = Seller


class SellerList(ListView):
    model = Seller
    template_name = 'seller_list.html'


class SellerDetail(DetailView):
    model = Seller
    template_name = 'seller_detail.html'