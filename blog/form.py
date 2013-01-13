from django import forms
class ContactForm(forms.Form):
        Account = forms.CharField()
        Passwd = forms.EmailField()
