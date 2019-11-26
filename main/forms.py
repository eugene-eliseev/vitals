from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import People, Race, PeopleVital, Vital, Buyer, Seller


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('first_name', 'second_name', 'reason', 'sex', 'is_alive', 'health_problems', 'birthday', 'sell_price',
                  'sell_date', 'seller', 'buyer', 'race')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save people'))


class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save race'))


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ('name', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save buyer'))


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('name', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save seller'))


class VitalForm(forms.ModelForm):
    class Meta:
        model = Vital
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save vital'))


class PeopleVitalForm(forms.ModelForm):
    class Meta:
        model = PeopleVital
        fields = ('vital', 'people', 'condition', 'price', 'buyer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save seller'))
