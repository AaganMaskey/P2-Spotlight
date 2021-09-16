from django.contrib import admin

# Register your models here.
from investor.models import investor_fund
from django.contrib import admin

class investorAdmin(admin.ModelAdmin):
    list_display    = ['name', 'email', 'address1', 'address2','zipNo','cardName','cardNum']

admin.site.register(investor_fund, investorAdmin)
