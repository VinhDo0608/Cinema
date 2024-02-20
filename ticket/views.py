from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.response import Response

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request):
        query = Ticket.objects.all()
        serializer = TicketSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
