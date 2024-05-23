from django import forms


class DateOfBirthForm(forms.Form):
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2024))
    )
