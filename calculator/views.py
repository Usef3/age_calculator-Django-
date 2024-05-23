from django.shortcuts import render
from datetime import date
from .forms import DateOfBirthForm


def calculate_age_view(request):
    age = None
    if request.method == 'POST':
        form = DateOfBirthForm(request.POST)
        if form.is_valid():
            date_of_birth = form.cleaned_data['date_of_birth']
            today = date.today()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    else:
        form = DateOfBirthForm()

    return render(request, 'calculator/age_calculator.html', {'form': form, 'age': age})
