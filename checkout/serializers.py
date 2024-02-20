from rest_framework import serializers
from .models import MovieTicket

class MovieTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTicket
        fields = '__all__'