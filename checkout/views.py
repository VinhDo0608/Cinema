from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reservation
from admin_cinema.models import User
from movie.models import Movie
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
            user = request.user
            user.points += 10  # Tăng điểm
            user.save()  # Lưu thay đổi
            return redirect('checkout:reservation_success')
    else:
        form = ReservationForm()

    movies = Movie.objects.all()
    return render(request, 'reserve_ticket.html', {'form': form, 'movies': movies})

# @login_required(login_url="admin:login")
# def reserve_ticket(request, movie_id):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             # Giả sử form này đã bao gồm tất cả trừ user và movie
#             reservation = form.save(commit=False)
#             reservation.user = request.user
#             # Tìm movie dựa trên movie_id và gán cho reservation
#             reservation.movie = Movie.objects.get(id=movie_id)
#             reservation.save()


#             user = request.user
#             user.points += 10  # Tăng điểm
#             user.save()  # Lưu thay đổi
#             return redirect('checkout:reservation_success')
#     else:
#         form = ReservationForm() 
    
#     movies = Movie.objects.all()
#     user_email = request.user.email  # Được sử dụng để hiển thị hoặc xử lý khác, không lưu trực tiếp vào model Reservation
#     selected_movie = Movie.objects.get(id=movie_id)
#     movie_name = selected_movie.name  # Tương tự như trên, dùng để hiển thị hoặc xử lý khác
    
#     # Chú ý: Phần tạo đối tượng Reservation dưới đây không cần thiết nếu bạn đã xử lý ở trên
#     # và có thể gây lỗi nếu bạn thực hiện nó ngoài block 'if POST' mà không kiểm tra dữ liệu đầu vào

#     context = {
#         'form': form,
#         'movies': movies,
#         'user_email': user_email,  # Đưa vào context để có thể sử dụng trong template
#         'movie_name': movie_name,  # Tương tự như trên
#     }

#     return render(request, 'reserve_ticket.html', context)

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
    actors = movie.actors.all()  # Lấy danh sách diễn viên của phim
    print(actors)
    return render(request, 'movie_detail.html', {'movie': movie, 'actors': actors})