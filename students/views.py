from django.shortcuts import render, redirect
from .forms import UserEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from librarian.models import book, book_category, reservation, latest_visited_book
from django.core.paginator import Paginator
from django.http import HttpResponse
from . import model

def librarypage(request,id):
    if request.user.is_authenticated and request.user.id == id:
        #fetching categories
        categories = book_category.objects.all()
        #searching
        keyword = request.GET.get("filter",None)
        if keyword == "":
            keyword = None
        filter_type = request.GET.get("filter_type",None)
        try:
            if filter_type == "" or filter_type == "None" or not book_category.objects.filter(id=int(filter_type)).exists():
                filter_type = None
        except:
            filter_type = None

        filter_page = []
        if keyword or filter_type:
            filter_books = []
            if keyword and filter_type:
                filter_books=book.objects.filter(category_id = book_category.objects.get(id=int(filter_type))).filter(title__icontains=keyword).order_by('-clicks')
            elif keyword:
                filter_books = book.objects.filter(title__icontains=keyword).order_by('-clicks')
            else:
                filter_books=book.objects.filter(category_id = book_category.objects.get(id=int(filter_type))).order_by('-clicks')
            filter_page_num = request.GET.get("filter_page",1)
            fp = Paginator(filter_books,20)
            #handling page number OutOfBound
            try:
                filter_page = fp.page(filter_page_num)
            except:
                filter_page = fp.page(1)
        
        #latest page section
        latest_books = book.objects.all().order_by('-created_at')
        latest_page_num = request.GET.get("latest_page",1)
        lp = Paginator(latest_books,20) #20 products per page
        #handling page number OutOfBound
        try:
            latest_page = lp.page(latest_page_num)
        except:
            latest_page = lp.page(1)
        
        #Using model with recommended page section
        recommended_page = []
        if latest_visited_book.objects.filter(user=request.user).exists():
            lvb=latest_visited_book.objects.get(user=request.user)
            #getting recomendation book IDs of all latest 5 books visited by the user
            recommend_ids=[]
            if lvb.book_1:
                recommend_ids=model.desc_recommend(lvb.book_1.id,lvb.book_1.category_id.id)
            if lvb.book_2:
                recommend_ids=recommend_ids+model.desc_recommend(lvb.book_2.id,lvb.book_2.category_id.id)
            if lvb.book_3:
                recommend_ids=recommend_ids+model.desc_recommend(lvb.book_3.id,lvb.book_3.category_id.id)
            if lvb.book_4:
                recommend_ids=recommend_ids+model.desc_recommend(lvb.book_4.id,lvb.book_4.category_id.id)
            if lvb.book_5:
                recommend_ids=recommend_ids+model.desc_recommend(lvb.book_5.id,lvb.book_5.category_id.id)
            #Removing duplicates
            recommend_ids=list(dict.fromkeys(recommend_ids))
            #getting books data
            recommended_books = book.objects.filter(id__in=recommend_ids).order_by('-clicks')
            #getting page number
            recommended_page_num = request.GET.get("recommended_page",1)
            #pagination
            rp = Paginator(recommended_books,20) #20 products per page
            try:
                recommended_page = rp.page(recommended_page_num)
            except:
                recommended_page = rp.page(1)
        
        return render(request, 'librarypage.html',{'latest_books' : latest_page, 'recommended_books' : recommended_page, 'filtered_books' : {'books': filter_page,'filter' : keyword, 'filter_type' : filter_type}, 'categories' : categories})
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
        #updating clicks
        b = book.objects.get(id=bid)
        if b.clicks is None:
            b.clicks=1
        else:
            b.clicks=b.clicks+1
        b.save()

        #updating last visited books
        if  latest_visited_book.objects.filter(user=request.user).exists():
            lbv=latest_visited_book.objects.get(user=request.user)
            lbv.book_5 = lbv.book_4
            lbv.book_4 = lbv.book_3
            lbv.book_3= lbv.book_2
            lbv.book_2 = lbv.book_1
            lbv.book_1 = b
            lbv.save()
        else:
            lbv=latest_visited_book(user=request.user,book_1=b)
            lbv.save()
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