from django.urls import path
from companies.views import dashboardView, detailsView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('details', detailsView, name='details')
]