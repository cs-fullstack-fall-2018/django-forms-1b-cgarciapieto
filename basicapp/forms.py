from django import forms



class FormName(forms.Form):
    name = forms.CharField
    email = forms.EmailField
    email2 = forms.EmailField
    url = forms.CharField(widget=forms.Textarea)


def clean(self):
    all_clean_data = super().clean()
    e1 = all_clean_data.get('email')
    e2 = all_clean_data.get('email2')
    if (e1 != e2):
        print("Invalid data")
        raise forms.ValidationError("Emails dont match")

    return all_clean_data
