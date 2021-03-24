from django.shortcuts import render, redirect
from .forms import UserEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from librarian.models import book, book_category, reservation
from django.core.paginator import Paginator
from django.http import HttpResponse

def librarypage(request,id):
    if request.user.is_authenticated and request.user.id == id:
        categories = book_category.objects.all()

        latest_books = book.objects.all().order_by('-created_at')
        latest_page_num = request.GET.get("latest_page",1)
        lp = Paginator(latest_books,20) #20 products per page

        recommended_books = book.objects.all().order_by('-clicks')
        recommended_page_num = request.GET.get("recommended_page",1)
        rp = Paginator(recommended_books,20) #20 products per page

        #handling page number OutOfBound
        try:
            latest_page = lp.page(latest_page_num)
        except:
            latest_page = lp.page(1)
        try:
            recommended_page = rp.page(recommended_page_num)
        except:
            recommended_page = rp.page(1)
        
        return render(request, 'librarypage.html',{'latest_books' : latest_page, 'recommended_books' : recommended_page, 'categories' : categories})
    else:
        return redirect("/")

def book_detail(request,id,bid):
    if request.user.is_authenticated and request.user.id == id:
        book_data = book.objects.get(id=bid)
        return render(request, 'book_detail.html',{'book_data' : book_data})
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
    if request.user.is_authenticated and request.user.id == id:
        reserved_books=book.objects.filter(reservation_id__in=reservation.objects.filter(reserved_by=request.user))
        return render(request,'my_reservation.html',{'reserved_books' : reserved_books})
    else:
        return redirect('/')

def update_book_clicks(request,id,bid):
    if request.user.is_authenticated and request.user.id == id and request.method == 'POST':
        b = book.objects.get(id=bid)
        if b.clicks is None:
            b.clicks=1
        else:
            b.clicks=b.clicks+1
        b.save()
    return HttpResponse("success")

def reserve_book(request,id,bid):
    if request.user.is_authenticated and request.user.id == id and request.method == 'POST':
        b = book.objects.get(id=bid)
        if b.reservation_id is None:
            mpr = reservation.objects.filter(reserved_by=request.user).count()
            if mpr <= 3: #Book reservation limit per user
                reserve = reservation(reserved_by=request.user)
                reserve.save()
                b.reservation_id = reserve
                b.save()
                return HttpResponse("success")
            else:
                return HttpResponse("Your reservation limit already reached.")
        else:
            return HttpResponse("Your request failed. Book already reserved.")