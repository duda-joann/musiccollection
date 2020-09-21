from django.contrib.auth import login, authenticate
from .forms import UserRegistration
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistration()
    return render(request, 'auth/signup.html', {'form': form})

