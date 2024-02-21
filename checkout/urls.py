from django.urls import path
from .views import reserve_ticket, reservation_success, home, movie_list, movie_detail

app_name = 'checkout'

urlpatterns = [
    path('movie-detail/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movie_list/', movie_list, name='movie_list'),
    path('home/', home, name='home'),
    path('reserve-ticket/', reserve_ticket, name='reserve_ticket'),
    path('reservation-success/', reservation_success, name='reservation_success'),
]