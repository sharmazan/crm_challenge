from django.contrib import admin
from .models import AppUser, Address, CustomerRelationship

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Address)
admin.site.register(CustomerRelationship)
