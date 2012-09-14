from lists.models import Item, List
from django import forms

class ListForm(forms.ModelForm):
	class Meta:
		model = List

