from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['user', 'event', 'movie', 'date', 'quantity', 'total_price', 'payment_method']

    def get_movie_name(self, obj):
        return obj.movie.name if obj.movie else None
