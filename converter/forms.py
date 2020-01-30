from django import forms

class NumForm(forms.Form):
    num = forms.IntegerField(
        min_value=1, 
        max_value=999999999,
        label="Number to Convert",
        required=True
    )