from django import forms
from companies.models import CompaniesModels, CompaniesCNPJModels
import re


class CompaniesForms(forms.ModelForm):

    class Meta:
        model = CompaniesModels
        exclude = ['username']

class CompaniesCNPJForms(forms.ModelForm):

    class Meta:
        model = CompaniesCNPJModels
        exclude = ['name', 'username']

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        regex = re.fullmatch(r'/^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$/', cnpj)
        if not regex:
            self.add_error(cnpj, 'Este CNPJ está incorreto, escreva corretamente!')

        return self.cleaned_data
