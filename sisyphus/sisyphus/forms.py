from django import forms

class PhotoForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=255
    )
    imgfile = forms.ImageField(
        label='Select a file'
    )
