from django.urls import path, include
from .views import MovieSerializer
from rest_framework.routers import DefaultRouter
from .views import AddMovieAPIView, ActorListCreateView, CategoryListCreateView, DirectorListCreateView, MovieViewSet

# router = DefaultRouter()
# router.register(r'movies', MovieViewSet, basename='movie')
# urlpatterns = router.urls

urlpatterns = [
    path('add_movie/', AddMovieAPIView.as_view(), name='add_movie'),
    path('actors/', ActorListCreateView.as_view(), name='actor-list-create'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('directors/', DirectorListCreateView.as_view(), name='director-list-create'),
]