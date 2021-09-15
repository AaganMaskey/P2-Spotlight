from django import forms
from .models import creator_Basic, creator_fund


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
		]
