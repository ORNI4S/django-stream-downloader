from django import forms




class linkform(forms.Form) : 
    link= forms.CharField(max_length=2000)