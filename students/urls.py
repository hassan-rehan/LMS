from django.urls import path
from . import views

urlpatterns= [
    path('library/',views.librarypage,name='library_page'),
    path('my-reservations/',views.my_reservations,name='my_reservations'),
    path('edit/',views.edit_user,name='edit_user'),
    path('password/',views.change_user_password,name='change_user_password'),
]