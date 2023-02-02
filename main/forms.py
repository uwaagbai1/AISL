from django import forms

class ContactForm(forms.Form):

	full_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'data-validation-required-message':'Please enter your name',}), max_length = 50)
	subject = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'data-validation-required-message':'Please enter a Subject',}), max_length = 50)
	email_address = forms.EmailField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'data-validation-required-message':'Please enter your Email Address',}),  max_length = 150)
	message = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Here', 'rows':"6", 'data-validation-required-message':'Please enter a message',}), max_length = 2000)
