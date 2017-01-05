from django.contrib import admin
from auth_module.models import *


class NavigationMenuAdmin(admin.ModelAdmin):
    fields = ['name','slug','parent','status']
    list_display = ('name', 'status','parent','slug')

admin.site.register(NavigationMenu, NavigationMenuAdmin)
