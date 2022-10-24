from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an Username')
        
        user = self.model(
            email = self.normalize_email(email), #  If you enter email address in captital format it will make it normalize
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email), #  If you enter email address in captital format it will make it normalize
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser, PermissionsMixin):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    username    = models.CharField(max_length=50, unique=True)
    email       = models.EmailField(max_length=100,unique=True)
    newsletter  = models.BooleanField(default=False)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=False)
    is_superadmin    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['username', 'first_name','last_name']

    objects = MyAccountManager()

    def __str__(self): # When we return the object in side the template so this should return the email address
        return self.email
    
    def has_perm(self, perm, obj=None): # if the user is the admin then he has all the permissions
        return self.is_admin 

    def has_module_perms(self, add_label):
        return True

    def name(self):
        return f'{self.first_name} {self.last_name}' 


class Report(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    country = models.CharField(max_length=10)
    state   = models.CharField(max_length=10)
    # phone_number = models.CharField(max_length=12, default=False)
    crime = models.TextField(max_length=10)
    description =  models.TextField(max_length=200, null=True, default=True, blank=True)
    proof = models.FileField(upload_to='dashboard\proof', null=False, default=False)
    reported_at = models.DateTimeField(auto_now_add = True)



    def name(self):
        return f'{self.user.f_name} {self.user.l_name}'


class Anonymous_report(models.Model):
    country = models.CharField(max_length=10)
    state   = models.CharField(max_length=10)
    crime = models.TextField(max_length=10)
    description =  models.TextField(max_length=200, null=True, default=True, blank=True)
    proof = models.FileField(upload_to='dashboard\proof', null=False, default=False)
    reported_at = models.DateTimeField(auto_now_add = True)

    def name(self):
        return f'{self.user.f_name} {self.user.l_name}'