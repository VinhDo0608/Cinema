# models.py
from django.db import models
from admin_cinema.models import User
from movie.models import Movie
from django.utils import timezone
from cinema.models import Seat

class Reservation(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        # Thêm các lựa chọn thanh toán khác nếu cần
    ]

    # def calculate_total_price():
    #     return Seat.quantity * Seat.price

    # def get_user_email(self):
    #     return self.user.email

    # def get_movie_name(self):
    #     return self.movie.name

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    event_id = models.IntegerField(default=1)
    date = models.DateField(default=timezone.now)
    # total_price = calculate_total_price()
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')

    def __str__(self):
        return f"{self.user.username} - {self.movie_id} - {self.event_id} - {self.date}"