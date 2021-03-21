from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm
from django.contrib import messages

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Account was created sucessfully for '+ username)
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreateForm()
        return render(request, 'signup.html', {'form': form})
