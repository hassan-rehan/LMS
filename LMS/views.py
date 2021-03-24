from django.shortcuts import render
from librarian.models import book

def landingpage(request):
    recent_books=book.objects.all().order_by('-created_at')[:8]
    return render(request, 'landing.html',{'recent_books' : recent_books})