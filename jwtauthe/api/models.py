from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
#from phonenumber_field.modelfields import PhoneNumberField



# -------------------------- Custome User Manager -----------------------

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, age,  **extra_fields):
        if not email:
            raise ValueError(" Email is Required for the Registration.")

        if not first_name:
            raise ValueError(" First Name is Required for the Registration.")

        if not age:
            raise ValueError(" Age is Required for the Registration.")

        email = self.normalize_email(email)
        first_name = self.normalize_email(first_name)
        

        user = self.model(email=email,age=age, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user


    def create_superuser(self, email, password, first_name, age,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, first_name, age, **extra_fields)

# --------------------------------------------------------------------------------------------



# --------------------------- Custome User Model -----------------------------------------------

class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ("Male", 'male'),
        ("Female", 'female'),
        ("Others", 'other')
    )

    first_name = models.CharField(verbose_name="First Name",  max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Last Name")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default= "Male")
    age = models.IntegerField(verbose_name="Age",)
    email = models.EmailField(max_length=128, unique=True, verbose_name="Email", primary_key=True)
    #phone = PhoneNumberField(null=True, blank=True, verbose_name = "Mobile No")
    password = models.CharField(max_length=128, verbose_name= "Password")
    adddress = models.CharField(max_length=500, null=True, blank=True, verbose_name="Address")
    pincode = models.IntegerField( null=True, blank=True, verbose_name="Pin Code")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'age']

    objects = UserManager()

    def __str__(self):
        return self.first_name

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_staff

    