from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, DeleteView
from .models import People, Vital, Race, PeopleVital, Seller, Buyer
from .forms import PeopleForm, RaceForm, VitalForm, PeopleVitalForm, SellerForm, BuyerForm


class PeopleCreateView(CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'people_form.html'
    success_url = '/success/'


class PeopleUpdateView(UpdateView):
    model = People
    form_class = PeopleForm
    template_name = 'people_form.html'
    success_url = '/success/'


class VitalCreateView(CreateView):
    model = Vital
    form_class = VitalForm
    template_name = 'people_form.html'
    success_url = '/success/'


class RaceCreateView(CreateView):
    model = Race
    form_class = RaceForm
    template_name = 'people_form.html'
    success_url = '/success/'


class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'people_form.html'
    success_url = '/success/'


class SellerCreateView(CreateView):
    model = Seller
    form_class = SellerForm
    template_name = 'people_form.html'
    success_url = '/success/'


class PeopleVitalCreateView(CreateView):
    model = PeopleVital
    form_class = PeopleVitalForm
    template_name = 'people_form.html'
    success_url = '/success/'


def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", data)
