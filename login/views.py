from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, user.first_name.upper()+', You successfully login into your account.')
            return redirect('/'+str(user.id)+'/library')
        else:
            messages.success(request,'Your username or password is incorrect.')
            return redirect('/login')
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')
