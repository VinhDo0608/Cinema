from django.urls import path, include
from .views import MovieSerializer, MovieRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, AddMovieAPIView

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
urlpatterns = router.urls

urlpatterns = [
    path('add_movie/', AddMovieAPIView.as_view(), name='add_movie'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-retrieve-update-destroy'),
]