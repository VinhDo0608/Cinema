from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models

class UserManager(BaseUserManager):


    def create_user(self,request, username, email, password=None):

        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        
        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('Password should not be none')
        
        user = self.create_user(username, email, password)
        user.is_supperuser=True
        user.is_staff=True
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, unique=False, db_index=True,null=True, blank=True)
    last_name = models.CharField(max_length=255, unique=False, db_index=True, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        return ''




    