from django.shortcuts import render
from rest_framework import generics, status, viewsets
from .models import Movie
from django.views import View
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class AddMovieAPIView(APIView):

    def get(self, request):
        query = Movie.objects.all()
        serializer = MovieSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer