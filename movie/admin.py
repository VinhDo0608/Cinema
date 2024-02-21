from django.contrib import admin
from .models import Actor, Director, Movie, Category, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    # filter_horizontal = ('actors',)  # Cho phép chọn nhiều diễn viên trong giao diện quản trị

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'category', 'actor', 'director' )


model_admin_pairs = [
    (Actor, ActorAdmin),
    (Director, DirectorAdmin),
    (Category, CategoryAdmin),
    (Movie, MovieAdmin),
]

# Sử dụng vòng lặp để đăng ký từng cặp
for model, admin_class in model_admin_pairs:
    admin.site.register(model, admin_class)
