from django import forms
from sisyphus.models import Trail

class PhotoForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=255
    )
    imgfile = forms.ImageField(
        label='Select a file'
    )
    trail = forms.ModelChoiceField(
        queryset=Trail.objects.all().order_by('name')
    )
