# authentication/views.py

from .forms import RegistrationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    
    return render(request, 'authentication/register.html', {'form': form})
