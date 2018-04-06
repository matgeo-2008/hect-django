from django.contrib import admin
from .models import Broker, Owner, Tenant

admin.site.register(Broker)
admin.site.register(Owner)
admin.site.register(Tenant)
