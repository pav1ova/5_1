from django.contrib import admin
from . models import  People, Company, House

admin.site.register(People)
admin.site.register(Company)
admin.site.register(House)