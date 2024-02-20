from django.urls import path
from .views import reserve_ticket, reservation_success, home

urlpatterns = [
    path('home/', home, name='home'),
    path('reserve-ticket/', reserve_ticket, name='reserve_ticket'),
    path('reservation-success/', reservation_success, name='reservation_success'),
]