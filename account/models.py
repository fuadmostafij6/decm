from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        if email is None:
            raise ValueError('User Must have a email')

        # first_name = first_name.title()
        # last_name = last_name.title()
        # username = username.title()

        user = self.model(
            email=email,
            # first_name=first_name,
            # last_name=last_name,
            # username=username,
            **extra_fields


        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email=email, password=password, **extra_fields)


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self,perm, obj=None ):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
