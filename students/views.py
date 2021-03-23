from django.shortcuts import render, redirect
from .forms import UserEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from librarian.models import book

def librarypage(request,id):
    if request.user.is_authenticated:
        latest_books = book.objects.all()
        return render(request, 'librarypage.html',{'latest_books' : latest_books})
    else:
        return redirect("/")

def edit_user(request,id):
    if request.user.is_authenticated and request.user.id == id:
        if request.method == 'POST':
            form = UserEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'Account updated sucessfully.')
                return redirect('/'+str(id)+'/edit')
            else:
                return render(request, 'edit_user.html', {'form': form})
        else:
            form = UserEditForm(instance=request.user)
            return render(request, 'edit_user.html', {'form': form})
    else:
        return redirect('/')

def change_user_password(request,id):
    if request.user.is_authenticated and request.user.id == id:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'Password updated sucessfully.')
                return redirect('/'+str(id)+'/password')
            else:
                return render(request, 'edit_user_password.html', {'form': form})
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request, 'edit_user_password.html', {'form': form})
    else:
        return redirect('/')

def my_reservations(request,id):
    return redirect('/')