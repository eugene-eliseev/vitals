from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from .models import People, Race, PeopleVital, Vital, Buyer, Seller


class MainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(
            Button('delete', 'Delete', onclick='window.location.href="{}"'.format('delete'), css_class='btn btn-danger')
        )


class PeopleForm(MainForm):
    class Meta:
        model = People
        fields = [f.name for f in People._meta.fields]


class RaceForm(MainForm):
    class Meta:
        model = Race
        fields = [f.name for f in Race._meta.fields]


class BuyerForm(MainForm):
    class Meta:
        model = Buyer
        fields = [f.name for f in Buyer._meta.fields]


class SellerForm(MainForm):
    class Meta:
        model = Seller
        fields = [f.name for f in Seller._meta.fields]


class PeopleVitalForm(MainForm):
    class Meta:
        model = PeopleVital
        fields = [f.name for f in PeopleVital._meta.fields]


class VitalForm(MainForm):
    class Meta:
        model = Vital
        fields = [f.name for f in Vital._meta.fields]