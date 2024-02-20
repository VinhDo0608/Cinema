from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Reservation
from .forms import ReservationForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
def reserve_ticket(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()

    movies = Movie.objects.all()
    return render(request, 'reserve_ticket.html', {'form': form, 'movies': movies})

@login_required
def reservation_success(request):
    return render(request, 'reservation_success.html')

def home(request):
    return render(request, 'base.html')