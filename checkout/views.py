from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Reservation
from .forms import ReservationForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required(login_url="admin:login")
def reserve_ticket(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('checkout:reservation_success')
    else:
        form = ReservationForm()

    movies = Movie.objects.all()
    return render(request, 'reserve_ticket.html', {'form': form, 'movies': movies})

@login_required(login_url="admin:login")
def reservation_success(request):
    return render(request, 'reservation_success.html')

def home(request):
    return render(request, 'home.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})