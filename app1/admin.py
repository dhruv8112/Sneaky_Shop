from django.contrib import admin

# Register your models here.
from .models import *


class CatAdmin(admin.ModelAdmin):
    list_display = ('img_return', 'cat_name', 'cat_desc', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_name',  'brand_name',
                    'price', 'Pro_Description', 'size',)


class contactRegister(admin.ModelAdmin):
    list_display = ['name',  'contact_no', 'subject',]


admin.site.register(categories, CatAdmin)
admin.site.register(products, ProductAdmin)
admin.site.register(contact, contactRegister)