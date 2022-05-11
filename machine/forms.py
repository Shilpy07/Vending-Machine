# Django form for machine app
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from machine.models import Currency
from machine.models import TransactionHistory

# create a ModelForm
class TransactionHistoryForm(forms.ModelForm):
	"""
	Customized transaction form for Collecting order
	"""

	currency = forms.ModelMultipleChoiceField(
		queryset=Currency.objects.all(),
		widget=FilteredSelectMultiple("Currency", is_stacked=False),
		help_text="Select Currency Deposited"
	)

	class Media:
		css = {'all': ('/admin/css/widgets.css', 'admin/css/overrides.css'), }
		js = ('/admin/jquery.js', '/admin/jsi18n/')

	class Meta:
		model = TransactionHistory
		fields = ('product', 'currency')
