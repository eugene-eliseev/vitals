from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .generate_data import generate_data


class MainCreateView(CreateView):
    template_name = 'main_form.html'


class MainUpdateView(UpdateView):
    template_name = 'main_form.html'


class MainDeleteView(DeleteView):
    template_name = 'delete.html'


def index(request):
    generate_data()
    return render(request, "index_content.html")


def success(request):
    return render(request, "success.html")