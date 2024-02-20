# import re
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from .forms import CreateUserForm
# from django.contrib.auth import authenticate, login, logout

# Create your views here.

# def signup(request):
#     form =  CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Account Created! You can Login')
#             return redirect('signin')
    
#     context = {'form': form}
#     return render(request, 'UserProfile/signup.html', context)

# def signin(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('checkout')
           
#         else:
#             messages.info(request, 'Invalid credentials')
            

# def signout(request):
#     logout(request)
#     return redirect('index')
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from admin_cinema.models import User
from .serializers import UserSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Để yêu cầu đăng nhập để xem danh sách người dùng

@api_view(['POST'])
def signup_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signin_api(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    