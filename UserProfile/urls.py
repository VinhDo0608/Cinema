from django.urls import path
from .views import signup_api, signin_api, UserListView

urlpatterns = [
    path('api/users/', UserListView.as_view(), name='user-list'),
     path('api/signup/', signup_api, name='signup_api'),
    path('api/signin/', signin_api, name='signin_api'),
     # path('signout/', views.signout, name = 'signout'),
]
 