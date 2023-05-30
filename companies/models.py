from django.db import models
from django.contrib.auth.models import User


class CompaniesModels(models.Model):
    class Meta:
        db_table = "Companies"

    name = models.CharField(max_length=100, null=False, blank=False)
    active = models.BooleanField(default=True)
    username = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )

    def __str__(self):
        return self.name


class CompaniesCNPJModels(models.Model):
    class Meta:
        db_table = "CNPJs"

    companie = models.ForeignKey(CompaniesModels, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=20, null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.cnpj