from django.urls import path
from companies.views import dashboard_view, details_view, addnew_companie_view, addnew_cnpj_view, update_cnpj_view, update_companie_view, delete_companie_view, list_data_for_update_cnpj

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('details/<int:companie_id>', details_view, name='details'),
    path('addnew-companie/', addnew_companie_view, name='add-companie'),
    path('details/addnew-cnpj/<int:companie_id>', addnew_cnpj_view, name='add-cnpj'),
    path('delete/<int:companie_id>', delete_companie_view, name='delete-companie'),
    path('details/update-companie/<int:companie_id>', update_companie_view, name='update-companie'),
    path('details/update-cnpj/<int:cnpj_id>', update_cnpj_view, name='update-companie'),
    path('details/list-data-for-update-cnpj/<int:cnpj_id>', list_data_for_update_cnpj, name='list-data-for-update-cnpj'),
]