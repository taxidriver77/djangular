from django.contrib import admin

# Register your models here.
from .models import Customer,ListCustomer,Company

admin.site.register(Customer)
admin.site.register(ListCustomer)
admin.site.register(Company)