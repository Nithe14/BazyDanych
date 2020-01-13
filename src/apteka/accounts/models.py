from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, phone_number, street, flat_number, post_code, city, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have an email name')
        if not surname:
            raise ValueError('Users must have an email surname')
        if not phone_number:
            raise ValueError('Users must have an email phone number')
        if not street:
            raise ValueError('Users must have an email street')
        if not flat_number:
            raise ValueError('Users must have an email flat number')
        if not post_code:
            raise ValueError('Users must have an email post code')
        if not city:
            raise ValueError('Users must have an email city')

        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.name           = name
        user.surname        = surname
        user.phone_number   = phone_number
        user.street         = street
        user.flat_number    = flat_number
        user.postcode       = post_code
        user.city           = city

        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, phone_number, street, flat_number, post_code, city, password):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a full name")
        if not surname:
            raise ValueError("User must have a full surname")
        if not phone_number:
            raise ValueError('Users must have an email phone number')
        if not street:
            raise ValueError('Users must have an email street')
        if not flat_number:
            raise ValueError('Users must have an email flat number')
        if not post_code:
            raise ValueError('Users must have an email post code')
        if not city:
            raise ValueError('Users must have an email city')
        user            = self.create_user(
            email,
            name=name,
            surname=surname,
            phone_number=phone_number,
            street=street,
            flat_number=flat_number,
            post_code=post_code,
            city=city,
            password= password,

        )
        user.set_password(password)

        user.set_password(password)
        user.name = name
        user.surname = surname
        user.phone_number = phone_number
        user.street = street
        user.flat_number = flat_number
        user.postcode = post_code
        user.city = city

        user.staff      = True
        user.admin      = True
        user.active     = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email        = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name         = models.CharField(max_length=255, blank=True, null=True)
    surname      = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    street       = models.CharField(max_length=255, blank=True, null=True)
    flat_number  = models.CharField(max_length=255, blank=True, null=True)
    post_code    = models.CharField(max_length=255, blank=True, null=True)
    city         = models.CharField(max_length=255, blank=True, null=True)

    staff        = models.BooleanField(default=False)
    admin        = models.BooleanField(default=False)
    active       = models.BooleanField(default=False)
    timestamp    = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname',  'phone_number', 'street', 'flat_number', 'post_code', 'city']

    def __str__(self):
        return self.email

################### GETS #######################
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_phone_number(self):
        return self.phone_number

    def get_postcode(self):
        return self.post_code

    def get_street(self):
        return self.street

    def get_flat_number(self):
        return self.flat_number

    def get_city(self):
        return self.city
###################################################

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = UserManager()