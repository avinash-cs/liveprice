from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(ProductInfo, ProductDetail)

class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',)