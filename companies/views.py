from django.shortcuts import render


def dashboardView(request):
    return render(request, 'companies/index.html')


def detailsView(request):
    return render(request, 'companies/details.html')
