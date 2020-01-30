from django import forms

class NumForm(forms.Form):
    num = forms.IntegerField(
        min_value=1, 
        label="Number to Convert",
        required=True
    )