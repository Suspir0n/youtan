from django.urls import path
from companies.views import dashboardView, detailsView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('details/<int:companie_id>', detailsView, name='details')
]