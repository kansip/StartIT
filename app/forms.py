from django import forms


class feedback(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
