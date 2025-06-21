from django import forms


class RegForm(forms.Form):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    birth = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': '0000-00-00'}))
    adress = forms.CharField(required=True)
    mail = forms.CharField(required=True)
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': '+71112223344'}))
    password = forms.CharField(required=True)


class LogInForm(forms.Form):
    mail = forms.CharField(required=True)
    password = forms.CharField(required=True)
