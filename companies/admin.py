from django.contrib import admin
from companies.models import CompaniesModels as Companies, CompaniesCNPJModels as CNPJs

class CompaniesAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "active")
    list_display_links = ("name", )
    search_fields = ("name", )
    list_filter = ("active", )
    list_editable = ("active", )
    list_per_page = 10
    ordering = ['id']

class CompaniesCNPJAdmin(admin.ModelAdmin):
    list_display = ("id", "cnpj", "name", "active")
    list_display_links = ("name", )
    search_fields = ("name", "cnpj")
    list_filter = ("active", )
    list_editable = ("active", )
    list_per_page = 10
    ordering = ['id']


admin.site.register(Companies, CompaniesAdmin)
admin.site.register(CNPJs, CompaniesCNPJAdmin)
