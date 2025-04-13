from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_student(self, user_id, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'student')
        return self.create_user(user_id=user_id, first_name=first_name, last_name=last_name, email=email, password=password, **extra_fields)

    def create_instructor(self, user_id, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'instructor')
        return self.create_user(user_id=user_id, first_name=first_name, last_name=last_name, email=email, password=password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class UserProfile(PermissionsMixin, AbstractBaseUser):
    user_id = models.CharField(max_length=20, primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=20, choices=[('student', 'Student'), ('instructor', 'Instructor'), ('admin', 'Admin')])

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    def save(self, *args, **kwargs):
        if not self.user_id:
            # Generate user ID based on role-specific format
            if self.role == 'instructor':
                # Generate instructor user ID format
                year = datetime.date.today().year % 100
                count = UserProfile.objects.filter(role='instructor').count() + 1
                user_id = f"I-{year:02d}-{count:04d}"
            else:
                # Generate student/admin user ID format
                year = datetime.date.today().year % 100
                count = UserProfile.objects.exclude(role='instructor').count() + 1
                user_id = f"{year:02d}-{count:04d}"
            
            self.user_id = user_id

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email