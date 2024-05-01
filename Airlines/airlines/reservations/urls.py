from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('sign-in/',views.signin, name = 'signin'),
    path('sign-up/',views.signup, name = 'signup'),
    path('profile/', views.profile, name='profile'),
    path('book/',views.book, name = 'book'),
    path('logout/', views.logoutPage, name='logout'),
    path('feedback/',views.feedback,name='feedback'),
    path('flights/', views.flights, name='flights'),
    path('filter-flights/', views.filter_flights, name='filter_flights'),
    path('ticket/',views.ticket,name='ticket'),
    path('clear/',views.clear,name='clear'),


    path('flights/', views.available_flights, name='available_flights'),
    path('book_flight/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('payment/', views.payment_page, name='payment'),  # Define this view for the payment page
    path('book_flight/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('payment/', views.payment_page, name='payment_page'),
    path('confirmPayment/', views.confirmPayment, name='confirmPayment'),
    path('thankyou/', views.thankyou, name='thankyou'),


    path('flights/', views.available_flights, name='available_flights'),
    path('payment/<int:flight_id>/', views.payment_page, name='payment_page'),

]



