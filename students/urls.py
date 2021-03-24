from django.urls import path
from . import views

urlpatterns= [
    path('library/',views.librarypage,name='library_page'),
    path('my-reservations/',views.my_reservations,name='my_reservations'),
    path('library/book/<int:bid>/reserve-book',views.reserve_book,name='reserve_book'),
    path('edit/',views.edit_user,name='edit_user'),
    path('password/',views.change_user_password,name='change_user_password'),
    path('library/book/<int:bid>/',views.book_detail,name='book_detail_page'),
    path('library/book/<int:bid>/update-clicks',views.update_book_clicks,name='update_book_clicks'),
]