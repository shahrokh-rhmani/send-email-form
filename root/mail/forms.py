from django import forms

class EmailForm(forms.Form):
    reci = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
