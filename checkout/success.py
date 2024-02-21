from django.core.mail import send_mail
from django.conf import settings

def send_booking_confirmation_email(to_email, movie_name, quantity, booking_time):
    subject = 'Đặt vé thành công'
    message = f"Bạn đã đặt vé thành công cho phim '{movie_name}' vào lúc {booking_time}. Số lượng vé: {quantity}."
    from_email = settings.DEFAULT_FROM_EMAIL  # Sử dụng địa chỉ email mặc định được cấu hình trong settings.py

    send_mail(subject, message, from_email, [to_email])