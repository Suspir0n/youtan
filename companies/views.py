from django.shortcuts import render
from companies.models import CompaniesModels, CompaniesCNPJModels
from companies.forms import CompaniesForms


def dashboardView(request):
    companies = CompaniesModels.objects.all()
    return render(request, 'companies/index.html', {'companies': companies})


def detailsView(request, companie_id):
    form = CompaniesForms()
    companie = CompaniesModels.objects.filter(id=companie_id)
    cnpjs = CompaniesCNPJModels.objects.filter(companie__id=companie_id)
    data = {
        'companie': companie,
        'cnpjs': cnpjs,
        'form': form,
    }
    return render(request, 'companies/details.html', data)
