from django.contrib import admin
from myapp.models import Employees

class AppModel(admin.ModelAdmin):
    list_display=('name','email','address','phone')

admin.site.register(Employees,AppModel)
# Register your models here.
