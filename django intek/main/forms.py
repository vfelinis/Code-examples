from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	sender = forms.EmailField()
	full_name= forms.CharField(required=False)
	message = forms.CharField(widget=forms.Textarea)