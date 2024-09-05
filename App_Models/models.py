from django.db import models

# Create your models here.


from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from datetime import timedelta
import random
class CustomBaseUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomBaseUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('Student', 'Student'),
        ('Admin', 'Admin'),
        ('Conten', 'Content'),
    )

    role = models.CharField(max_length=30, choices=USER_TYPE_CHOICES,default='Student')
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.PositiveBigIntegerField(blank=True, null=True)
    slug_field = models.SlugField(blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_otp_verify=models.BooleanField(default=False)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.otp_created_at = timezone.now()
        self.save()

    def verify_otp(self, otp):
        if self.otp == otp and timezone.now() < self.otp_created_at + timedelta(minutes=10):
            return True
        return False

    

    objects = CustomBaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.slug_field:
            base_slug = slugify(self.name) if self.name else slugify(self.email)
            base_slug =base_slug.lower()
            num = 1
            while CustomBaseUser.objects.filter(slug_field=base_slug).exists():
                base_slug = f"{base_slug}{num}"
                num += 1
            self.slug_field = base_slug
        super().save(*args, **kwargs)

            
########################question and options
class Question(models.Model):
    text = models.CharField(max_length=255 , null=True, blank=True)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
############################content
class Category(models.Model):
    language =models.CharField(max_length=50,)
    
    def __str__(self) -> str:
        return self.language
    
class Subcategory(models.Model):
    category_name=models.ForeignKey(Category, on_delete= models.CASCADE, related_name='category')
    field = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.field
    
class Content(models.Model):
    name =models. ForeignKey(Subcategory, on_delete= models.CASCADE, related_name="subcategory")
    Question=models.CharField(max_length=5000, null=False)
    answer = models.TextField(blank=False , null= False)
    slug =models.SlugField()
    
    def __str__(self) -> str:
        return self.name_self.Question
    