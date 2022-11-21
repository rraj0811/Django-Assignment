from django import forms
from Cars.models import otherDetails


class InputForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=300)
    phonenumber = forms.CharField(max_length=10)
    NumberOfDays = forms.IntegerField()

    class Meta:

        model = otherDetails
        fields = ['username', 'Address', 'phonenumber', 'NumberOfDays']
