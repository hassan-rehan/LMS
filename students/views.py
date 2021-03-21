from django.shortcuts import render, redirect

def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect("/")

