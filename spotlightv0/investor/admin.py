from django.contrib import admin

# Register your models here.
from investor.models import investor_fund
from django.contrib import admin


class investorAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at', 'userid',
                    'projectid', 'username', 'pledgeAmount']


admin.site.register(investor_fund, investorAdmin)
