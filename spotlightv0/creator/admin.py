from django.contrib import admin

# Register your models here.
from creator.models import creator_Basic
from django.contrib import admin


class creatorAdmin(admin.ModelAdmin):
    list_display = ['Author','title', 'description', 'category', 'image',
                    'reciepient', 'FundingGoal', 'pledgeAmount', 'TargetLaunchDate']


admin.site.register(creator_Basic, creatorAdmin)
