from django.shortcuts import render, redirect
from companies.models import CompaniesModels, CompaniesCNPJModels
from companies.forms import CompaniesCNPJForms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse


@login_required(login_url="/auth/login/")
def dashboard_view(request):
    companies = CompaniesModels.objects.all()
    companie_paginator = Paginator(companies, 6)
    page_num = request.GET.get('page')
    page = companie_paginator.get_page(page_num)
    return render(request, 'companies/index.html', {'page': page})


@login_required(login_url="/auth/login/")
def addnew_companie_view(request):
    name = request.GET.get('name')
    active = request.GET.get('active')
    username = User.objects.get(username=request.user.get_username())

    if CompaniesModels.objects.filter(name=name).exists():
        messages.warning(request, 'Está empresa já existe!')

    new_companie = CompaniesModels(
        name=name,
        active=active,
        username=username
    )
    new_companie.save()

    messages.info(request, 'Empresa criada com sucesso!')
    return redirect('/')


@login_required(login_url="/auth/login/")
def details_view(request, companie_id):
    form = CompaniesCNPJForms()
    companie = CompaniesModels.objects.filter(id=companie_id).first()
    cnpjs = CompaniesCNPJModels.objects.filter(companie__id=companie_id)
    data = {
        'companie': companie,
        'cnpjs': cnpjs,
        'form': form,
    }
    return render(request, 'companies/details.html', data)


@login_required(login_url="/auth/login/")
def addnew_cnpj_view(request, companie_id):
    companie = CompaniesModels.objects.get(id=companie_id)
    name = request.GET.get('name')
    active = request.GET.get('active')
    cnpj = request.GET.get('cnpj')
    new_cnpj = CompaniesCNPJModels(
        name=name,
        active=active,
        cnpj=cnpj,
        companie=companie
    )
    new_cnpj.save()
    messages.info(request, 'CNPJ adicionado na empresa com sucesso!')
    return redirect(f'/details/{companie_id}')


@login_required(login_url="/auth/login/")
def update_companie_view(request, companie_id):
        companie = CompaniesModels.objects.get(id=companie_id)
        companie.name = request.GET.get('name')
        companie.active = request.GET.get('active')
        companie.save()
        messages.info(request, f'Dados da empresa {request.GET.get("name")} atualizadas com sucesso!')

        return redirect(f'/details/{companie.id}')


@login_required(login_url="/auth/login/")
def update_cnpj_view(request, cnpj_id):
    companie_cnpj = CompaniesCNPJModels.objects.get(id=cnpj_id)
    companie = CompaniesModels.objects.filter(name=request.GET.get('companie')).first()
    companie_cnpj.active = request.GET.get('active')
    companie_cnpj.cnpj = request.GET.get('cnpj')
    companie_cnpj.companie.name = request.GET.get('companie')
    companie_cnpj.save()
    messages.info(request, f'Dados do cnpj {companie_cnpj.cnpj} atualizados com sucesso!')

    return redirect(f'/details/{companie.id}')



@login_required(login_url="/auth/login/")
def list_data_for_update_cnpj(request, cnpj_id):
    cnpj = CompaniesCNPJModels.objects.get(id=cnpj_id)
    print(cnpj)
    context = {
        'cnpj': cnpj.cnpj,
        'companie': cnpj.companie.name,
        'active': cnpj.active
    }
    return JsonResponse({'context': context})


@login_required(login_url="/auth/login/")
def delete_companie_view(request, companie_id):
    companie = CompaniesModels.objects.get(id=companie_id)
    companie.delete()
    messages.info(request, 'Empresa apagada com sucesso!')
    return redirect('dashboard')
