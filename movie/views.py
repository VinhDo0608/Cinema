from django.shortcuts import render
from rest_framework import generics, status, viewsets
from .models import Movie, Actor, Category, Director
from django.views import View
from .serializers import MovieSerializer, ActorSerializer, CategorySerializer, DirectorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class AddMovieAPIView(APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

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

class ActorListCreateView(APIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        query = Actor.objects.all()
        serializer = ActorSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryListCreateView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DirectorListCreateView(APIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get(self, request):
        query = Director.objects.all()
        serializer = DirectorSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)