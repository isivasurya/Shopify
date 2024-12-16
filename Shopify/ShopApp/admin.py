from django.contrib import admin
from .models import *
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')

admin.site.register(Category,categoryAdmin)
admin.site.register(Product)