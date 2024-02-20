
from rest_framework import serializers
from .models import Movie, Actor, Director, Category

class MovieSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    directors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'created_date', 'updated_date', 'description', 'status', 'name', 'image',
                  'duration_time', 'release_day', 'language', 'trailer', 'categories', 'actors', 'directors']

    def get_categories(self, obj):
        return obj.category.name if obj.category else None

    def get_actors(self, obj):
        return obj.actor.name if obj.actor else None

    def get_directors(self, obj):
        return obj.director.name if obj.director else None
    
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'