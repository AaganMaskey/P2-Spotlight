from django import forms
from .models import creator_Basic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# creating a form
class creatorBasic(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = creator_Basic

		# specify fields to be used
		fields = [
			"title",
			"description",
			 "image",
			 "FundingGoal",
			 "TargetLaunchDate"

		]
