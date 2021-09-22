from django.contrib import admin

# Register your models here.
from UserProfile.models import profile_Basic


class profileAdmin(admin.ModelAdmin):
    list_display = ['User','Email', 'Phone', 'Address', 'Funded',
                    'Projects']


admin.site.register(profile_Basic, profileAdmin)



    
