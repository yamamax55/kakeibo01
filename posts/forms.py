from django import forms


class KakikomiForm(forms.Form):
        name = forms.CharField()
        email = forms.EmailField()
        body = forms.CharField()
