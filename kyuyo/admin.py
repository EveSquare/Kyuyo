from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ZandakaModel)
admin.site.register(models.SyunyuModel)
admin.site.register(models.MonthlyModel)
admin.site.register(models.ExpenseModel)