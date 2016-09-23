from django import forms

class ContactForm(forms.Form):
	name= forms.CharField(label='Контактное лицо')
	phone= forms.CharField(label='Телефон', required=False)
	sender = forms.EmailField(label='Электронная почта')
	theme = forms.CharField(label='Тема заявки')
	message = forms.CharField(label='Текст заявки', widget=forms.Textarea)